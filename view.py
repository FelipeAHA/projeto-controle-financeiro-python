from models import Conta, engine, Bancos, Status, Historico, Tipos
from sqlmodel import Session, select
from datetime import date, timedelta


def criar_conta(conta: Conta):

    with Session(engine) as conexao_db:
        statement = select(Conta).where(Conta.banco == conta.banco)
        results = conexao_db.exec(statement).all()
        
        if results:
            print('Já existe uma conta nesse banco!')
            return
        
        conexao_db.add(conta)
        conexao_db.commit()

        return conta

def listar_contas():
    with Session(engine) as conexao_db:
        statement = select(Conta)
        results = conexao_db.exec(statement).all()
        return results

def desativar_conta(id):
    with Session(engine) as conexao_db:
        statement = select(Conta).where(Conta.id == id)
        conta = conexao_db.exec(statement).first()
        if conta.saldo > 0:
            raise ValueError('Essa conta ainda possui saldo.')
        conta.status = Status.INATIV0
        conexao_db.commit()

def transferir_saldo(id_canta_destinador, id_conta_destinataria, valor):
    with Session(engine) as conexao_db:
        statement = select(Conta).where(Conta.id == id_canta_destinador)
        conta_destinador = conexao_db.exec(statement).first()

        if conta_destinador.saldo < valor:
            raise ValueError('A conta não possui saldo disponível para essa transação.')
        
        conta_destinador.saldo -= valor

        statement_2 = select(Conta).where(Conta.id == id_conta_destinataria)
        conta_destinataria = conexao_db.exec(statement_2).first()
        conta_destinataria.saldo += valor

        conexao_db.commit()

def movimentar_saldo(historico: Historico):
    with Session(engine) as conexao_db:
        statement = select(Conta).where(Conta.id == historico.conta_id)
        conta = conexao_db.exec(statement).first()

        if conta.status == Status.INATIV0:
            raise ValueError('Essa conta está inativa.')
        
        if historico.tipo == Tipos.ENTRADA:
            conta.saldo += historico.valor
        else:
            if conta.saldo < historico.valor:
                raise ValueError('A conta não possui saldo suficiente.')
            conta.saldo -= historico.valor

        conexao_db.add(historico)
        conexao_db.commit()
        return historico 

def total_saldo_contas(): 
    with Session(engine) as conexao_db:
        statement = select(Conta)
        lista_contas = conexao_db.exec(statement).all()
        
        total = 0
        for conta in lista_contas:
            total += conta.saldo
        
        return float(total) 

def historico_entre_datas(data_inicio: date, data_fim: date):
    with Session(engine) as conexao_db:
        statement = select(Historico).where(Historico.data >= data_inicio, Historico.data <= data_fim)
        resultados = conexao_db.exec(statement).all()
        return resultados

def criar_grafico_por_conta():
    with Session(engine) as conexao_db:
        statement = select(Conta).where(Conta.status == Status.ATIVO)
        contas_ativas = conexao_db.exec(statement).all()

        lista_contas_ativas = [conta.banco.value for conta in contas_ativas]
        saldos_contas_ativas = [conta.saldo for conta in contas_ativas]

        import matplotlib.pyplot as plt
        plt.bar(lista_contas_ativas, saldos_contas_ativas)
        plt.show()



# conta = Conta(saldo=710, banco=Bancos.CAIXA_ECONOMICA, status=Status.INATIV0)    
# criar_conta(conta)

# tranferir_saldo(3, 1, 5000)

# historico = Historico(conta_id=2, tipo=Tipos.ENTRADA, valor=100, data=date.today())
# movimentar_saldo(historico)

# total_saldo_contas()

# x = historico_entre_datas(date.today(), date.today())
# print(x)

# criar_grafico_por_conta()