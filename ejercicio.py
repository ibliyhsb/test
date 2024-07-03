lista=[]
ceo=[]
desarrollador=[]
analista_de_datos=[]
ceo2=[]
desarrollador2=[]
analista_de_datos2=[]

def registrar_trabajador(nombre, cargo, sueldo_bruto):
    dcto_salud=sueldo_bruto*0.07
    dcto_afp=sueldo_bruto*0.12
    sueldo_liquido=sueldo_bruto-dcto_salud-dcto_afp
    lista.append([nombre, cargo, sueldo_bruto, dcto_salud, dcto_afp, sueldo_liquido])
    if cargo=="ceo":
        for fila in lista:
            if fila[1]=="ceo":
                ceo.append(fila)
                for i in range(len(ceo)):
                    if ceo[i] not in ceo2:
                        ceo2.append(ceo[i])           
    if cargo=="desarrollador":
        for fila in lista:
            if fila[1]=="desarrollador":
                desarrollador.append(fila)
                for i in range(len(desarrollador)):
                    if desarrollador[i] not in desarrollador2:
                        desarrollador2.append(desarrollador[i])
    if cargo=="analista de datos":
        for fila in lista:
            if fila[1]=="analista de datos":
                analista_de_datos.append(fila)
                for i in range(len(analista_de_datos)):
                    if analista_de_datos[i] not in analista_de_datos2:
                        analista_de_datos2.append(analista_de_datos[i])




def lista_trabajadores():
    with open ('lista_trabajadores.txt', 'w', newline='') as lista_trabajadores:
        lista_trabajadores.write(" nombre|cargo|sueldo bruto|dcto salud|dcto afp|sueldo liquido\n")
        for trabajador in lista:
            lista_trabajadores.write(f"{trabajador}\n")
    archivo=open('lista_trabajadores.txt', 'r')
    contenido=archivo.read()
    print(contenido)
    archivo.close

def planilla_trabajadores():
    opcion2=int(input("seleccione una opción: \n1) imprimir todos \n2) ceo \n3) desarrollador \n4) analista de datos\n"))
    if opcion2==1:
        with open ('lista_trabajadores.txt', 'w', newline='') as lista_trabajadores:
            lista_trabajadores.write(" nombre|cargo|sueldo bruto|dcto salud|dcto afp|sueldo liquido\n")
            for trabajador in lista:
                lista_trabajadores.write(f"{trabajador}\n")
    if opcion2==2:
        with open ('planilla_ceo.txt', 'w', newline='') as planilla_ceo:
            planilla_ceo.write(" nombre|cargo|sueldo bruto|dcto salud|dcto afp|sueldo liquido\n")
            for trabajador in ceo2:
                planilla_ceo.write(f"{trabajador}\n")
    if opcion2==3:
        with open ('planilla_desarrollador.txt', 'w', newline='') as planilla_desarrollador:
            planilla_desarrollador.write(" nombre|cargo|sueldo bruto|dcto salud|dcto afp|sueldo liquido\n")
            for trabajador in desarrollador2:
                planilla_desarrollador.write(f"{trabajador}\n")
    if opcion2==4:
        with open ('planilla_analista_de_datos.txt', 'w', newline='') as planilla_analista_de_datos:
            planilla_analista_de_datos.write(" nombre|cargo|sueldo bruto|dcto salud|dcto afp|sueldo liquido\n")
            for trabajador in analista_de_datos2:
                planilla_analista_de_datos.write(f"{trabajador}\n")
    
while True:
    opcion=int(input("elija una opción: \n1) Registrar trabajador \n2) listar todos los trabajadores \n3) imprimir planilla de sueldos \n4) salir del programa\n"))
    if opcion==1:
        nombre=input("ingrese el nombre del trabajador: ")
        cargo=input("ingrese el cargo del trabajador: ")
        sueldo_bruto=int(input("ingrese el sueldo bruto: "))
        registrar_trabajador(nombre, cargo, sueldo_bruto)
    if opcion==2:
        lista_trabajadores()
    if opcion==3:
        planilla_trabajadores()
    if opcion==4:
        break
