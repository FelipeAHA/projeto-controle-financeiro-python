from sqlmodel import SQLModel, Field, create_engine, Relationship
from enum import Enum
from datetime import date

class Bancos(Enum):
    NUBANK = 'Nubank'
    SANTANTER = 'Santander'
    INTER = 'Inter'
    BRADESCO = 'Bradesco'
    BANCO_DO_BRASIL = 'Banco Do Brasil'
    CAIXA_ECONOMICA = 'Caixa Economica'

class Status(Enum):
    ATIVO = 'Ativo'
    INATIV0 = 'Inativo'

class Tipos(Enum):
    SAIDA = 'Saida'
    ENTRADA = 'Entrada'

class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    saldo: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key='conta.id')
    conta: Conta = Relationship()
    tipo: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date

sqlite_file_name = 'database.db'
sqlite_url = f'sqlite:///{sqlite_file_name}'

engine = create_engine(sqlite_url, echo=False)

if __name__ == '__main__':
    SQLModel.metadata.create_all(engine)