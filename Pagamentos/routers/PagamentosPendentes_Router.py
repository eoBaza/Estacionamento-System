from Database.Database import get_db
from Pagamentos.schemas.PagamentoPendente import PagamentosPendentesResponse
from Pagamentos.models.PagamentoPendente import PagamentoPendente
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

router = APIRouter()

@router.get("/cobranca/pagamentopendente/{placa}")
def verify_pagamento_pendente(placa: str, db: Session = Depends(get_db)):
    pagamento = db.query(PagamentosPendentesResponse).filter(PagamentosPendentesResponse.placa == placa).first()
    return pagamento

@router.get("/cobranca/pagamentospendentes", response_model=list[PagamentosPendentesResponse])
def Pagamentos_Pendentes_List(db:Session = Depends(get_db)):
    pagamentos = db.query(PagamentoPendente).all()
    return pagamentos