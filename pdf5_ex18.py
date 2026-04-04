print("18. Leia um número e: Mostre se ele é par positivo, par negativo, impar positivo, impar negativo ou neutro.")
a = 0
if(a > 0):
    if(a % 2 == 0):
        print("Ele positivo e é par")
    else:
     print("Ímpar e positivo")
else:
    print("Se chegou até aqui é pq tem coisa errada")     
if(a < 0):
    if( a % 2 == 0):
        print("O número é par negativo")
    else:
       print("Ímpar e negativo")
elif(a == 0):
    print("Neste caso o número é neutro")

            