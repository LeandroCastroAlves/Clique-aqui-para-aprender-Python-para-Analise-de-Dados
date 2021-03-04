# Manipulando string e textos

texto = '''A amizade consegue ser tão complexa...
Deixa uns desanimados, outros bem felizes...
É a alimentação dos fracos
É o reino dos fortes

Faz-nos cometer erros
Os fracos deixam se ir abaixo
Os fortes erguem sempre a cabeça
os assim assim assumem-os

Sem pensar conquistamos
O mundo geral
e construímos o nosso pequeno lugar
deixando brilhar cada estrelinha

Estrelinhas...
Doces, sensíveis, frias, ternurentas...
Mas sempre presentes em qualquer parte
Os donos da amizade'''
print(f"Tamanho do texto: {len(texto)}")
texto = texto.lower()
pontuacoes = [",", ".", "(", ")", ";", ":"]
for i in pontuacoes:
    texto = texto.replace(i, "")
palavras = texto.split()
palavra = input("Palavra a ser encontrada: ")
for i in palavras:
    conta_palavras = palavras.count(palavra)
print(f"A palavra {palavra} conta em {conta_palavras} resultados de pesquisa")