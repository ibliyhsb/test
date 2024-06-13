pares=[]
impares=[]

def valida_numeros(list):
        for num in list:
            try:
                int (num)
            except:
                 print("ingreso valor no valido")
                 return "no valid"
        return "valid"

validador="no valid"
while validador == "no valid":
    nums = input("ingresa una lista de numeros separados por espacio: ")
    nums_list= nums.split()

    validador=valida_numeros(nums_list)

def pareimpar(nums_list):
    for num in nums_list:
        numero=int(num)
        numero= numero%2
        if numero == 0:
            pares.append(num)
        else:
            impares.append(num)


pareimpar(nums_list)
print("numeros pares: ", pares)
print("numeros impares: ", impares)
