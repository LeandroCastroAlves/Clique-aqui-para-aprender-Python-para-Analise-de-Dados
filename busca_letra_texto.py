disciplina = "A inserção de comentários no código do programa é uma prática normal. Em função disso, toda linguagem de programação tem alguma maneira de permitir que comentários sejam inseridos nos programas. O objetivo é adicionar descrições em partes do código, seja para documentá-lo ou para adicionar uma descrição do algoritmo implementado (BANIN, 2018, p. 45)"
disciplina = disciplina.lower()
letra_1 = input("Primeira letra a ser encontrada ")
letra_2 = input("Segunda letra a ser encontrada ")
count_1 = []
count_2 = []

for i, c in enumerate(disciplina):
    if c == letra_1 or c == letra_2:
        print(f"Letra {c} na posição {i}")
        if c == letra_1:
            count_1.append(c)
        elif c == letra_2:
            count_2.append(c)
print(f"Itens encontrados da letra {letra_1} {len(count_1)}")
print(f"Itens encontrados da letra {letra_2} {len(count_2)}")



