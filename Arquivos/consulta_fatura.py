# Supondo que você tenha o ID da fatura
payment_hash = "sua_chave_de_pagamento"

# Verifica o estado da fatura pelo ID (payment_hash)
payment_info = lnd.paymenthash(payment_hash)

print("Estado da fatura:")
print("Status:", payment_info['status'])

# Verifica se a fatura foi paga
if payment_info['status'] == 'paid':
  print("Fatura paga!")
  print("Valor pago:", payment_info['amount_paid'])
