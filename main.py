from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3
s="""
MDFloatLayout:
	BoxLayout:
		orientation: "vertical"
		size: root.width, root.height

		Label:
			id: word_label
			text_size: self.size
			halign: "center"
			valign: "middle"
			text: "Enter A Name"
			font_size: 32

		TextInput:
			id: word_input
			multiline: False
			size_hint: (1, .5)

		Button:
			size_hint: (1, .5)
			font_size: 32
			text: "Submit Name"
			on_press: app.submit()

		Button:
			size_hint: (1, .5)
			font_size: 32
			text: "Show Records"
			on_press: app.show_records()"""

class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Create A Table
        c.execute("""CREATE TABLE if not exists customers(
			name text)
		 """)

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

        return Builder.load_string(s)

    def submit(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Add A Record
        c.execute("INSERT INTO customers VALUES (:first)",
                  {
                      'first': self.root.ids.word_input.text,
                  })

        # Add a little message
        self.root.ids.word_label.text = f'{self.root.ids.word_input.text} Added'

        # Clear the input box

        self.root.ids.word_input.text = ''

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

    def show_records(self):
        # Create Database Or Connect To One
        conn = sqlite3.connect('first_db.db')

        # Create A Cursor
        c = conn.cursor()

        # Grab records from database
        c.execute("SELECT * FROM customers")
        records = c.fetchall()

        word = ''
        # Loop thru records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.word_label.text = f'{word}'

        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()


MainApp().run()
