from pyln.client import LightningRpc
from time import sleep



class connect:

  def __init__(self):
    self.lnd = LightningRpc()
    self.on_or_false() # chama a função de verificação de connectividade!

  
  def on_or_false(self):
    try:

      if not self.lnd.is_connected():
        print("Erro: Falha ao conectar ao lightningd")
        
        """ Tomada de decisão caso não conecte!"""

      
      else:
        print("Conectado ao lightningd com sucesso!")

    except:
      pass # tratar erro.

  
  def loop_connect(self):
    TENTATIVA = 0 # número de tentativas de conexão!
    try:
      while True:
        sleep(5.1)
        
        if not self.lnd.is_connected():
          TENTATIVA =+1
          continue

        elif TENTATIVA == 50:
          break

        else: # caso de conetado, então saia do loop!
          break


    except:
      pass




# Conecta ao lightningd rodando no path padrão (/tmp/lightning/lightning-rpc)
#lnd = LightningRpc()

# Verifica se a conexão foi bem sucedida
#if not lnd.is_connected():
#  print("Erro: Falha ao conectar ao lightningd")
#  exit()

#print("Conectado ao lightningd com sucesso!")
