a = 0
b = 5
c = 9
print("A =", a, "----B =", b, "===C =", c)
if (a > b) and (b > c):

    print("Primmeiro maior 'a': ", a, " Segundo maior 'b': ", b, " Ultimo é 'c': ", c)


elif (b > a) and (a > c):
    print("==============Primmeiro maior 'b': ", b, " Segundo maior 'a': ", a, " Ultimo é 'c': ", c,"==============")

elif (c > b ) and (a > b):
    print("_____Primmeiro maior 'c': ", c, " Segundo maior 'a': ", a, " Ultimo é 'b': ", b,"_____")


elif (c > b ) and (b > a):
    print("_____Primmeiro maior 'c': ", c, " Segundo maior 'b': ", b, " Ultimo é 'a': ", a,"_____")


elif (a==b) and (b==c):
    print("Os valores são iguais")
else:
    print("ascou")    