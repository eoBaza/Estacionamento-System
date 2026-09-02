from Estacionamento.Database.Database import Database

db = Database()

print(db.connect())
print(db.execute_query("select placa, codigo_ticket, dt_entrada from ticket"))