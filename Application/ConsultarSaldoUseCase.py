from Domain.interfaces.IContaRepository import IContaRepository
from isNullOrEmpty.is_null_or_empty import is_null_or_empty

class ConsultarSaldoUseCase:
    def __init__(self, contas_repository: IContaRepository):
        self.contas_repository = contas_repository
    def execute(self, id_contas):
        if is_null_or_empty(id_contas):
            raise ValueError("O ID da conta não pode ser nulo ou vazio.")
        conta = self.contas_repository.read(id_contas)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        return conta.saldo_conta