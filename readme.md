Aplicação desktop de calculadora básica desenvolvida em **Python** utilizando a biblioteca **Tkinter**. Este projeto permite realizar as quatro operações matemáticas fundamentais por meio de uma interface gráfica intuitiva.

##  Funcionalidades

* **Operações Matemáticas**: Suporte para Adição (`+`), Subtração (`-`), Multiplicação (`*`) e Divisão (`/`).
* **Interface Gráfica**: Utiliza campos de entrada (*Entry*) e um menu suspenso (*OptionMenu*) para seleção de operadores.
* **Tratamento de Erros**: 
    * Prevenção de erro por divisão por zero.
    * Validação de entrada de dados para evitar falhas ao digitar caracteres não numéricos.
* **Feedback Visual**: Exibe mensagens de erro em vermelho para facilitar a identificação de problemas pelo usuário.

##  Tecnologias Utilizadas

* **Python 3.14.3**.
* **Tkinter**: Biblioteca padrão do Python para criação de interfaces gráficas.

##  Pré-requisitos

Não é necessário instalar bibliotecas externas, pois o `tkinter` já vem integrado na instalação padrão do Python na maioria dos sistemas operacionais.

##  Como Executar

1.  Certifique-se de ter o Python instalado em sua máquina.
2.  Salve o código em um arquivo chamado `app.py`.
3.  Abra o terminal ou prompt de comando no diretório do arquivo.
4.  Execute o comando:
    ```bash
    python app.py
    ```

##  Como Usar

1.  **Entrada 1**: Digite o primeiro número no campo superior.
2.  **Operação**: Selecione o operador desejado no menu suspenso.
3.  **Entrada 2**: Digite o segundo número no campo inferior.
4.  **Cálculo**: Clique no botão **"Calcular"**.
5.  **Resultado**: O valor processado (ou uma mensagem de erro) aparecerá no rótulo inferior.

## Objetivo

Aprender as funções básicas da biblioteca.