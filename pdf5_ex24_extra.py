print("24. Leia um número inteiro. Verifique se ele está no intervalo de 1 a 100 (inclusive).")
print("Se estiver: Verifique se o número é par ou ímpar; Exiba: “Par no intervalo” ou “Ímpar no intervalo”.")
print("Caso não esteja no intervalo, exiba: “Fora do intervalo”.")
print("=====================================================================================================")
a = int(input("Digite valor de a : "))
# python pdf5_ex25_extra.py
if ( a > 1) and (a < 100):
    if(a % 2 == 0):
        print("Par")
    else:
        print("Ímpar")    

else:
    print("Número fora  do Íntervalo")