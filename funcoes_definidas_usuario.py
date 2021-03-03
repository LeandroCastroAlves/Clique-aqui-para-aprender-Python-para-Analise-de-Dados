# Para que o resultado de uma função possa ser guardado em uma
# variável, a função precisa ter o comando "return". A instrução
# "return", retorna um valor de uma função. Veja a nova versão da
# função "imprimir_mensagem", agora, em vez de imprimir a mensagem,
# ela retorna a mensagem para chamada.

def imprimir_mensagem(disciplina, curso):
    return f"Minha primeira função em Python desenvolvida na disciplina: {disciplina}" \
           f" do curso {curso}"
mensagem = imprimir_mensagem("Python", "ADS")
print(mensagem)