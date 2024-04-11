from pyln.client import LightningRpc

# Conecta ao lightningd
lnd = LightningRpc()

# Define a função callback para pagamentos recebidos
def payment_received(payment):
    print("Pagamento recebido!")
    print("Valor:", payment['amount'])
    print("Descrição:", payment['description'])

# Registra a função callback para pagamentos recebidos
lnd.subscribe_payments(payment_received)

# Aguarda a recepção de novos pagamentos
print("Aguardando pagamentos...")
