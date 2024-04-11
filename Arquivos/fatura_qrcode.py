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

# Importe a biblioteca QR escolhida
import qrcode  # Exemplo com qrcode

# Crie o objeto QR Code
qr = qrcode.QRCode(
    version=1,  # Nível de versão do QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nível de correção de erros
    box_size=10,  # Tamanho do módulo QR Code
    border=4,  # Largura da borda
)

# Adicione a chave da fatura ao QR Code
qr.add_data(invoice['payment_request'])

# Gere a imagem QR Code
qr.make(file="fatura.png")  # Nome do arquivo de imagem
