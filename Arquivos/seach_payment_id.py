

"A função getpayment permite obter informações sobre um pagamento específico usando seu ID."

# Supondo que você tenha o ID do pagamento
payment_hash = "seu_id_de_pagamento"

# Obtém informações sobre o pagamento
payment_info = lnd.getpayment(payment_hash)

# Exibe os detalhes do pagamento
print("Pagamento:", payment_hash)
print("Valor:", payment_info['amount'])
print("Descrição:", payment_info['description'])
print("Status:", payment_info['status'])
