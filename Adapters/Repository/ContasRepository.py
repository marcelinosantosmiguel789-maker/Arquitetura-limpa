from domain.entiities.ContaEntitie import Conta
from domain.interfaces.repository import IContasRepository

class ContasRepository(IContasRepository):
    def __init__(self):
        self.contas = {}

    def create(self, conta: Conta):
        self.contas[conta.id_conta] = conta

    def read(self, id_conta):
        return self.contas.get(id_conta)

    def update(self, conta: Conta):
        if conta.id_conta in self.contas:
            self.contas[conta.id_conta] = conta
        else:
            raise ValueError("Conta não encontrada.")

    def delete(self, id_conta):
        if id_conta in self.contas:
            del self.contas[id_conta]
        else:
            raise ValueError("Conta não encontrada.")