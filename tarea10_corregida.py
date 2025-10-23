import random 

numero_secretro= random.randint(1,10)


for i in range (5):
    numero=int(input(f"Ingresa un numero entre 1 y 10:  "))
    if numero == numero_secretro:
        print(f"adivinaste")
        break
    elif numero > numero_secretro:
        print(f"es menor  ")
    elif numero < numero_secretro :
        print(f"es mayor ")
else:
    print(f"Perdiste, el numero era: ", numero_secretro)