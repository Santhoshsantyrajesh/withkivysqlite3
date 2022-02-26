import pyrebase
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
s = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:
    LoginScreen:
    SignupScreen:
<MenuScreen>:
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_press: root.manager.current = 'profile'
    MDRectangleFlatButton:
        text: 'Upload'
        pos_hint: {'center_x':0.5,'center_y':0.5}
        on_press: root.manager.current = 'upload'
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


class MenuScreen(Screen):
    pass


class ProfileScreen(Screen):
    pass


class UploadScreen(Screen):
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
        return scr

    def navigation_draw(self):
        pass

    def on_start(self):
        Clock.schedule_once(self.login, 3)

    def login(self, *args):
        scr.current = "login"

    def create(self, *args):
        add= self.root.get_screen('signup')
        email = add.ids["email"].text
        password=add.ids["password"].text
        try:
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

        except:
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
    def log(self, *args):
        new = self.root.get_screen('login')
        email = new.ids["email"].text
        password = new.ids["password"].text
        conn = sqlite3.connect('accounts.db')
        c = conn.cursor()
        c.execute("SELECT * FROM accounts WHERE uname=? and pwd=?", [email,password])
        if c.fetchone()==None:
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


if __name__ == "__main__":
    MainApp().run()
