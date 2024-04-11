import random

# Gera um valor aleatório para a fatura em satoshis
amount = random.randint(1000, 100000)

# Cria uma fatura com descrição e valor
description = "Pagamento de teste"
invoice = lnd.invoice(amount, description)

# Exibe os detalhes da fatura
print("Fatura criada:")
print("Valor:", invoice['amount'])
print("Descrição:", invoice['description'])
print("Chave da fatura (bolt11):", invoice['payment_request'])
