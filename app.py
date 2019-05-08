import f
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout  # one of many layout structures
from kivy.uix.textinput import TextInput  # allow for ...text input.
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy import Config
Config.set('graphics', 'multisamples', '0')

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

#kivy.require("1.10.1")

# An actual app is likely to consist of many different
# "pages" or "screens." Inherit from GridLayout
class InputPage(GridLayout):
    # runs on initialization
    def __init__(self, **kwargs):
        # we want to run __init__ of both ConnectPage AAAAND GridLayout
        super().__init__(**kwargs)

        self.cols = 3  # used for our grid

        # widgets added in order, so mind the order.
        self.add_widget(Label(text='Encrypt:'))  # widget #1, top left
        self.intext = TextInput(multiline=False)  # defining self.ip...
        self.add_widget(self.intext) # widget #2, top right
        self.encryptButton = Button(text = "Encrypt")
        self.encryptButton.bind(on_press = self.encrypt)
        self.add_widget(self.encryptButton)

        self.add_widget(Label(text='Decrypt'))
        self.incrypt = TextInput(multiline=False)
        self.add_widget(self.incrypt)
        self.decryptButton = Button(text = "Decrypt")
        self.decryptButton.bind(on_press = self.decrypt)
        self.add_widget(self.decryptButton)

        self.add_widget(Label(text="Custom Encrypting Alphabet:\n(eg. a,b,c,f,6,d,e,7, ...)\n(Leave blank for default)",halign = "center", valign = "middle"))
        self.customAlphabetText = TextInput(multiline=False)
        self.add_widget(self.customAlphabetText)
        self.addCustomAlphabetButton = Button(text = "Save")
        self.addCustomAlphabetButton.bind(on_press = self.addCustomAlphabet)
        self.add_widget(self.addCustomAlphabetButton)

    def encrypt(self, instance):
        try:
            output = f.encrypt(self.intext.text)
        except Exception as e:
            output = f"Something went wrong: {e}"
        encryptingApp.output_page.update_output(output)
        encryptingApp.screen_manager.current = "Output"

    def decrypt(self, instance):
        try:
            output = f.decrypt(self.incrypt.text)
        except Exception as e:
            output = f"Something went wrong: {e}"
        encryptingApp.output_page.update_output(output)
        encryptingApp.screen_manager.current = "Output"

    def addCustomAlphabet(self, instance):
        f.setCustomAlphabet(self.customAlphabetText.text.split(","))

class OutputPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Just one column
        self.cols = 1

        # And one label with bigger font and centered text
        self.message = TextInput(multiline = True, font_size=30)

        # By default every widget returns it's side as [100, 100], it gets finally resized,
        # but we have to listen for size change to get a new one
        # more: https://github.com/kivy/kivy/issues/1044
        self.message.bind(width=self.update_text_width)

        # Add text widget to the layout
        self.add_widget(self.message)

        self.BackButton = Button(text = "BACK")
        self.BackButton.bind(on_press = self.toInputPage)
        self.add_widget(self.BackButton)

    # Called with a message, to update message text in widget
    def update_output(self, message):
        self.message.text = message

    # Called on label width update, so we can set text width properly - to 90% of label width
    def update_text_width(self, *_):
        self.message.text_size = (self.message.width * 0.9, None)

    def toInputPage(self, instance):
        encryptingApp.screen_manager.current = "Input"

class EpicApp(App):
    def build(self):

        # We are going to use screen manager, so we can add multiple screens
        # and switch between them
        self.screen_manager = ScreenManager()

        # Initial, connection screen (we use passed in name to activate screen)
        # First create a page, then a new screen, add page to screen and screen to screen manager
        self.input_page = InputPage()
        screen = Screen(name="Input")
        screen.add_widget(self.input_page)
        self.screen_manager.add_widget(screen)

        # Info page
        self.output_page = OutputPage()
        screen = Screen(name='Output')
        screen.add_widget(self.output_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
    encryptingApp = EpicApp()
    encryptingApp.run()
