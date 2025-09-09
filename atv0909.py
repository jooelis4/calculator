from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculadora(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1


        self.display = TextInput(multiline=False, halign = "right", font_size = 45)

        self.add_widget(self.display)

        botoes = GridLayout(cols = 4)

        lista_botoes = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "c","0","=","+"
        ]

        for texto in lista_botoes:
            botao = Button(text = texto, font_size = 20,)
            botao.bind(on_press = self.clique)
            botoes.add_widget(botao)


        self.add_widget(botoes)

    def clique(self, instance):
        texto = instance.text

        if texto == "c":
            self.display.text = ""
            
        elif texto == "=":
            try:
                self.display.text = str(eval(self.display.text))
            except:
                self.display.text = "Erro"
        else:
            self.display.text += texto

class CalculadoraApp(App):
    def build(self):
        return Calculadora()
    
if __name__ == '__main__':
    CalculadoraApp().run()