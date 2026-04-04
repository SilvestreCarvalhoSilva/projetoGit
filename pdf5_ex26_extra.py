print("Leia um número inteiro. Classifique o número de acordo com as seguintes regras: Se for maior que 0:")
print("Se for menor que 10 → exiba: “Pequeno”; Se estiver entre 10 e 100 → exiba: “Médio”;")
print("Se for maior que 100 → exiba: “Grande”; Caso contrário, exiba: “Negativo ou zero”")
a = int(input("Digite o valor : "))
if(a > 0) and ( a < 10):
    print("Pequeno")
elif(a > 10) and (a < 100):
    print("Médio") 
elif(a > 100):
    print("Grande")  
else:
    print("Negativo ou zero")    