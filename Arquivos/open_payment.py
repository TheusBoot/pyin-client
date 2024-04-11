# Define o ID do nó remoto com quem deseja abrir o canal
pub_key = "02..."  # Chave pública do nó remoto

# Define a capacidade inicial do canal em satoshis
local_amount = 100000

# Abre um canal de pagamento com o nó remoto
lnd.openchannel(pub_key, local_amount)

# A abertura de canais pode levar algum tempo. 
# É necessário monitorar o processo para verificar o sucesso.

print("Solicitando abertura de canal...")
