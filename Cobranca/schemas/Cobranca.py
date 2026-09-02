from pydantic import BaseModel

class CobrancaCreate(BaseModel):
    ticket_id: int
    