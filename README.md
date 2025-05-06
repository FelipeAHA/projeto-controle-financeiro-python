# Projeto de Controle Financeiro em Python

Este é um projeto simples de controle financeiro desenvolvido em Python usando a biblioteca SQLModel para interagir com um banco de dados SQLite. Ele permite aos usuários gerenciar contas bancárias, registrar movimentações financeiras e visualizar o saldo total e o histórico de transações.

## Funcionalidades

* **Criação de Conta:** Permite criar novas contas bancárias, especificando o banco e o saldo inicial.
* **Desativação de Conta:** Permite desativar contas, desde que o saldo seja zero.
* **Transferência de Saldo:** Permite transferir saldo entre contas existentes.
* **Movimentação de Dinheiro:** Permite registrar entradas e saídas de dinheiro nas contas.
* **Saldo Total das Contas:** Calcula e exibe o saldo total de todas as contas.
* **Filtragem de Histórico:** Permite filtrar o histórico de movimentações por período.
* **Geração de Gráfico:** Gera um gráfico de barras mostrando o saldo das contas ativas por banco.

## Tecnologias Utilizadas

* **Python:** Linguagem de programação principal.
* **SQLModel:** ORM (Object-Relational Mapper) para interagir com o banco de dados SQLite.
* **SQLite:** Banco de dados utilizado para armazenar os dados.
* **Enum:** Módulo do Python para criar enumerações para Bancos, Status e Tipos de transação.
* **datetime:** Módulo para trabalhar com datas.
* **matplotlib:** Biblioteca para geração de gráficos (usada na função de gráfico de bancos ativos).

## Estrutura do Projeto

O projeto está organizado nos seguintes arquivos:

* **`models.py`:** Define os modelos de dados (`Conta`, `Historico`) usando SQLModel, as enumerações (`Bancos`, `Status`, `Tipos`) e configura a conexão com o banco de dados SQLite.
* **`view.py`:** Contém as funções que executam as operações no banco de dados (CRUD - Create, Read, Update, Delete), como criar conta, listar contas, transferir saldo, movimentar dinheiro, etc.
* **`templates.py`:** Implementa a interface do usuário (UI) no terminal, apresentando o menu de opções e interagindo com o usuário para coletar os dados e exibir os resultados.

## Como Executar

1.  **Instalar as dependências:**
    
    ```bash
    pip install sqlmodel matplotlib
    ```
    
2.  **Executar o script `templates.py`:**
    
    ```bash
    python templates.py
    ```
    
3.  O menu principal será exibido no terminal, e você poderá interagir com o sistema.

## Entidades do Sistema

* **Conta:** Representa uma conta bancária, com atributos como saldo, banco e status (ativa/inativa).
* **Histórico:** Registra as movimentações financeiras, associando a transação a uma conta, tipo (entrada/saída), valor e data.

## Enumerações

* **Bancos:** Lista os bancos suportados (Nubank, Santander, Inter, Bradesco, Banco do Brasil, Caixa Econômica).
* **Status:** Indica o status da conta (Ativo, Inativo).
* **Tipos:** Define o tipo de movimentação (Saída, Entrada).

## Observações

* O banco de dados é um arquivo SQLite local (`database.db`).
* A interface do usuário é baseada em texto no terminal.
* A biblioteca `matplotlib` é utilizada para gerar um gráfico simples de barras.
* Há tratamento básico de erros, como verificar saldo insuficiente e existência de conta.
