from Database.Database import get_db
from sqlalchemy import text
from sqlalchemy.orm import Session



def criar_cobranca(ticket_id: int, db: Session):
    db.execute(
    text("""SELECT estacionamento.calc_valorestacionamento_fnc(:ticket_id) """), {"ticket_id": ticket_id} )
    # Funciona, mas não é a melhor prática
    # db.execute(text(f"SELECT estacionamento.calc_valorestacionamento_fnc({ticket_id})"))
    db.commit()
