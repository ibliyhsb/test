
num= input("ingrese numeros enteros separados por espacios: ")
num= num.split()

def validar_lista_numeros(num):
    for numero in num:
        try:
            int(numero)
        except ValueError:
            print("no es entero")

validar_lista_numeros(num)







