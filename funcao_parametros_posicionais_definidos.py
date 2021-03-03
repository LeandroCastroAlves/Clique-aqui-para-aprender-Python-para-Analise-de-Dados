# A funçõe possui parâmetro nominal e
# não obrigatório. O mecanismo é parecido
# com funcao_parametros_posicionais_indefinidos,
# porém agora a passagem é feita de modo nominal e não posicional,
# o que nos permite acessar tanto o valor do parâmetro
# quanto o nome da variável que o armazena. Veja a função
# "imprimir_parametros" a seguir:

def imprimir_parametros(**kwargs):
    print(f"Tipo de objeto recebido = {type(kwargs)}")
    qtde_parametros = len(kwargs)
    print(f"Quantidade de parâmetros = {qtde_parametros}")

    for chave, valor in kwargs.items():
        print(f"variavel = {chave}, valor = {valor}")

print("\nChamada")
imprimir_parametros(cidade="Uberlandia", idade=29, nome="Leandro")