from models import *
from view import *
from datetime import datetime

class UI():
    def start(self):
        while True:
            print('''
            [1] -> Criar conta
            [2] -> Desativar conta
            [3] -> Transferir dinheiro
            [4] -> Movimentar dinheiro
            [5] -> Saldo total contas
            [6] -> Filtrar histórico
            [7] -> Gráfico bancos ativos
                  ''')
            
            escolha = int(input('Escolha uma das opções acima: '))

            if escolha == 1:
                self._criar_conta()
            elif escolha == 2:
                self._desativar_conta()
            elif escolha == 3:
                self._transferir_saldo()
            elif escolha == 4:
                self._movimentar_dinheiro()
            elif escolha == 5:
                self._total_contas()
            elif escolha == 6:
                self._filtrar_movimentacoes()
            elif escolha == 7:
                self._criar_grafico()
            else:
                break

    def _criar_conta(self):
        print('Digite o nome de algum dos bancos abaixo:')

        for banco in Bancos:
            print(f'---{banco.value}---')
        
        banco = input('Banco: ').title()
        valor = float(input('Saldo na conta: '))

        conta = Conta(saldo=valor, banco=Bancos(banco))
        criar_conta(conta)

    def _desativar_conta(self):
        print('Escolha entre as contas possíveis de desativar:')

        for conta in listar_contas():
            if conta.saldo == 0:
                print(f'{conta.id} -> {conta.banco.value} -> R$ {conta.saldo}')

        id_conta = int(input('Conta id: '))

        try:
            desativar_conta(id_conta)
            print('Conta desativada com sucesso.')
        except ValueError:
            print('Essa conta ainda possui saldo, faça uma transferência')

    def _transferir_saldo(self):
        print('Escolha a conta para retirar o dinheiro.')

        for conta in listar_contas():
            print(f'{conta.id} -> {conta.banco.value} -> R$ {conta.saldo}')

        conta_retirar_id = int(input('Conta id: '))

        print('Escolha a conta para enviar dinheiro.')

        for conta in listar_contas():
            if conta.id != conta_retirar_id:
                print(f'{conta.id} -> {conta.banco.value} -> R$ {conta.saldo}')

        conta_enviar_id = int(input('Conta id: '))

        valor = float(input('Digite o valor para transferir: '))
        transferir_saldo(conta_retirar_id, conta_enviar_id, valor)
    
    def _movimentar_dinheiro(self):
        print('Escolha a conta:')

        for conta in listar_contas():
            print(f'{conta.id} -> {conta.banco.value} -> R$ {conta.saldo}')

        conta_id = int(input('Conta id: '))

        valor = float(input('Digite o valor para movimentar: '))

        print('Selecione o tipo da movimentação')

        for tipo in Tipos:
            print(f'---{tipo.value}---')
        
        tipo = input().title()

        historico = Historico(conta_id = conta_id, tipo = Tipos(tipo), valor = valor, data = date.today())
        movimentar_saldo(historico)

    def _total_contas(self):
        print(f'Você possui R$ {total_saldo_contas()} somando todas as contas.')

    def _filtrar_movimentacoes(self):
        data_inicio = input('Digite a data de início: ')
        data_fim = input('Digite a data final: ')

        data_inicio = datetime.strptime(data_inicio, '%d/%m/%Y').date()
        data_fim = datetime.strptime(data_fim, '%d/%m/%Y').date()

        for i in historico_entre_datas(data_inicio, data_fim):
            print('Histórico:')
            print(f'{i.valor} - {i.tipo.value}')

    def _criar_grafico(self):
        criar_grafico_por_conta()

UI().start()
