from datetime import datetime
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from Database.Database import Base

# Reprensentação do modelo de dados da tabela Ticket MODELO ORM
class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    placa: Mapped[str] = mapped_column(String(255), nullable=False)
    codigo_ticket: Mapped[str] = mapped_column(String(13), nullable=False)
    dt_entrada: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now)
    dt_saida: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    def is_open(self) -> bool:
        return self.dt_saida is None

    def close_ticket(self):
        self.dt_saida = datetime.now()
    
# Representação do modelo de dados do Ticket para resposta da API
# class VeiculoResponse(BaseModel):
#     placa: str
#     codigo_ticket: str
#     dt_entrada: datetime