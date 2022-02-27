from kivymd.app import MDApp
from kivy.uix.button import Button
from kivymd.uix.button import MDFlatButton
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivymd.uix.dialog import MDDialog
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder
import sqlite3
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from plyer import filechooser
from kivy.uix.anchorlayout import AnchorLayout

s = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    LoginScreen:
    SignupScreen:
    ClientsTable:
    firstpage:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'new'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'Clientstable'
    MDRectangleFlatButton:
        text: 'backlogin'
        pos_hint: {'center_x':0.5,'center_y':0.4}
        on_press: root.manager.current = 'login'
<ProfileScreen>:
    name: 'profile'
    MDLabel:
        text: 'Profile'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x':0.5,'center_y':0.1}
        on_press: root.manager.current = 'menu' 
<UploadScreen>:
    name: 'upload'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Entered'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5

        MDLabel:
            text: 'hello world'
            halign: 'center'
        MDBottomAppBar:
            MDToolbar:
                title: 'Demo'
                icon: 'language-python'
                type: 'bottom'
                left_action_items: [["coffee", lambda x: app.navigation_draw()]]
                on_action_button: root.manager.current = 'menu' 



<LoginScreen>:
    name:"login"
    MDFloatLayout:

        MDTextField:
            id:email
            hint_text: "Enter username"
            helper_text: "or click on forgot username"
            helper_text_mode: "on_focus"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            size_hint_x:None
            width:300

        MDTextField:
            id:password
            hint_text: "Enter password"
            helper_text: "or click on forgot password"
            helper_text_mode: "on_focus"
            icon_right: "lock"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.58}
            size_hint_x:None
            width:300
        MDRaisedButton:
            text:"LOGIN"
            pos_hint:{'center_x': 0.6, 'center_y': 0.5}
            md_bg_color: 1, 0, 1, 1
            on_press:app.log()
        MDRaisedButton:
            text:"SIGNUP"
            pos_hint:{'center_x': 0.4, 'center_y': 0.5}
            md_bg_color: 1, 0, 1, 1
            on_press:root.manager.current = 'signup'   
<SignupScreen>:
    name: 'signup'
    MDFloatLayout:

        MDTextField:
            id:email
            hint_text: "Enter username"
            helper_text: "or click on forgot username"
            helper_text_mode: "on_focus"
            icon_right: "android"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.7}
            size_hint_x:None
            width:300

        MDTextField:
            id:password
            hint_text: "Enter password"
            helper_text: "or click on forgot password"
            helper_text_mode: "on_focus"
            icon_right: "lock"
            icon_right_color: app.theme_cls.primary_color
            pos_hint:{'center_x': 0.5, 'center_y': 0.58}
            size_hint_x:None
            width:300
        MDRaisedButton:
            text:"SIGNUP"
            pos_hint:{'center_x': 0.6, 'center_y': 0.5}
            md_bg_color: 1, 0, 1, 1
            on_press:app.create() 
        MDRaisedButton:
            text: 'Backlogin'
            pos_hint: {'center_x':0.4,'center_y':0.5}
            md_bg_color: 1, 0, 1, 1
            on_press: root.manager.current = 'login'
<firstpage>:
    name:'new'
    
    MDBoxLayout:
        id: main_layout
        orientation: 'vertical'
        padding: dp(20)

        MDLabel:
            text: "Records Manager"
            font_size: dp(20)
            halign: 'center'
            padding_y: dp(20)
            size_hint_y: None
            height: self.texture_size[1]

        MDGridLayout:
            adaptive_height: True
            cols: 2
            MDBoxLayout:
                MDLabel:
                    text: "Record Id"
                MDLabel:
                    id: record_id
                    text: ''
            Widget:

            MDTextField:
                id: matter_name
                hint_text: "Matter Name"

            MDTextField:
                id: file_name
                hint_text: "File name"

            MDTextField:
                id: description
                hint_text: "Description"

            MDTextField:
                id: location
                hint_text: "Location"

        MDBoxLayout:
            adaptive_height: True
            spacing: dp(50)
            padding: dp(20)

            MDRectangleFlatButton:
                text: "Clear Form"
                on_press: app.clear_form()

            MDRectangleFlatButton:
                text: "Add Record"
                on_press: app.add_record()

            MDRectangleFlatButton:
                text: "Update Record"
                on_press: app.update_record()

            MDRectangleFlatButton:
                text: "Delete Record"
                on_press:root.manager.current = 'Clientstable'   


