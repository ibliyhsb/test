import csv
from datetime import date
salir=True

def guardar_asistencia(nombre, asistencia):
    with open ('asistencia.csv', 'w', newline='') as archivo_csv:
        escritor_csv=csv.writer(archivo_csv)
        escritor_csv.writerow([nombre, asistencia, date.today().strftime('%d-%m-%y')])

def buscar_asistencia(nombre, fecha):
    with open('asistencia.csv', 'r', newline='') as archivo_csv:
        reader = csv.reader(archivo_csv)
        for fila in reader:
            if fila[0]==nombre and fila[2]==fecha:
                return asistencia
    
while True:
    opcion=int(input("seleccione una opcion: \n 1) guardar asistencia \n 2) buscar asistencia \n"))
    if opcion==1:
        salir=True
        while salir:
            nombre=input("ingrese nombre del estudiante: ")
            if nombre != "salir":
                asistencia=input("asistió?: ")
                guardar_asistencia(nombre, asistencia)
            else:
                salir=False
    if opcion==2:
        salir=True
        while salir:
            nombre=input("ingrese nombre del estudiante: ")
            if nombre != "salir":
                fecha=input("ingrese la fecha: ")
                print(buscar_asistencia(nombre, fecha))
            else:
                salir=False




        
