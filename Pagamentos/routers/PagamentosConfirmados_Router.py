from Database.Database import get_db
from Pagamentos.models.PagamentoConfirmado import PagamentoConfirmados
from Pagamentos.schemas.PagamentoConfirmado import PagamentosConfirmadosResponse
from Pagamentos.models.PagamentoConfirmado import PagamentoConfirmados
from Pagamentos.services.PagamentosConfirmados_Service import confirmar_pagamento
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()


@router.put("/cobranca/confirmacaopagamento/{placa}/")
def confirm_pagmento(placa: str, db: Session = Depends(get_db)):
    try:
        pagamento_confirmado = confirmar_pagamento(placa, db)
        if pagamento_confirmado:
            return {
                "message": f"Pagamento confirmado com sucesso para a placa {placa}."
            }
        else:
            return {"error": "Pagamento não foi encontrado."}
    except ValueError as e:
        return {"error": str(e)}

@router.get("/cobranca/pagamentoconfirmado", response_model=list[PagamentosConfirmadosResponse])
def pagamentoconfirmados_list(db: Session = Depends(get_db)):
    pagamentos_confirmados = db.query(PagamentoConfirmados).filter_by(situacao=True).all()
    return pagamentos_confirmados