<ClientsTable>:
    name: 'Clientstable'



        """
LO = '''
MDScreen:
    name:"pre"
    MDFloatLayout:
        md_bg_color: 115/255.0, 62/255.0, 198/255.0, 1
        MDLabel:
            text:"Welcome"
            pos_hint:{"center_x": .5, "center_y": .2}
            halign:"center"
            theme_text_color:"Custom"
            text_color: 1, 1, 1, 1
            font_size:"35sp"
        MDLabel:
            text:"App by santhoshkumar"
            pos_hint:{"center_x": .5, "center_y": .15}
            halign:"center"
            theme_text_color:"Custom"
            text_color: 1, 1, 1, 1
            font_size:"14sp"

     '''


class ClientsTable(Screen):
    def load_table(self):
        layout = AnchorLayout()
        self.data_tables = MDDataTable(
            pos_hint={'center_y': 0.5, 'center_x': 0.5},
            size_hint=(0.9, 0.6),
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("Head 1", dp(30)),
                ("Head 2", dp(30)),
                ("Head 3", dp(30)),
                ("Head 4", dp(30)), ],
            row_data=[
                (f"{i + 1}", "", "", "", "")
                for i in range(50)], )
        self.add_widget(self.data_tables)
        return layout

    def on_enter(self):
        self.load_table()


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
    pass


class firstpage(Screen):
    pass


class LoginScreen(MDScreen):
    pass


class SignupScreen(Screen):
    pass


class MainApp(MDApp):

    def build(self):
        global scr
        scr = ScreenManager()
        Builder.load_string(s)
        conn = sqlite3.connect("accounts.db")
        c = conn.cursor()

        c.execute('''CREATE TABLE if not exists accounts 
        		(uname text, pwd text)''')
        conn.commit()
        conn.close()
        self.theme_cls.primary_palette = "Orange"
        scr.add_widget((Builder.load_string(LO)))

        scr.add_widget((Builder.load_string(LO)))
        scr.add_widget(MenuScreen(name='menu'))
        scr.add_widget(ProfileScreen(name='profile'))
        scr.add_widget(UploadScreen(name='upload'))
        scr.add_widget(LoginScreen(name='login'))
        scr.add_widget(SignupScreen(name='signup'))
        scr.add_widget(ClientsTable(name='Clientstable'))
        scr.add_widget(firstpage(name='new'))
        return scr

    def navigation_draw(self):
        pass

    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(self, *args):
        scr.current = "login"

    def create(self, *args):
        add = self.root.get_screen('signup')
        email = add.ids["email"].text
        password = add.ids["password"].text
        if (email == ''):
            self.dialog = MDDialog(
                title="INVALID LOGIN",
                text="Please enter corrent login id",
                size_hint=(0.7, 1),
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Error",
                        text_color=self.theme_cls.primary_color, on_release=self.closeDialog
                    ),
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    )
                    , ], )
            self.dialog.open()

        else:
            conn = sqlite3.connect('accounts.db')
            c = conn.cursor()
            c.execute("INSERT INTO accounts VALUES (?, ?)", [email, password])

            self.dialog = MDDialog(
                title="SUCESSFULLY CREATED",
                text="CLICK BACK TO LOGIN PAGE",
                size_hint=(0.7, 1),
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Error",
                        text_color=self.theme_cls.primary_color, on_release=self.closeDialog
                    ), ], )
            self.dialog.open()
            conn.commit()
            conn.close()

    def log(self, *args):
        new = self.root.get_screen('login')
        email = new.ids["email"].text
        password = new.ids["password"].text
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        c.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [email, password])
        if c.fetchone() == None:

            self.dialog = MDDialog(
                title="INVALID LOGIN",
                text="Please enter correct id and password",
                size_hint=(0.7, 1),
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Error",
                        text_color=self.theme_cls.primary_color, on_release=self.closeDialog
                    )
                    , ], )
            self.dialog.open()
        else:
            self.dialog = MDDialog(
                title="WELCOME",
                text=email,
                size_hint=(0.7, 1),
                radius=[20, 7, 20, 7],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Error",
                        text_color=self.theme_cls.primary_color, on_release=self.closeDialog
                    ), ], )
            self.dialog.open()
            scr.current = 'menu'
            conn.commit()
            conn.close()

    def closeDialog(self, inst):
        self.dialog.dismiss()

    def add_record(self):
        new = self.root.get_screen('Clientstable')
        matter = new.ids["matter_name"].text
        file_name = new.ids["file_name"].text
        description = new.ids["description"].text
        location = new.ids["location"].text
        conn = sqlite3.connect("records.db")
        c = conn.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS records (id INTEGER PRIMARY KEY, matter text, filename text, description text, location text)")
        c.execute("INSERT INTO records VALUES (NULL, ?, ?, ?, ?)", (matter, file_name, description, location))
        conn.commit()

    def update_record(self):
        new = self.root.get_screen('Clientstable')
        matter = new.ids["matter_name"].text
        file_name = new.ids["file_name"].text
        description = new.ids["description"].text
        location = new.ids["location"].text
        conn = sqlite3.connect("records.db")
        c = conn.cursor()
        c.execute("INSERT INTO records VALUES (NULL, ?, ?, ?, ?)", (matter, file_name, description, location))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    MainApp().run()
