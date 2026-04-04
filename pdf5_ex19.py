print("19. Leia dois números e: Verifique se são iguais ou diferentes. Sendo diferentes mostre a diferença entre eles.")
a = float(input("Digite o valor  de A : "))
b = float(input("Digite o valor de B : "))
if (a > b):
    c = a - b
    print("O valor da diferença é :  ", c)
elif(b > a):
    c = b - a
    print("O valor da diferença é : ", c)
else:
    print("Os dois números são iguais")
      