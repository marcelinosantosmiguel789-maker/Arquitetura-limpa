from fastapi import FastAPI
from Adapters.Repository.ContasRepository import ContasRepository
from Application.ConsultarSaldoUseCase import ConsultarSaldoUseCase
from Domain.Entities.ContaEntitie import Conta
from infraestructure.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="API de Contas", description="API para gerenciar contas bancárias", version="1.0.0")

contas_repository = ContasRepository()
conta_use_case = ConsultarSaldoUseCase(contas_repository)

@app.post("/contas")
def criar_conta(id_conta: str, nome_conta: str, saldo_conta: float):
    try:
        conta = Conta(id_conta, nome_conta, saldo_conta)
        contas_repository.create(conta)
        logger.info(f"Conta criada com sucesso: {conta.__dict__}")
        return {"message": "Conta criada com sucesso."}
    except ValueError as e:
        logger.error(f"Erro ao criar conta: {str(e)}")
        return {"error": str(e)}
@app.get("/contas/{id_conta}")
def consultar_saldo(id_conta: str):
    try:
        saldo = conta_use_case.execute(id_conta)
        logger.info(f"Saldo consultado com sucesso para a conta {id_conta}: {saldo}")
        return {"saldo": saldo}
    except ValueError as e:
        logger.error(f"Erro ao consultar saldo: {str(e)}")
        return {"error": str(e)}
@app.on_event("shutdown")
def shutdown_event():
    logger.info("Aplicação encerrada.")