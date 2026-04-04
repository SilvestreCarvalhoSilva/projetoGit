print("17. Leia idade e: Mostre: Menor de idade (<18); Adulto (18 a 59); Idoso (60+).")
idade =float(input("Digite um valor : "))
if (idade < 18):
    print("Menor de Idade")
elif(idade > 18) and (idade < 59):
    print("Adulto")
else:
    print("Idoso")
