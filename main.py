from kivymd.app import MDApp
from kivymd.theming import ThemeManager
from kivymd.uix import button
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineAvatarListItem
from kivy.uix.popup import Popup
from kivy.properties import StringProperty 
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.core.window import Window
from kivy.lang import Builder
from os import mkdir, chdir, startfile, getcwd, listdir, remove
from datetime import date, datetime
from sqlite3 import connect
from multiprocessing import Process
from threading import Thread
from kivymd.uix.list.list import OneLineListItem
from win32gui import GetForegroundWindow
import psutil
import time
import win32process
from matplotlib import pyplot as plt

appnm = []
try:
    with open('data.dat', 'r') as file:
        a = file.read()
        l = a.split(";\n")
except:
    pass

myval=""
mylist = [x.split(",") for x in l]
myset = {x[0] for x in mylist}
nval = dict()
num = []

for i in myset:
    nval[i] = 0
try:
    for i in mylist:
        if i[0] in list(myset):
            nval[i[0]] += int(i[1])
except:
    pass

for i in nval:
    num.append(nval[i])

for i in myset:
    myval += f"\t\t\t\t\t\t\tMDLabel:\n\t\t\t\t\t\t\t\ttext:'{i}'\n"




code1='''
ScreenManager:
	OptionScreen:
    RMode1Screen:
    RMode2Screen:
    AppScreen:
    DataScreen:
    AboutScreen:

<OptionScreen>:
	
	name:'opt'
	
	MDNavigationLayout:

		ScreenManager:
			Screen:

                MDFloatLayout:
                    cols:1

                    MDBoxLayout:
                        orientation:'vertical'
                        spacing: 50

                    MDRectangleFlatButton:
                        text: "Normal"
                        pos_hint: {'center_x':0.4, 'center_y':0.5}
                        on_release: 
                            app.root.current = 'rmode1'
                            root.manager.transition.direction = 'up'

                    MDRectangleFlatButton:
                        text: "Parent"
                        pos_hint: {'center_x':0.6, 'center_y':0.5}
                        on_release: 
                            app.root.current = 'rmode2'
                            root.manager.transition.direction = 'up'
                

<RMode1Screen>:

    name:'rmode1'

    nm:nm
    scrt:scrt

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "Welcome to Registration"
                        elevation: 10

                    MDBoxLayout:
                        orientation: 'vertical'

                        Widget:
                            
                        MDTextField:
                            id: nm
                            hint_text:"Enter Your Full Name"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                        MDTextField:
                            id: scrt
                            hint_text:"Enter Your Prefered Screen Time (Usually 3 hours)"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: 15
                        spacing: 15

                        MDRectangleFlatButton:
                            text: "Register"
                            pos_hint:{'center_x':0.5}
                            on_release:
                                root.reg()
                                app.root.current = 'app'
                                root.manager.transition.direction = 'up'

                        MDRectangleFlatButton:
                            text: "Back"
                            pos_hint:{'center_x':0.5}
                            on_release:
                                app.root.current = 'opt'
                                root.manager.transition.direction = 'down'

                        Widget:

<RMode2Screen>:

    name:'rmode2'

    nm:nm
    email:email
    scrt:scrt

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "Welcome to Registration"
                        elevation: 10

                    MDBoxLayout:
                        orientation: 'vertical'

                        Widget:
                            
                        MDTextField:
                            id: nm
                            hint_text:"Enter Full Name"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                        MDTextField:
                            id: email
                            hint_text:"Enter Your Email ID"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                        MDTextField:
                            id: scrt
                            hint_text:"Enter Your Prefered Screen Time (Usually 3 hours)"
                            size_hint: (0.8,0)
                            pos_hint:{'center_x':0.5}
                            multiline:False

                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: 15
                        spacing: 15

                        MDRectangleFlatButton:
                            text: "Register"
                            pos_hint:{'center_x':0.5}
                            on_release: 
                                root.reg()
                                app.root.current = 'app'
                                root.manager.transition.direction = 'up'

                        MDRectangleFlatButton:
                            text: "Back"
                            pos_hint:{'center_x':0.5}
                            on_release:
                                app.root.current = 'opt'
                                root.manager.transition.direction = 'down'

                        Widget:
<AppScreen>:

    name:'app'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "HonestClock"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    ScrollView:
                        do_scroll_x: False
                        size_hint:(None, None)
                        size: (500, 800)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDGridLayout:
                            
                            cols:1
                            row_default_height: '48dp'
                            row_force_default: True
                            padding: 20
                            spacing: 10
                            size_hint: (None, None)
                            size_hint_y: None
                            width: 300
                            height: self.minimum_height

%s



                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'clock'
                            type: 'bottom'
                            mode: 'end'
                            on_action_button:
                                app.root.current = 'data'
                                root.manager.transition.direction = 'up'

        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
                orientation: 'vertical'
                spacing: 25
                padding: 30

                Widget:

                MDFlatButton:
                    text: "Apps  "

                MDRaisedButton:
                    text: "About"
                    on_release:
                        app.root.current = 'about'
                        root.manager.transition.direction = 'up'

                Widget:

<DataScreen>:

    name: 'data'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "HonestClock"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    Widget:

                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: 15

                        MDLabel:
                            text: "Graphical Representation of Data Usage"

                    Image:
                        source: 'graph.png'
                        size_hint_y: None
                        width: 600
                        allow_stretch: True

                    Widget:

                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'clock'
                            type: 'bottom'
                            mode: 'end'

        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
                orientation: 'vertical'
                spacing: 25
                padding: 30

                Widget:

                MDRaisedButton:
                    text: "Apps  "
                    on_release:
                        app.root.current = 'app'
                        root.manager.transition.direction = 'down'

                MDRaisedButton:
                    text: "About"
                    on_release:
                        app.root.current = 'about'
                        root.manager.transition.direction = 'up'

                Widget:

<AboutScreen>:

    name: 'about'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "HonestClock"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    Widget:

                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: 20
                        spacing: 15

                        MDLabel:
                            text: "About App"

                        Image:
                            source: 'logo.png'
                            size_hint_y: None
                            width: 600
                            allow_stretch: True

                        MDLabel:
                            text: "HonestClock is an application that helps you to track your screen time wisely."

                        Widget:

                        MDLabel:
                            text: "Things That We Are Trying To Include:"

                        MDLabel:
                            text: "- Parental Control feature that will allow parents to access app usage and time spent per app data."

                        MDLabel:
                            text: "- Graphical Interpretation for better understanding."

                        MDLabel:
                            text: "- User Friendly GUI."

                    Widget:

                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'clock'
                            type: 'bottom'
                            mode: 'end'
                            on_action_button:
                                app.root.current = 'data'
                                root.manager.transition.direction = 'up'


        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
                orientation: 'vertical'
                spacing: 25
                padding: 30

                Widget:

                MDRaisedButton:
                    text: "Apps  "
                    on_release:
                        app.root.current = 'app'
                        root.manager.transition.direction = 'down'

                MDFlatButton:
                    text: "About"

                Widget: 
'''% '{}'.format(myval)

