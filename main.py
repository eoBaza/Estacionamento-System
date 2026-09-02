from fastapi import FastAPI

# ROTAS
from Ticket.routers.Ticket_Router import router as TicketRouter
from Cobranca.routers.Cobranca_Router import router as CobrancaRouter
from Pagamentos.routers.PagamentosPendentes_Router import router as PagamentosPendentes_Router

app = FastAPI()
app.include_router(TicketRouter)
app.include_router(CobrancaRouter)
app.include_router(PagamentosPendentes_Router)