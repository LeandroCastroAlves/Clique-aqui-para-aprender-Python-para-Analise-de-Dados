def calcular_valor(valor_prod, qtde, moeda="real", desconto=None, acrescimo=None):

    v_bruto = valor_prod*qtde

    if moeda == "real":
        v_liquido = v_bruto
    elif moeda == "dolar":
        v_liquido = v_bruto*5
    elif moeda == "euro":
        v_liquido = v_bruto*5.7

    if desconto:
        return v_liquido - (v_liquido*(desconto/100))

    elif acrescimo:
        return v_liquido + (v_liquido*(acrescimo/100))




valor_a_pagar = calcular_valor(valor_prod=32, qtde=5, desconto=5)
print(f"O valor final da conta é {valor_a_pagar}")