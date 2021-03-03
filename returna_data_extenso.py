# Vamos implementar uma função que recebe uma data no formato
# dd/mm/aaaa e converte o mês para extenso. Então, ao se receber
# a data 10/05/2020, a função deverá retornar: 10 de maio de 2020.
# Observe a implementação a seguir.

def converter_mes_para_extenso(data):
    mes = '''janeiro fevereiro março abril maio junho julho agosta
    setembro outubro novembro dezembro'''.split()
    d, m, a = data.split('/')
    mes_extenso = mes[int(m) -1] # O mes 1 estará na posição zero
    return f'{d} de {mes_extenso} de {a}'

print(converter_mes_para_extenso('10/05/2021'))