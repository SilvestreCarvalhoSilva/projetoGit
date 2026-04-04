print("23. Leia três números inteiros informados pelo usuário. Exiba em ordem decrescente o resto da divisão por 3.")
a = int(input("Digite valor de a : "))
b = int(input("Digite valor de b : "))
c = int(input("Digite valor de c : "))

aa = int(a/3)
print(aa)
bb = int(b/3)
print(bb)

cc = int(c/3)
print(cc)
print("-----------------------------------------------------------------------------------------------------------")
if(aa > bb) and (bb > cc):
    print(aa, bb, cc)
elif(aa > cc) and (cc > bb):
   print(aa, cc, bb)

elif(bb > aa) and (aa > cc):
    print(bb, aa, cc)

elif (bb > cc) and (cc > aa):
     print(bb, cc, aa)

elif(cc > bb) and (bb > aa):
    print(cc, bb, aa)
elif(cc > aa) and (aa > bb):
    print(cc, aa, bb)   
else:
    print("Se essa mensagem apareceu para você significa que algo deu errado nos número acima")
