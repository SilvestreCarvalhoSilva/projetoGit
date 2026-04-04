print("27. Leia dois números informados pelo usuário. Se ambos forem positivos, calcule e exiba a soma entre eles Caso contrário,")
print("calcule e exiba o produto entre eles.")
a = int(input("Digite o valor : "))
b = int(input("Digite o valor : "))
if (a > 0) and (b > 0):
    c = a + b
    print("A soma entre eles são : ", c)
else:
    d = a * b
    print("A mulltiplicação entre eles é : ", d)
    