from datetime import datetime
from pydantic import BaseModel


class PagamentosConfirmadosResponse(BaseModel):
    ticket_id: int
    placa: str
    codigo_ticket: str
    dt_entrada: datetime
    dt_saida: datetime
    valor_total: float
    situacao: bool

    model_config = {
        "from_attributes": True
    }