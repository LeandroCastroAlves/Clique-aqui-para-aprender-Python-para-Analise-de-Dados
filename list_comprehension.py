#  Forma pythônica de criar uma lista com base em um objeto iterável

# Esse tipo de técnica é utilizada quando, dada uma sequência, deseja-se criar uma nova sequência,
# porém com as informações originais transformadas ou filtradas por um critério.

linguagens = ["Python", "Java", "JavaScript", "C", "C#", "C++", "Swift", "Go", "Kotlin"]
print("Antes da listcomp = ", linguagens)

linguagens = [i.lower() for i in linguagens]
print("Depois da listcomp = ", linguagens)

# Lista que possue somente a liguagem que possui java no texto

linguagens_java = [i for i in linguagens if "java" in i]
print(linguagens_java)

# Para palavras identicas...

linguagens_java_identicas = [i for i in linguagens if "java" == i]
print(linguagens_java_identicas)