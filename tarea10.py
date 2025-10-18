import random 

numero_secretro= random.randint(1,10)


for i in range (5):
    numero=int(input(f"Ingresa un numero entre 1 y 10:  "))
    if numero > 10:
        print(f"Ingresaste un numero que supera el 10: ")
    elif numero < 1:
        print(f"ingresaste un numero que es menor a 1: ")
    elif numero == numero_secretro:
        print(f"adivinaste")
        break
else:
    print(f"Perdiste, el numero era: ", numero_secretro)