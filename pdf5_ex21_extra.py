print("21. Leia um número inteiro informado pelo usuário.Verifique se o número é positivo. Caso seja, analise se ele é múltiplo de 2 e de 3 ao mesmo tempo.")
print("Se atender a ambas as condições, exiba: “Múltiplo de 2 e 3”. Caso contrário, exiba: “Não atende”. Se o número não for positivo, exiba: “Número inválido”.")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Observação : Todo número que é múltiplo de 6 é também múltiplo de 2 e de 3 ao mesmo tempo. ")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
a = float(input("Digite um valor : "))
if(a > 0):
    if(a % 6 == 0):
    
        print("Então este  número é multiplo de 2 e 3")
    else:
     print("Não atende")
else:
    print("Senhor e número é zero")
