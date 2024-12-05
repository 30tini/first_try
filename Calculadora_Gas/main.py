import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.spinner import Spinner
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

kivy.require('2.0.0')

class CalculadoraEconomiaCombustivelApp(App):
    def build(self):
        Window.clearcolor = (0.1, 0.3, 0.1, 1)  # Dark green background
        self.title = "Calculadora de Economia de Combustível"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        # Title Label
        title_label = Label(
            text='Calculadora de Economia de Combustível',
            font_size=28,
            bold=True,
            color=(0.9, 1, 0.9, 1)  # Light green text
        )
        layout.add_widget(title_label)

        # Spinner para tipos de veículo
        self.vehicle_spinner = Spinner(
            text='Selecione o Tipo de Veículo',
            values=('Carro', 'Moto', 'Caminhão', 'Van'),
            size_hint=(None, None),
            size=(250, 44)
        )

        # Spinner para tipos de combustível
        self.fuel_spinner = Spinner(
            text='Selecione o Tipo de Combustível',
            values=('Gasolina', 'Álcool', 'Diesel', 'Elétrico'),
            size_hint=(None, None),
            size=(250, 44)
        )

        # Entrada de detalhes do carro
        self.distance_input = TextInput(
            hint_text='Distância percorrida (km)',
            multiline=False,
            input_filter='float',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.5, 0.2, 1),  # Darker green for input
            foreground_color=(1, 1, 1, 1),  # White text
            padding=(10, 10)
        )
        self.fuel_input = TextInput(
            hint_text='Combustível consumido (litros)',
            multiline=False,
            input_filter='float',
            size_hint_y=None,
            height=50,
            background_color=(0.2, 0.5, 0.2, 1),  # Darker green for input
            foreground_color=(1, 1, 1, 1),  # White text
            padding=(10, 10)
        )

        # Botão de calcular
        calcular_button = Button(text='Calcular', size_hint_y=None, height=50)
        calcular_button.bind(on_press=self.calcular_economia_combustivel)
        self.style_button(calcular_button)

        # Adiciona widgets ao layout
        layout.add_widget(self.vehicle_spinner)
        layout.add_widget(self.fuel_spinner)
        layout.add_widget(self.distance_input)
        layout.add_widget(self.fuel_input)
        layout.add_widget(calcular_button)

        return layout

    def style_button(self, button):
        with button.canvas.before:
            Color(0.5, 1, 0.5, 1)  # Light green button color
            self.rounded_rectangle = RoundedRectangle(size=button.size, pos=button.pos, radius=[20])
        button.bind(size=self.update_rect, pos=self.update_rect)

        # Add hover effect
        button.bind(on_enter=self.on_hover, on_leave=self.on_leave)

    def update_rect(self, instance, value):
        self.rounded_rectangle.pos = instance.pos
        self.rounded_rectangle.size = instance.size

    def on_hover(self, instance):
        instance.background_color = (0.7, 1, 0.7, 1)  # Lighter green on hover

    def on_leave(self, instance):
        instance.background_color = (0.5, 1,  0.5, 1)  # Reset to original color

    def calcular_economia_combustivel(self, instance):
        try:
            distancia = float(self.distance_input.text)
            combustivel = float(self.fuel_input.text)

            if combustivel <= 0:
                raise ValueError("O combustível consumido deve ser maior que zero.")

            km_por_litro = distancia / combustivel
            tipo_veiculo = self.vehicle_spinner.text
            tipo_combustivel = self.fuel_spinner.text
            self.mostrar_resultado(km_por_litro, tipo_veiculo, tipo_combustivel)

        except ValueError as e:
            self.mostrar_erro(str(e))

    def mostrar_resultado(self, km_por_litro, tipo_veiculo, tipo_combustivel):
        content = BoxLayout(orientation='vertical', padding=10)
        resultado_label = Label(
            text=f'Economia de Combustível: {km_por_litro:.2f} km/L\nTipo de Veículo: {tipo_veiculo}\nTipo de Combustível: {tipo_combustivel}',
            font_size=24,
            color=(0.9, 1, 0.9, 1)  # Light green text
        )
        fechar_button = Button(text='Fechar', size_hint_y=None, height=40)
        self.style_button(fechar_button)

        content.add_widget(resultado_label)
        content.add_widget(fechar_button)

        popup = Popup(title='Resultado', content=content, size_hint=(0.6, 0.4))
        fechar_button.bind(on_press=popup.dismiss)
        popup.open()

    def mostrar_erro(self, mensagem):
        content = BoxLayout(orientation='vertical', padding=10)
        erro_label = Label(text=mensagem, color=(1, 0, 0, 1), font_size=24)
        fechar_button = Button(text='Fechar', size_hint_y=None, height=40)
        self.style_button(fechar_button)

        content.add_widget(erro_label)
        content.add_widget(fechar_button)

        popup = Popup(title='Erro', content=content, size_hint=(0.6, 0.4))
        fechar_button.bind(on_press=popup.dismiss)
        popup.open()

if __name__ == '__main__':
    CalculadoraEconomiaCombustivelApp().run()