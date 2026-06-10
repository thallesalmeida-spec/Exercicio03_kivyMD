# exemplos/exemplo_bits.py

from Cliente.clientemodbus import ClienteMODBUS

cliente = ClienteMODBUS(host='localhost',porta=502)
cliente.conectar()

try:
    endereco = 1010
    print("====== TESTE BITS ======")
    print("\nEstado inicial:")
    bits = cliente.ler_bits_registrador(endereco)

    for i, bit in enumerate(bits):
        print(f"Bit {15-i}: {bit}")

    print("\nAlterando bit 3 para 0...")

    cliente.escrever_bit_individual(endereco,3,0)

    print("\nNovo estado:")

    bits = cliente.ler_bits_registrador(
        endereco
    )

    for i, bit in enumerate(bits):

        print(f"Bit {15-i}: {bit}")

finally:
    cliente.desconectar()