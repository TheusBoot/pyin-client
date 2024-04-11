'''
Gerando Fatura com ID de Pagamento no pyln-client
Para gerar uma fatura com ID de pagamento (bolt11) utilizando o pyln-client, siga estes passos:

1. Importe a Biblioteca:
'''

import random
from pyln.client import LightningRpc


#2. Conecte ao Lightning Daemon:
# Conecta ao lightningd rodando no path padrão (/tmp/lightning/lightning-rpc)
lnd = LightningRpc()

# Verifica se a conexão foi bem sucedida
if not lnd.is_connected():
  print("Erro: Falha ao conectar ao lightningd")
  exit()

print("Conectado ao lightningd com sucesso!")

#3. Gere a Fatura:
# Gera um valor aleatório para a fatura em satoshis
amount = random.randint(1000, 100000)

# Cria uma fatura com descrição e valor
description = "Pagamento de teste"
invoice = lnd.invoice(amount, description)

# Exibe os detalhes da fatura, incluindo o ID de pagamento (bolt11)
print("Fatura criada:")
print("Valor:", invoice['amount'])
print("Descrição:", invoice['description'])
print("ID de Pagamento (bolt11):", invoice['payment_request'])

'''
4. Utilize o ID de Pagamento:

O ID de pagamento (bolt11) da fatura (invoice['payment_request']) pode ser utilizado para:

Compartilhar com o pagador: Envie o ID de pagamento para a pessoa ou serviço que deseja que te envie o pagamento.
Exibir um QR Code: Gere um QR Code a partir do ID de pagamento para facilitar o pagamento.
Armazenar para referência: Salve o ID de pagamento para consultas futuras.
Observações:

Este código ainda necessita de um lightningd em execução e o pyln-client instalado.
Certifique-se de substituir os valores de exemplo (valor, descrição) pelas informações reais do seu pagamento.
O ID de pagamento (bolt11) é um código único e sensível. Não o compartilhe com ninguém que você não confie.
Lembre-se:

A geração de faturas com ID de pagamento é um processo fundamental para receber pagamentos na Lightning Network.
Utilize o ID de pagamento de forma segura e responsável para garantir transações confiáveis.
'''
