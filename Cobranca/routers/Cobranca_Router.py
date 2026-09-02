from Database.Database import get_db
#from Cobranca.schemas.Cobranca import CobrancaResponse
from Cobranca.services.Cobranca_Service import criar_cobranca
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Ticket.models.Ticket import Ticket

router = APIRouter()

@router.post("/cobranca/criarcobranca/{placa}")
def create_cobranca(placa: str, db: Session = Depends(get_db)):
    get_ticket = db.query(Ticket).filter(Ticket.placa == placa).first()
    if not get_ticket:
        return {"message": "Ticket não encontrado."}

    criar_cobranca(get_ticket.id, db)

    return {"message": "Cobrança criada com sucesso."}