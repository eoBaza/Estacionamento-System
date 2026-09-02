from datetime import datetime
from pydantic import BaseModel

# Pode existir tambem essa classe para criar o modelo de dados do Ticket para criação de um novo ticket na API
class TicketCreate(BaseModel):
    placa: str
    

class TicketResponse(BaseModel):
    id: int
    placa: str
    codigo_ticket: str
    dt_entrada: datetime
    dt_saida: datetime | None = None

    # Ponto chave pois aqui permite que o Pydantic aceite os atributos do modelo ORM como entrada para a criação do modelo de resposta SQLAlchemy ex: ticket = Ticket(...) em uma resposta de API
    model_config = {
        "from_attributes": True
    }