print("28. Leia um valor informado pelo usuário. Verifique o tipo da variável; Caso seja possível interpretá-lo como um valor numérico:")
print("Se for um número inteiro, exiba o dobro; Caso seja um número real, exiba a metade")
print("Caso não seja possível interpretar como número, exiba: “Tipo inválido”.")
a = float(input("Digite o valor : "))
b = type(a)
d = str(a)
print(d)
print(b)
c = a/2
print("-------------------------------------------------------------------------------------------------------")
if (a % 2 == 0) or (a % 2 == 1):
    print("É número inteiro : ", a*a)

elif (c != 0) or (c != 1):
    print ("Exibindo o  a metade ", a/2)


else: 
    print("Tipo inválido")    