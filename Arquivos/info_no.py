# Obtém informações básicas do seu nó
info = lnd.getinfo()

# Exibe alguns dados da informação obtida
print("Identidade do nó:", info['id'])
print("Capacidade total dos canais:", info['channels']['total_capacity'])
