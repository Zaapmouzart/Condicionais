"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez. 

"""

nota1 = float(input("Digite a nota do primeiro bimestre"))
nota2 = float(input("Digite a nota do segundo bimestre"))
nota3 = float(input("Digite a nota do terceiro bimestre"))
nota4 = float(input("Digite a nota do quarto bimestre"))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media == 10:
    print("Parabéns, você foi aprovado com distinção ")
elif media >=7:
    print("Você foi aprovado ")
else:
    print("Você foi reprovado") 

print(f"A sua média é {media}")
