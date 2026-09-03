from Pagamentos.schemas.PagamentoConfirmado import PagamentosConfirmadosResponse
from sqlalchemy.orm import Session
from Pagamentos.models.PagamentoPendente import PagamentoPendente
#from Pagamentos.models.PagamentoConfirmados import PagamentosConfirmados

def confirmar_pagamento(placa: str,  db: Session) -> PagamentosConfirmadosResponse:
    pagamento = db.query(PagamentoPendente).filter_by(placa=placa, situacao=False).first()
    if pagamento:
        pagamento.situacao = True
        db.commit()
        # como e uma view, não possui um ID primary key, entao nao faz sentido fazer um refresh.
        #db.refresh(pagamento)
        return pagamento
    else:
        raise ValueError("Pagamento não encontrado")