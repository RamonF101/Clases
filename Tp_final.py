import random

def crear_ticket(nombre, sector, asunto, problema, numT):

    archivo = open(f"{numT}.txt","a",encoding='utf-8')
    archivo.write(f"User: {nombre}\n")
    archivo.write(f"Sector: {sector}\n")
    archivo.write(f"Asunto: {asunto}\n")
    archivo.write(f"Problema: {problema}\n")
    
    archivo.close()

def leer_ticket(numT):
        archivo = open(f"{numT}.txt","r",encoding='utf-8')
        contenido= archivo.readlines()
        archivo.close()

        for linea in contenido:
            print(linea.strip())

def menu():
    while True:
        print("\n --- MENU DE TICKES ---")
        print(f"1 - Generar ticket")
        print(f"2 - Leer Ticket ")
        print(f"3 - Salir ")

        opcion=input(f"ingrese una opcion:  ")
        
        if opcion == "1":
            while True:
                ticket= random.randint(1000,9999)
                print(f"\n---Ingrese los datos para un nuevo ticket ---\n")
                nombre=input("Ingrese su nombre: ")
                sector=input("Ingrese el sector: ")
                asunto=input("Ingrese el asunto: ")
                problema=input("Ingrese el problema: ")
                crear_ticket(nombre,sector,asunto,problema,ticket)
                print("\n --- SE GENERO EL SIGUIENTE TICKET ---")
                print(f"\nSu nombre: {nombre}\nSu sector: {sector}\nSu asunto: {asunto}\nSu problema: {problema}\nTicket: {ticket}\n")
                while True:
                    pregunta=input("\nDesea generar otro Ticket s/n?: ")
                    
                    if pregunta == "s" or pregunta == "n":
                        break
                        
                if pregunta == "n":
                    break
        elif opcion == "2":
            while True:
                print("\n---TICKETS---\n")
                numT=int(input("\nIngrese el ticket para leer: "))
                print(f"-----TICKET N°{numT}-----")
                leer_ticket(numT)
                while True:
                    pregunta1=input("\nDesea desea leer otro Ticket s/n?: ")
                    
                    if pregunta1 == "s" or pregunta1 == "n":
                        break
                        
                if pregunta1 == "n":
                    break
        elif opcion == "3":
            print("FINALIZO EL PROGRAMA")
            return True
        
menu()






