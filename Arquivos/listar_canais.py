# Obtém uma lista de todos os seus canais de pagamento ativos
channels = lnd.listchannels(active=True)

# Exibe algumas informações sobre cada canal
for channel in channels:
  print("Capacidade do canal:", channel['capacity'])
  print("ID do nó remoto:", channel['remote']['pub_key'])
