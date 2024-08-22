numero1 = float(input("Digite el primer numero "))
numero2 = float(input("Digite el segundo numero "))

if numero1 == numero2:
    print("Los numeros son iguales")
elif numero1 > numero2:
    print(numero1, " es mayor que ",numero2)
else:
    print(numero2, " es mayor que ",numero1)