code2 = '''
ScreenManager:
    AppScreen:
    DataScreen:
    AboutScreen:

<AppScreen>:

    name:'app'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "HonestClock"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    ScrollView:
                        do_scroll_x: False
                        size_hint:(None, None)
                        size: (500, 800)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        MDGridLayout:
                            
                            cols:1
                            row_default_height: '48dp'
                            row_force_default: True
                            padding: 20
                            spacing: 10
                            size_hint: (None, None)
                            size_hint_y: None
                            width: 300
                            height: self.minimum_height

%s



                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'clock'
                            type: 'bottom'
                            mode: 'end'
                            on_action_button:
                                app.root.current = 'data'
                                root.manager.transition.direction = 'up'

        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
                orientation: 'vertical'
                spacing: 25
                padding: 30

                Widget:

                MDFlatButton:
                    text: "Apps  "

                MDRaisedButton:
                    text: "About"
                    on_release:
                        app.root.current = 'about'
                        root.manager.transition.direction = 'up'

                Widget:

<DataScreen>:

    name: 'data'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "HonestClock"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    Widget:

                    MDBoxLayout:
                        orientation: 'vertical'
                        spacing: 15

                        MDLabel:
                            text: "Graphical Representation of Data Usage"

                    Image:
                        source: 'graph.png'
                        size_hint_y: None
                        width: 600
                        allow_stretch: True

                    Widget:

                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'clock'
                            type: 'bottom'
                            mode: 'end'

        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
                orientation: 'vertical'
                spacing: 25
                padding: 30

                Widget:

                MDRaisedButton:
                    text: "Apps  "
                    on_release:
                        app.root.current = 'app'
                        root.manager.transition.direction = 'down'

                MDRaisedButton:
                    text: "About"
                    on_release:
                        app.root.current = 'about'
                        root.manager.transition.direction = 'up'

                Widget:

<AboutScreen>:

    name: 'about'

    MDNavigationLayout:

        ScreenManager:
			Screen:

                MDGridLayout:
                    cols:1

                    MDToolbar:
                        title: "HonestClock"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('toggle')]]

                    Widget:

                    MDBoxLayout:
                        orientation: 'vertical'
                        padding: 20
                        spacing: 15

                        MDLabel:
                            text: "About App"

                        Image:
                            source: 'logo.png'
                            size_hint_y: None
                            width: 600
                            allow_stretch: True

                        MDLabel:
                            text: "HonestClock is an application that helps you to track your screen time wisely."

                        Widget:

                        MDLabel:
                            text: "Things That We Are Trying To Include:"

                        MDLabel:
                            text: "- Parental Control feature that will allow parents to access app usage and time spent per app data."

                        MDLabel:
                            text: "- Graphical Interpretation for better understanding."

                        MDLabel:
                            text: "- User Friendly GUI."

                    Widget:

                    MDBottomAppBar:
                        MDToolbar:
                            icon: 'clock'
                            type: 'bottom'
                            mode: 'end'
                            on_action_button:
                                app.root.current = 'data'
                                root.manager.transition.direction = 'up'


        MDNavigationDrawer:
            id: nav_drawer

            MDBoxLayout:
                orientation: 'vertical'
                spacing: 25
                padding: 30

                Widget:

                MDRaisedButton:
                    text: "Apps  "
                    on_release:
                        app.root.current = 'app'
                        root.manager.transition.direction = 'down'

                MDFlatButton:
                    text: "About"

                Widget: 
'''% '{}'.format(myval)

