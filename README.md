# Cliente Modbus TCP com Interface KivyMD

Este projeto consiste em uma aplicação de supervisório industrial simplificado utilizando o protocolo Modbus TCP. A lógica de comunicação foi baseada no repositório referente à **Atividade 2**, sendo agora integrada a uma interface gráfica moderna utilizando a biblioteca **KivyMD**.

## Tecnologias Utilizadas

*   **Python 3.x**
*   **Kivy / KivyMD**: Para a interface gráfica.
*   **Pymodbus**: Para a comunicação Modbus TCP.
*   **PyModbusTCP**: Utilizado no simulador de servidor.

## Estrutura do Projeto

*   `Cliente/`: Contém a lógica do cliente Modbus e a interface gráfica.
    *   `clientemodbus.py`: Classe responsável pela comunicação.
    *   `interface_usuario.py`: Aplicação gráfica (KivyMD).
    *   `Basic.kv`: Definição do layout da interface.
*   `Servidor/`: Simulador de servidor Modbus para testes.

## Como Executar

### 1. Instalação das Dependências

```bash
pip install -r requirements.txt
```

### 2. Executar o Servidor (Simulador)

Para testar a aplicação, primeiro inicie o servidor que simula um equipamento industrial:

```bash
python Servidor/servidormodbus.py
```

### 3. Executar o Cliente (Interface Gráfica)

Em outro terminal, execute a interface gráfica. Na raiz do projeto execute:

```bash
python -m Cliente.interface_usuario
```

## Funcionalidades da Interface

*   **Conexão**: Configuração de IP e Porta do servidor.
*   **Tipos de Dados**: Suporte para Holding Registers, Floats, Bits individuais e Coils.
*   **Escrita e Leitura**: Campos dedicados para endereços, valores e bits específicos.
*   **Leitura Recorrente**: Opção de atualizar os dados automaticamente a cada segundo utilizando o `Clock` do Kivy.
