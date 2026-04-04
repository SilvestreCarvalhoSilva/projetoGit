print("Escrevaum programa que, dados três números inteiros, imprima o menor deles.")  


# a = -3
# b = -1
# c = 9
a = float(input("Digite Primeiro valor : "))
b = float(input("Digite Segundo valor : "))
c = float(input("Digite Terceiro valor : "))

if(a <= b) and (b <= c):
    print("Valor menor é : ", a)
elif(b <= a) and (a <= c):
    print("O menor valor é : ", b)
else:
 print("O menor valor é C : ", c)

if (a == b) or (b == c) or (a == c):
    print("Dois ou mais valores são iguais")

print("---------------------------------------------------------------------------------------------------------------------")
print("Exercicio1. Este programa tem um comportamento indesejado quando o menor número não é único. Como corrigi-lo?")
    