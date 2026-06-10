import os
# Configuração para evitar problemas com OpenGL no Windows
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.clock import Clock
from Cliente.clientemodbus import ClienteMODBUS

class MyWidget(MDBoxLayout):
    """
    Widget principal da interface gráfica.
    Substitui a lógica de terminal da classe InterfaceUsuario.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._cliente = None
        self._ev = None

    def conectar(self):
        """
        Lógica para conectar ao servidor Modbus usando os campos IP e Porta.
        """
        try:
            host = self.ids.txt_ip_servidor.text
            porta = int(self.ids.txt_porta.text)
            self._cliente = ClienteMODBUS(host, porta)
            if self._cliente.conectar():
                self.ids.lbl_resultado.text = "Conectado com sucesso!"
            else:
                self.ids.lbl_resultado.text = "Falha na conexão."
        except Exception as e:
            self.ids.lbl_resultado.text = f"Erro na conexão: {e}"

    def ler(self):
        """
        Lógica para ler dados do servidor dependendo da checkbox ativa.
        """
        if not self._cliente:
            self.ids.lbl_resultado.text = "Conecte ao servidor primeiro!"
            return

        try:
            endereco = int(self.ids.txt_endereco.text)
            
            if self.ids.chk_register.active:
                valor = self._cliente.ler_holding_register(endereco)
            elif self.ids.chk_float.active:
                valor = self._cliente.ler_float(endereco)
            elif self.ids.chk_bits.active:
                valor = self._cliente.ler_bits_registrador(endereco)
            elif self.ids.chk_coil.active:
                valor = self._cliente.ler_coil(endereco)
            else:
                self.ids.lbl_resultado.text = "Selecione o tipo de dado."
                return
            
            self.ids.lbl_resultado.text = f"Valor lido: {valor}"
        except Exception as e:
            self.ids.lbl_resultado.text = f"Erro na leitura: {e}"

    def escrever(self):
        """
        Lógica para escrever dados no servidor dependendo da checkbox ativa.
        """
        if not self._cliente:
            self.ids.lbl_resultado.text = "Conecte ao servidor primeiro!"
            return

        try:
            endereco = int(self.ids.txt_endereco.text)
            valor_str = self.ids.txt_valor.text
            
            ok = False
            if self.ids.chk_register.active:
                ok = self._cliente.escrever_holding_register(endereco, int(valor_str))
            elif self.ids.chk_float.active:
                ok = self._cliente.escrever_float(endereco, float(valor_str))
            elif self.ids.chk_bits.active:
                bit = int(self.ids.txt_bit.text)
                ok = self._cliente.escrever_bit_individual(endereco, bit, int(valor_str))
            elif self.ids.chk_coil.active:
                ok = self._cliente.escrever_coil(endereco, int(valor_str))
            else:
                self.ids.lbl_resultado.text = "Selecione o tipo de dado."
                return
            
            if ok:
                self.ids.lbl_resultado.text = "Escrita realizada com sucesso!"
            else:
                self.ids.lbl_resultado.text = "Falha na escrita."
        except Exception as e:
            self.ids.lbl_resultado.text = f"Erro na escrita: {e}"

    def toggle_recorrente(self, active):
        """
        Ativa ou desativa a leitura recorrente usando Clock.
        """
        if active:
            self._ev = Clock.schedule_interval(lambda dt: self.ler(), 1)
        else:
            if self._ev:
                self._ev.cancel()

class BasicApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"
        return MyWidget()

if __name__ == '__main__':
    BasicApp().run()
