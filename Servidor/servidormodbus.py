# servidor/servidor_modbus.py

from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
import random

class ServidorModbus:

    def __init__(self, host='localhost', porta=502):

        self._db = DataBank()

        self._server = ModbusServer(host=host,port=porta,no_block=True,data_bank=self._db)

    def iniciar(self):

        self._server.start()

        print("Servidor MODBUS iniciado.")

        self._inicializar_registradores()

        while True:

            self._atualizar_dados()
            self._mostrar_estado()

            sleep(1)

    def _inicializar_registradores(self):

        self._db.set_holding_registers(1000,[400])

        self._db.set_holding_registers(1001,[0,0])
        self._db.set_holding_registers(1010,[0b1010101010101010])

    def _atualizar_dados(self):

        valor = random.randint(380,420)
        self._db.set_holding_registers(1000,[valor])

    def _mostrar_estado(self):
        print(self._db.get_holding_registers(1000))

if __name__ == '__main__':
    servidor = ServidorModbus()
    servidor.iniciar()