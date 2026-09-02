from Ticket.schemas.Ticket import TicketResponse
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from Database.Database import get_db
from Ticket.models.Ticket import Ticket
from Ticket.services.Ticket_Service import criar_ticket

router = APIRouter()

@router.get("/tickets", response_model=list[TicketResponse])
def ticket_list(db:Session =Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets

@router.post("/tickets/createticket/{placa}", response_model=TicketResponse)
def create_ticket(placa: str, db: Session = Depends(get_db)):
    ticket = criar_ticket(placa, db)
    return ticket