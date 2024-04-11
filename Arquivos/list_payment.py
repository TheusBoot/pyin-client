# Obtém uma lista de pagamentos recebidos
payments = lnd.listpayments()

# Exibe os detalhes de cada pagamento
for payment in payments:
    print("Pagamento:")
    print("Valor:", payment['amount'])
    print("Descrição:", payment['description'])
    print("Data:", payment['created_at'])
