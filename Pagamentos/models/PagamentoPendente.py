from sqlalchemy import Integer, String, Numeric,DateTime, Boolean
from decimal import Decimal
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

from Database.Database import Base

class PagamentoPendente(Base):
    __tablename__ = "vw_pagamentos_pendentes"

    ticket_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    placa: Mapped[str] = mapped_column(String(255), nullable=False)
    codigo_ticket: Mapped[str] = mapped_column(String(13), nullable=False)
    dt_entrada: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    dt_saida: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    valor_total: Mapped[Decimal] = mapped_column(Numeric(6, 2), nullable=False)
    situacao: Mapped[bool] = mapped_column(Boolean, nullable=False)