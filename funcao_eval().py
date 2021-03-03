# funções de python https://docs.python.org/3/library/functions.html

# A função eval() usada no código recebe como entrada uma string
# (sequência de caracteres) digitada pelo usuário, que nesse caso
# é uma equação linear. Essa entrada é analisada e avaliada como uma
# expressão Python pela função eval(). Veja que, para cada valor de x,
# a fórmula é executada como uma expressão matemática (linha 10) e
# retorna um valor diferente.

# A função eval() foi mostrada a fim de exemplificar a variedade de
# funcionalidades que as funções built-in possuem. Entretanto,
# precisamos ressaltar que eval é uma instrução que requer prudência
# para o uso, pois é fácil alguém externo à aplicação fazer uma
# "injection" de código intruso.

a = 2
b = 1

equacao = input("Digite a formula geral da equação linear: (a * x + b): ")
print(f"\nA entrada do usuario {equacao} é do tipo {type(equacao)}")

for x in range(5):
    y = eval(equacao)
    print(f"\nResultado da equacao para x = {x} é {y}")