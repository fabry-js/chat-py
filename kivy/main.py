import kivy
import os

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #cols
        self.cols = 2
        
        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt","r") as f:
                d = f.read().split(",")
                prev_ip = d[0]
                prev_port = d[1]
                prev_username = d[2]
        else:
            prev_ip = ''
            prev_port = ''
            prev_username = ''
        
        #IP
        self.add_widget(Label(text="Indirizzo IP: ")) 
        self.ip = TextInput(text=prev_ip, multiline=False)
        self.add_widget(self.ip)
        
        #Porta
        self.add_widget(Label(text="Porta: "))
        self.port = TextInput(text=prev_port, multiline=False)
        self.add_widget(self.port)
        
        #Username
        self.add_widget(Label(text="Username: "))
        self.username = TextInput(text=prev_username, multiline=False)
        self.add_widget(self.username)
        
        #bottone join
        self.join = Button(text="Entra")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)
        
    def join_button(self, instance):
        port = self.port.text
        ip = self.ip.text
        username = self.username.text

        print(f"Tentando di accedere ad {ip}:{port} con il nome {username}")
        
        with open("prev_details.txt", "w") as f:
            f.write(f"{ip},{port},{username}")
        
class EpicApp(App):
    def build(self):
        return ConnectPage()
            
if __name__ == "__main__":
    EpicApp().run()