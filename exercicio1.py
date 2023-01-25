"""Faça um Programa que peça dois números e imprima o maior deles. """

a = int(input("Digite um número"))
b = int(input("Digite um número"))

maior = b
menor = a

if a > b:
    maior = a
    menor = b
    print(f"{a} é maior que {b}  ")
elif b > a:
    maior = b
    menor = a
    print(f"{b} é maior que {a}  ")
else:
    print("Numeros São iguais ")
