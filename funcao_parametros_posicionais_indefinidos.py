# a passagem de valores é feita de modo posicial,
# porém a quantidade não é conhecida. Observe a função
# "obter_parametros" a seguir

def imprimir_parametros(*args):
    qtde_parametros = len(args)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for i, valor in enumerate(args):
        print(f"Posicao {i}, parametro = {valor}")

print("\nChamada 1")
imprimir_parametros("Uberlândia", 10, 23.78, "Leandro")