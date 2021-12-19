from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class FirstScreen(Screen):
    def search_image(self):
        pass


class RootWidget(ScreenManager):
    pass


# We create a MainApp class for our application and inherit the App class from Kivy
class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
