from pyln.client import LightningRpc

# Conecta ao lightningd rodando no path padrão (/tmp/lightning/lightning-rpc)
lnd = LightningRpc()

# Verifica se a conexão foi bem sucedida
if not lnd.is_connected():
  print("Erro: Falha ao conectar ao lightningd")
  exit()

print("Conectado ao lightningd com sucesso!")
