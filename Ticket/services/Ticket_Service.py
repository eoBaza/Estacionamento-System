from Ticket.models.Ticket import Ticket
from Database.Database import get_db as db
import random


def criar_ticket(placa, db):
    codigo = codigoticket_random()
    ticket = Ticket(placa=placa, codigo_ticket=codigo)
    db.add(ticket)
    db.commit()
    return ticket

def codigoticket_random():
    tamanho = 13
    digitos = "0123456789"
    return ''.join(random.choice(digitos) for _ in range(tamanho))
   
