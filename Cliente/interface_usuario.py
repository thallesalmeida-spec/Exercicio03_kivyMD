from Cliente.clientemodbus import ClienteMODBUS

class InterfaceUsuario:
    """
    Classe para interação com o usuário.
    """

    def __init__(self, cliente_modbus):
        """
        Construtor
        """
        self._cliente = cliente_modbus

    def iniciar(self):
        """
        inicialização da interfaxew
        """

        self._cliente.conectar()

        try:
            while True:

                self._mostrar_menu()

                opcao = input("Escolha uma opção: ")
                # switch em python? mudar dps
                if opcao == '1':
                    self._ler_registrador()

                elif opcao == '2':
                    self._escrever_registrador()

                elif opcao == '3':
                    self._escrever_float()

                elif opcao == '4':
                    self._ler_float()

                elif opcao == '5':
                    self._ler_bits()

                elif opcao == '6':
                    self._alterar_bit()

                elif opcao == '0':
                    print("Encerrando aplicação")
                    break

                else:
                    print("Opção inválida")

        except Exception as e:
            print(f"Erro: {e}")

        finally:
            self._cliente.desconectar()

    def _mostrar_menu(self):

        print("\n==============================")
        print("      CLIENTE MODBUS TCP")
        print("==============================")
        print("1 - Ler Holding Register")
        print("2 - Escrever Holding Register")
        print("3 - Escrever Float")
        print("4 - Ler Float")
        print("5 - Ler Bits de Registrador")
        print("6 - Alterar Bit Individual")
        print("0 - Sair")
        print("==============================")

    def _ler_registrador(self):
        endereco = int(input("Endereço do registrador: "))
        valor = self._cliente.ler_holding_register(endereco)
        print(f"Valor lido: {valor}")

    def _escrever_registrador(self):
        endereco = int(input("Endereço do registrador: "))
        valor = int(input("Valor inteiro: "))
        ok = self._cliente.escrever_holding_register(endereco,valor)

        if ok:
            print("Escrita realizada.")
        else:
            print("Falha na escrita.")

    def _escrever_float(self):
        endereco = int(
            input("Endereço inicial dos 2 registradores: ")
        )
        valor = float(
            input("Valor float: ")
        )
        ok = self._cliente.escrever_float(endereco,valor)

        if ok:
            print("Float escrito com sucesso.")
        else:
            print("Erro ao escrever.")

    def _ler_float(self):

        endereco = int(input("Endereço inicial dos 2 registradores: "))
        valor = self._cliente.ler_float(endereco)
        print(f"Float lido: {valor}")

    def _ler_bits(self):
        endereco = int(input("Endereço do registrador: "))
        bits = self._cliente.ler_bits_registrador(endereco)
        print("\nEstado dos bits:")

        for i, bit in enumerate(bits):

            print(
                f"Bit {15-i}: {bit}"
            )

    def _alterar_bit(self):
        endereco = int(
            input("Endereço do registrador: ")
        )
        bit = int(
            input("Número do bit [0-15]: ")
        )
        valor = int(
            input("Novo estado (0 ou 1): ")
        )
        ok = self._cliente.escrever_bit_individual(endereco,bit,valor)
        if ok:
            print("Bit alterado com sucesso.")
        else:
            print("Falha na alteração.")


if __name__ == '__main__':

    cliente = ClienteMODBUS(
        'localhost',
        502
    )

    interface = InterfaceUsuario(
        cliente
    )

    interface.iniciar()