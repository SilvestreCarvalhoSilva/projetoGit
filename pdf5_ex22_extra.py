print("22. Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro. Caso não seja possível realizar a conversão,")
print("“Entrada inválida”. Caso a conversão seja bem-sucedida: Se o número for maior que 10, exiba: “Alto”.")
print(":  Caso contrário, exiba: “Baixo”.")
print("-------------------------------------------------------------------------------------------------------------------------------")
# a = float(input("Digite o valor : "))
a = float(input("Digite o valor  de a : "))
d = int(a)
b = int(a)
print(b)
if(b % 2 == 0) or (b % 2 == 1):
    if ( d > 10 ):
        print("este é o valor de d : ", d)
        print("Alto")
    else:
        print("Baixo")    
else:
    print("Entrada invalida")    
    