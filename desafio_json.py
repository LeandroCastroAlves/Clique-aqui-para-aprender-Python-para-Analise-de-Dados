# Ha duas lista com informações de envios de email, em que os registro que tiverem a informaçõo de email = False
# nao foram enviados email. Extraia os email dos registros das pessoas em que os email nao foram enviados

# Eu poderia ter feito sem o pandas, mas preferi assim. Há varias formas de se resolver o problema

import pandas as pd

dados_1 = {
  'nome': ['Sonia Weber', 'Daryl Lowe', 'Vernon Carroll', 'Basil Gilliam', 'Mechelle Cobb', 'Edan Booker', 'Igor Wyatt', 'Ethan Franklin', 'Reed Williamson', 'Price Singleton'],
  'email': ['Lorem.ipsum@cursusvestibulumMauris.com', 'auctor@magnis.org', 'at@magnaUttincidunt.org', 'mauris.sagittis@sem.com', 'nec.euismod.in@mattis.co.uk', 'egestas@massaMaurisvestibulum.edu', 'semper.auctor.Mauris@Crasdolordolor.edu', 'risus.Quisque@condimentum.com', 'Donec@nislMaecenasmalesuada.net', 'Aenean.gravida@atrisus.edu'],
  'enviado': [False, False, False, False, False, False, False, True, False, False]
}

dados_2 = {
  'nome': ['Travis Shepherd', 'Hoyt Glass', 'Jennifer Aguirre', 'Cassady Ayers', 'Colin Myers', 'Herrod Curtis', 'Cecilia Park', 'Hop Byrd', 'Beatrice Silva', 'Alden Morales'],
  'email': ['at@sed.org', 'ac.arcu.Nunc@auctor.edu', 'nunc.Quisque.ornare@nibhAliquam.co.uk', 'non.arcu@mauriseu.com', 'fringilla.cursus.purus@erategetipsum.ca', 'Fusce.fermentum@tellus.co.uk', 'dolor.tempus.non@ipsum.net', 'blandit.congue.In@libero.com', 'nec.tempus.mauris@Suspendisse.com', 'felis@urnaconvalliserat.org'],
  'enviado': [False, False, False, True, True, True, False, True, True, False]
}
def n_enviados(dict_1, dict_2):
  dados = pd.DataFrame(dict_1)
  dados_ = pd.DataFrame(dict_2)
  dados = [dados_, dados]
  dados = pd.concat(dados)
  dados_nao_enviado = dados[dados.enviado.eq(False)]
  lista = []
  for i in dados_nao_enviado['email']:
    lista.append(i)
  return f"emails nao enviado \n{lista}"

i = n_enviados(dados_1, dados_2)
print(i)


