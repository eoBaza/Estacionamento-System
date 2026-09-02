# Como funciona o fluxo da API

## 1. Models → representa o banco de dados

A pasta `models/` representa as tabelas e objetos do banco de dados através do SQLAlchemy.

```text
models/
└── ticket.py
        ↓
Representa o Ticket no banco de dados
```

O `Ticket` conhece os **dados do Ticket** e comportamentos que pertencem naturalmente ao próprio Ticket do banco.

Exemplo:

```python
class Ticket(Base):
    __tablename__ = "ticket"

    id: Mapped[int]
    placa: Mapped[str]
    codigo_ticket: Mapped[str]
    dt_entrada: Mapped[datetime]
    dt_saida: Mapped[datetime | None]

    def is_open(self):
        return self.dt_saida is None

    def close_ticket(self):
        self.dt_saida = datetime.now()
```

---

# 2. Schemas → contrato da API

A pasta `schemas/` representa os dados que **entram e saem da API**.

```text
schemas/
└── ticket.py
        ↓
Define o contrato da API
```

Podemos ter vários schemas para o mesmo Model.

### TicketCreate

```text
TicketCreate
      ↓
dados necessários para CRIAR um Ticket
```

### TicketResponse

```text
TicketResponse
      ↓
dados DEVOLVIDOS pela API
```

### TicketUpdate

```text
TicketUpdate
      ↓
dados permitidos para ALTERAR um Ticket
```

IMPORTANTE:

```text
MODEL
  ↓
representa o BANCO

SCHEMA
  ↓
representa o CONTRATO DA API
```

Um não precisa ser igual ao outro.

---

# 3. Services → regras do sistema

A pasta `services/` contém as **regras de negócio** do sistema.

```text
services/
└── ticket_service.py
        ↓
Regras relacionadas ao estacionamento
```

Por exemplo:

```python
def criar_ticket(...):
    # regras para criar um ticket
```

```python
def fechar_ticket(...):
    # regras para fechar um ticket
```

```python
def calcular_valor(...):
    # calcula quanto o cliente deve pagar
```

O Service responde principalmente à pergunta:

> "O que o sistema deve fazer?"

---

# 4. Utils → ferramentas auxiliares

A pasta `utils/` contém funções/classes auxiliares que não representam diretamente uma regra do negócio.

No nosso caso:

```text
utils/
└── ticket_formatter.py
        ↓
Formatação / impressão do Ticket
```

O `TicketFormatter` pega um Ticket e transforma seus dados em algo adequado para apresentação.

Por exemplo:

```text
Ticket vindo do banco:

placa = "ABC1234"
codigo_ticket = "TK20260901001"
dt_entrada = 2026-09-01 15:10:00
```

O Formatter transforma isso em:

```text
================================
        SEJA BEM-VINDO
================================

Data: 01/09/2026
Hora: 15:10

Placa: ABC1234
Código: TK20260901001

================================
```

---

# 5. Onde fica o FORMAT_DATA?

A data armazenada no banco deve continuar sendo um objeto `datetime`.

Exemplo:

```python
ticket.dt_entrada
```

Pode conter:

```text
2026-09-01 15:10:00
```

Nós **não alteramos o dado do banco** para transformá-lo em:

```text
01/09/2026
```

Apenas formatamos para apresentação.

Por isso:

```python
data = ticket.dt_entrada.strftime("%d/%m/%Y")
```

fica no `TicketFormatter`.

Exemplo:

```python
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
Hora: {horario}

Placa: {ticket.placa}
Código: {ticket.codigo_ticket}

================================
"""
```

O Formatter **não modifica o Ticket**.

Ele apenas pega:

```text
Ticket
  ↓
lê os dados
  ↓
formata
  ↓
retorna uma representação em texto
```

---

# 6. Fluxo completo

Podemos imaginar o sistema dessa maneira:

```text
                    CLIENTE
                       ↓
                 FastAPI / Router
                       ↓
                    Service
                       ↓
                    Ticket
                       ↓
                  PostgreSQL
                       ↓
                    Ticket
                       ↓
               TicketFormatter
                       ↓
              Texto formatado
```

Ou, de forma mais simples:

```text
Router
  ↓
Service
  ↓
Model
  ↓
Banco de dados
```

E quando precisamos apresentar/imprimir:

```text
Model
  ↓
TicketFormatter
  ↓
Texto para impressão
```

---

# 7. Responsabilidade de cada pasta

Uma forma fácil de lembrar:

```text
models/
    ↓
"O que é esse objeto?"

schemas/
    ↓
"Quais dados entram e saem da API?"

services/
    ↓
"O que o sistema deve fazer?"

utils/
    ↓
"Como vou auxiliar/formata/apresentar esses dados?"

routers/
    ↓
"Qual URL o cliente chama?"
```

### Exemplo real

Quando alguém cria um Ticket:

```text
POST /tickets
       ↓
Router recebe a requisição
       ↓
Schema valida os dados
       ↓
Service executa as regras
       ↓
Model representa o Ticket
       ↓
SQLAlchemy salva no PostgreSQL
       ↓
SchemaResponse devolve os dados
```

Quando alguém quer imprimir:

```text
GET /tickets/1/imprimir
       ↓
Router recebe a requisição
       ↓
Service busca o Ticket
       ↓
Ticket é recuperado
       ↓
TicketFormatter formata
       ↓
"SEJA BEM-VINDO
 Data: 01/09/2026
 Hora: 15:10
 Placa: ABC1234
 Código: TK20260901001"
```

---

# Regra mental para lembrar

```text
MODEL
↓
Dado / objeto do banco

SCHEMA
↓
Contrato da API

SERVICE
↓
Regra de negócio

UTIL
↓
Auxiliar / formatação

ROUTER
↓
Entrada e saída HTTP
```

Não é uma regra absoluta para todo projeto, mas é uma ótima divisão inicial para organizar nosso projeto de estacionamento enquanto estamos aprendendo FastAPI.
