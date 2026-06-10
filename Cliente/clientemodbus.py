from pymodbus.client import ModbusTcpClient

class ClienteMODBUS():
    """
    Classe Cliente MODBUS usando pymodbus dados serao recebidos a partir da classe InterfaceUsuario
    """
    def __init__(self, host='localhost', porta = 502, device_id = 1):
        """
        Construtor
        """
        self._host = host
        self._porta = porta
        self._device_id = device_id

        self._cliente = ModbusTcpClient(host=self._host, port=self._porta)

    def conectar(self):
        return self._cliente.connect()

    def desconectar(self):
        self._cliente.close()

    def ler_holding_register(self, endereco):
        """
        Método para ler só 1 registrador
        """
        resposta = self._cliente.read_holding_registers(address = endereco, count = 1,device_id = self._device_id)

        if resposta.isError():
            return None

        return resposta.registers[0]
    
    def escrever_holding_register(self, endereco, valor):
        """
        Escreve em só 1 Registrador. Retorna True em caso de sucesso, False em caso de falha.
        """
        resposta = self._cliente.write_register(address=endereco,value=valor,device_id=self._device_id)
        return not resposta.isError()

    def escrever_float(self, endereco, valor):
        """
        Escreve float em 2 registradores consecutivos.
        """
        registradores = self._cliente.convert_to_registers(value=valor, data_type=self._cliente.DATATYPE.FLOAT32)
        resposta = self._cliente.write_registers(address=endereco,values=registradores,device_id=self._device_id)
        return not resposta.isError()

    def ler_float(self, endereco):
        """
        Método para ler float de 2 registradores consecutivos.
        """
        resposta = self._cliente.read_holding_registers(address=endereco,count=2,device_id=self._device_id)
        if resposta.isError():
            return None
        return self._cliente.convert_from_registers(registers=resposta.registers,data_type=self._cliente.DATATYPE.FLOAT32)

    def ler_bits_registrador(self, endereco):
        """
        Retorna os 16 bits de individuais de 1 registrador.
        """
        valor = self.ler_holding_register(endereco)
        if valor is None:
            return None
        
        bits = []
        for i in range(16):
            bits.append((valor >> i) & 1)

        return bits[::-1]

    def escrever_bit_individual(self,endereco,numero_bit,novo_estado):
        """
        Escreve somente um bit do registrador.
        """
        valor_atual = self.ler_holding_register(endereco)

        if valor_atual is None:
            return False

        if novo_estado == 1:

            novo_valor = (
                valor_atual |
                (1 << numero_bit)
            )

        else:
            novo_valor = (valor_atual & ~(1 << numero_bit))
        return self.escrever_holding_register(endereco, novo_valor)

    def ler_coil(self, endereco):
        """
        Lê o estado de um Coil.
        """
        resposta = self._cliente.read_coils(address=endereco, count=1, device_id=self._device_id)
        if resposta.isError():
            return None
        return resposta.bits[0]

    def escrever_coil(self, endereco, valor):
        """
        Escreve em um Coil.
        """
        resposta = self._cliente.write_coil(address=endereco, value=valor, device_id=self._device_id)
        return not resposta.isError()