"""O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                          Até 5 Kg           Acima de 5 Kg
    File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
    Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
    Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

    Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
    porém não há limites para a quantidade de carne por cliente. 
    Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
    Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
    contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, 
    valor do desconto e valor a pagar. """

tipo_de_carne = input("Digite o tipo de carne que voce deseja ")
quantidade = float(input("Digite a quantidade em KG que você deseja "))



if tipo_de_carne == "File Duplo" and quantidade <= 5:
    preco = 4.9
    total = preco * quantidade
    print(tipo_de_carne)
    print(quantidade)
    print(f"O valor por KG é de {preco}")
    print(f"R${total:.2f}")
    
elif tipo_de_carne == "File Duplo" and quantidade > 5:
    preco = 5.80
    total = preco * quantidade
    print(tipo_de_carne)
    print(quantidade)
    print(f"O valor por KG é de {preco}")
    print(f"R${total:.2f}")

elif tipo_de_carne == "Alcatra" and quantidade <= 5:
    preco = 5.9
    total = preco * quantidade
    print(tipo_de_carne)
    print(quantidade)
    print(f"O valor por KG é de {preco}")
    print(f"R${total:.2f}")

elif tipo_de_carne == "Alcatra" and quantidade > 5:
    preco = 6.8
    total = preco * quantidade
    print(tipo_de_carne)
    print(quantidade)
    print(f"O valor por KG é de {preco}")
    print(f"R${total:.2f}")

elif tipo_de_carne == "Picanha" and quantidade <= 5:
    preco = 6.9
    total = preco * quantidade
    print(tipo_de_carne)
    print(quantidade)
    print(f"O valor por KG é de {preco}")
    print(f"R${total:.2f}")

elif tipo_de_carne == "Picanha" and quantidade > 5:
    preco = 7.8
    total = preco * quantidade
    print(tipo_de_carne)
    print(quantidade)
    print(f"O valor por KG é de {preco}")
    print(f"R${total:.2f}")

else: 
    print("Produto não está em oferta ou foi digitado incorretamente")


