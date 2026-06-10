# exemplos/exemplo_float.py

# from cliente.cliente_modbus import ClienteModbus
from Cliente.clientemodbus import ClienteMODBUS

cliente = ClienteMODBUS(host='localhost',porta=502)
cliente.conectar()

try:
    endereco = 1001
    valor_escrito = 37.85

    print("====== TESTE FLOAT ======")

    print(
        f"Escrevendo {valor_escrito} "
        f"nos registradores "
        f"{endereco}-{endereco+1}"
    )

    ok = cliente.escrever_float(
        endereco,
        valor_escrito
    )

    if ok:
        valor_lido = cliente.ler_float(
            endereco
        )

        print(
            f"Valor lido: {valor_lido}"
        )

    else:
        print("Falha na escrita.")

finally:
    cliente.desconectar()