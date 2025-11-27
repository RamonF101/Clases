import random

def generar_contraseña(letras="abcdefghijklmnopqrstuvwxyz", numeros="0123456789",longitud= 12,  ):
    base2=letras+numeros
    base1 = random.sample(base2, longitud)
    contraseña="".join(base1)
    print(contraseña)

generar_contraseña()
