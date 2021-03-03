# https://docs.python.org/3/reference/expressions.html#lamb
# Já que estamos falando sobre funções, não podemos deixar de mencionar
# um poderoso recurso da linguagem Python: a expressão "lambda".
# Expressões lambda (às vezes chamadas de formas lambda) são usadas
# para criar funções anônimas

# Uma função anônima é uma função que não é construída com o "def" e,
# por isso, não possui nome. Esse tipo de construção é útil, quando a
# função faz somente uma ação e é usada uma única vez. Observe o código
# a seguir:


print((lambda x: x + 1)(x=3))


# Na entrada, criamos uma função que recebe como parâmetro
# um valor e retorna esse valor somado a 1. Para criar essa função anônima,
# usamos a palavra reservada "lambda" passando como parâmetro "x".
# O dois pontos é o que separa a definição da função anônima da sua ação,
# veja que após os dois pontos, é feito o cálculo matemático x + 1.
# Na frente da função, já a invocamos passando como parâmetro o valor x=3,
# veja que o resultado é portanto 4.

print((lambda x, y: x + y)(x=3, y=2))

# Podemos invocar mais de um parâmetros

somar = lambda x, y: x + y
print(somar(x=5, y=3))

# criamos uma função anônima que recebe como parâmetro dois valores e
# retorna a soma deles, essa função foi atribuída a uma variável chamada
# "somar". Veja que na linha 2, fazemos a chamadada função através do nome
# da variável, passando os parâmetros que ela requer.