class OptionScreen(Screen):
    pass
            
class RMode1Screen(Screen):
    
    def reg(self):
        con = connect('user.db')
        cur = con.cursor()
        if len(self.nm.text)>0 and len(self.scrt.text)>0:
            if self.scrt.text.isnumeric():
                try:
                    cur.execute('CREATE TABLE IF NOT EXISTS reg(name TEXT PRIMARY KEY, scrt INTEGER)')
                    cur.execute(f"INSERT INTO reg VALUES ('{self.nm.text}', {int(self.scrt.text)})")
                except Exception as e:
                    dialog = MDDialog (
                            title = 'Error',
                            text = str(e)
                        )
                    dialog.open()
            else:
                dialog = MDDialog (
                            title = 'Error',
                            text = "Enter a Numeric Value for Screen Time"
                        )
                dialog.open()
        else:
            dialog = MDDialog (
                        title = 'Error',
                        text = "Text Field Empty"
                    )
            dialog.open()

class RMode2Screen(Screen):
    
    def reg(self):
        con = connect('user.db')
        cur = con.cursor()
        if len(self.nm.text)>0 and len(self.scrt.text)>0:
            if self.scrt.text.isnumeric():
                try:
                    cur.execute('CREATE TABLE IF NOT EXISTS reg(name TEXT PRIMARY KEY, email TEXT, scrt INTEGER)')
                    cur.execute(f"INSERT INTO reg VALUES ('{self.nm.text}', '{self.email.text}', {int(self.scrt.text)})")
                except Exception as e:
                    dialog = MDDialog (
                            title = 'Error',
                            text = str(e)
                        )
                    dialog.open()
            else:
                dialog = MDDialog (
                            title = 'Error',
                            text = "Enter a Numeric Value for Screen Time"
                        )
                dialog.open()
        else:
            dialog = MDDialog (
                        title = 'Error',
                        text = "Text Field Empty"
                    )
            dialog.open()

        cur.execute('select * from reg')

        r = cur.fetchall()

class AppScreen(Screen):
    pass

class DataScreen(Screen):
    pass

class AboutScreen(Screen):
    pass
            
sm = ScreenManager()
sm.add_widget(OptionScreen(name = 'opt'))
sm.add_widget(RMode1Screen(name = 'rmode1'))
sm.add_widget(RMode2Screen(name = 'rmode2'))
sm.add_widget(AppScreen(name = 'app'))
sm.add_widget(DataScreen(name = 'data'))
sm.add_widget(AboutScreen(name = 'about'))


class HonestClockApp(MDApp):

    global process_time
    global timestamp
    process_time={}
    timestamp = {}

    def ScreenTime(self, *args):
        
        current_app = psutil.Process(win32process.GetWindowThreadProcessId(GetForegroundWindow())[1]).name().replace(".exe", "")
        timestamp[current_app] = int(time.time())
        time.sleep(1)
        if current_app not in process_time.keys():
            process_time[current_app] = 0
        process_time[current_app] = process_time[current_app]+int(time.time())-timestamp[current_app]

    def data(*args):
        return process_time
        
    def build(self):
        self.theme_cls = ThemeManager()
        self.theme_cls.primary_palette='DeepPurple'
        self.theme_cls.primary_hue='900'
        self.icon="logo.png"
        if 'user.db' in listdir():
            self.screen=Builder.load_string(code2)
            try:
                Clock.schedule_interval(self.ScreenTime, 3)
            except Exception as e:
                print(e)
        else:
            self.screen=Builder.load_string(code1)
        self.ScreenTime()
        return self.screen

HonestClockApp().run()



apps_list = nval.keys()     #list of apps which are analysed
explode = []
for i in range(len(apps_list)):
    explode.append(0.1)

plt.pie(num, labels= apps_list, explode = explode, shadow = True, startangle = 90, autopct = "%1.2f%%")
        
plt.title("Screen Usage")
plt.tight_layout()

plt.savefig("graph.png")

data = HonestClockApp.data()
val = ""
try:
    for i in data.keys():
        val += f"{i}, {data[i]};\n"
    with open('data.dat', 'a') as file:
        file.write(val)
except Exception as e:
    pass