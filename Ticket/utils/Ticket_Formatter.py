from Estacionamento.Ticket.models.Ticket import Ticket


class TicketFormatter:

    @staticmethod
    def imprimir_ticket(ticket: Ticket) -> str:
        
        data = ticket.dt_entrada.strftime("%d/%m/%Y")
        horario = ticket.dt_entrada.strftime("%H:%M")
        
        return f"""
            ================================
                    SEJA BEM-VINDO
            ================================

            Data: {data}
            Hora de entrada: {horario}

            Placa: {ticket.placa}
            Código: {ticket.codigo_ticket}

            ================================
        """