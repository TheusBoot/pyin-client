# Supondo que você tenha a chave de pagamento (bolt11) do destino
payment_request = "lnbc..."

# Define o valor do pagamento em satoshis
amount = 50000

# Envia o pagamento ao destino
payment = lnd.sendpayment(payment_request, amount)

# Verifica se o pagamento foi bem sucedido
if payment['status'] == 'SUCCEEDED':
  print("Pagamento enviado com sucesso!")
  print("ID da transação:", payment['payment_hash'])
else:
  print("Erro ao enviar pagamento:", payment['status'])
