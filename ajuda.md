Futuramente vou prcisar de varios schemas para o mesmo objeto, pois MODELS/ ... representa o BANCAO DE DADOS enquanto o schemas/... Representa o contrato da API
        ( EXEMPLO )
                TicketCreate
                    ↓
                dados necessários para CRIAR

                TicketResponse
                    ↓
                dados devolvidos pela API

                TicketUpdate
                    ↓
                dados permitidos para ALTERAR

Para melhores organizacoes, devemos criar as pastas services e utils, porque ? Por ser algo utilizando POO, nao exatamente segue as mesmas regras de uma Programacao Oriental, ou seja os metodos nao vao estar na classe, pois a classe representa objetos. POIS ISSO E UMA MANDEIRA DO ORM 

        ( EXEMPLO )
                models/
                    ticket.py
                        ↓
                    representa o Ticket (objeto do banco )

                services/
                    ticket_service.py
                        ↓
                    regras do estacionamento 

                utils/
                    ticket_formatter.py
                        ↓
                    formatação/impressão