# print("11. Leia um número e: Se for par e positivo → “Par positivo”")
# print("Se for par e negativo → “Par negativo”; Caso contrário → “Ímpar”.") 
a = float(input("Digite o número : "))

if (a > 0):
    if(a % 2 == 0):
        print("Par positivo")

    else:
        print("Ímpar Positivo")   

if(a < 0):
    if(a % 2 == 0):
        print("Par Negativo")
    else:
        print("Ímpar negativo")

else:
    print("Nesse caso ele é igual a zero")

