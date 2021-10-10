from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty, NumericProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.behaviors import CoverBehavior

import httpclient
from models import Pizza
from storage_manager import StorageManager


class PizzaWidget(BoxLayout):
    name = StringProperty()
    ingredients = StringProperty()
    price = NumericProperty()
    vegetarian = BooleanProperty()



class MainWidget(FloatLayout):
    recycleView = ObjectProperty(None)
    error_str = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.pizzas = [
        #     Pizza("4 cheeses", "mozarella, emmental, brie, blue cheese", 9.5, True),
        #     Pizza("Chorizo", "tomato, chorizo,cheese", 11.2, False),
        #     Pizza("Calzone", "cheese, ham, mushrooms", 10, False)
        # ]
        httpclient.HttpClient().get_pizzas(self.on_server_data, self.on_server_error)

    def on_parent(self, widget, parent):
        pizzas_dict = StorageManager().load_data("pizzas")
        if pizzas_dict:
            self.recycleView.data = pizzas_dict

    def on_server_data(self, pizzas_dict):
        self.recycleView.data = pizzas_dict
        StorageManager().save_data("pizzas", pizzas_dict)

    def on_server_error(self, error):
        print("ERROR" + error)
        self.error_str = "ERROR: " + error



with open("pizzascr.kv", encoding='utf8') as f:
    Builder.load_string(f.read())

class PizzaApp(App):
    def build(self):
        return MainWidget()


PizzaApp().run()
