from sqlalchemy import Integer, Numeric, Decimal
from sqlalchemy.orm import Mapped, mapped_column

from Database.Database import Base

class Cobranca(Base):
    __tablename__ = "cobranca"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    preco_id: Mapped[int] = mapped_column(Integer, nullable=False)
    ticket_id: Mapped[int] = mapped_column(Integer, nullable=False)
    valor_total: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)