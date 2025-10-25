import math

numero=int(input(f"Ingresar un numero entero mayor a:  "))

while numero !=0:
    if numero == 0 or numero < 0:
     print(f"el numero no puede ser 0 o menor a 0")
     break
    else:
        palabra= str(input(f"Ingresa una palabra:  "))
        a= len(palabra)
        print(a)
    resultado=math.factorial(a)
    print(resultado)
    if resultado %2  == 0 :
       print("par")
    else:
        print("impar")
    numero=int(input(f"Ingresar el numero 0 si quiere finalizar el programa:  "))
    if numero == 0:
        print("A concluido el programa")
        break
