print("Leia um valor informado pelo usuário. Tente convertê-lo para número inteiro.")
print("Caso não seja possível, exiba: “Entrada inválida”; Caso seja possível:")
print("Verifique se o número é par: Se for par e maior que 100 → exiba: “Par alto”")
print("Se for par e menor ou igual a 100 → exiba: “Par baixo”; Caso não seja par, exiba: “Ímpar”.")
print("Este exercicio eu não estava conseguindo saber converte str para para int ai usei a internet")
try:
    
    a = float(input("Digite um número: "))
    
    
    numero = int(a) 
    
    if (numero % 2 == 0):
        if (numero > 100):
            print("Par alto")
        else:
            print("Par baixo")
    else:
        print("Ímpar")
        
except ValueError:
    
    print("Entrada inválida")