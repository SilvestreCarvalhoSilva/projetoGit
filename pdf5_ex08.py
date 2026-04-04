print("8. Leia um número e: Se for positivo, mostre a raiz aproximada (use **0.5); Caso contrário, informe “Número inválido”")
a = float(input("Digite o valor"))
if(a > 0):
    a = (a**0.5)
    print("O resultado da aproximado  raiz é : ", a)
else:
    print("Número Ínválido")
