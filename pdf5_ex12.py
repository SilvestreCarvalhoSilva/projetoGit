print("Leia dois números e: Mostre a soma; Mostre qual é maior ou se são iguais.")
a = float(input("Qual valor de A : "))
b = float(input("Qual valor de B : "))
c = a + b
print("A soma é : ", c)

if( a > b):
    print("O maior valor é o A")
elif(a < b):
    print("O maior valor é o B")
else:
    print("Neste caso o valor do número é zero")