# Não poderíamos falar de listas sem mencionar duas funções built-in que são usadas por esse tipo de estrutura
# de dados: map() e filter(). A função map() é utilizada para aplicar uma determinada função em cada item de um
# objeto iterável. Para que essa transformação seja feita, a função map() exige que sejam passados dois
# parâmetros: a função e o objeto iterável.

linguagens = '''Python Java JavaScript C C# C++ Swift Go Kotlin'''.split()

nova_lista = map(lambda x: x.lower(), linguagens)
print(f"A nova lista é {nova_lista}")

nova_lista = list(nova_lista)
print(f"Agora sim, a nova lista é {nova_lista}")

#Outro exemplo

numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = list(map(lambda x: x*x, numeros))
print(f"Lista de numero elevado a ele mesmo {quadrados}")

# Filter

#A função filter() tem as mesmas características da função map(), mas, em vez de usarmos uma função para transformar
# os valores da lista, nós a usamos para filtrar. Veja o código a seguir.

print("\nList")
numeros = list(range(0, 100))
numeros_pares = list(filter(lambda x: x%2 == 0, numeros))
print(f"Numero pares de 0 à 100: {numeros_pares}")
