#pense ingreso por cuit para empresas y por dni para clientes
cont=0
opcion = 3
while opcion > 2:  #por si ingresan opcion que no existe
    opcion = int(input("INGRESE TIPO DE ACCESO:\n1)CUIT\n2)DNI\n"))
    if opcion == 1:
        user = input("INGRESE CUIT SIN GUIONES:\t")
        while user != "27947287058": #BASE DE DATOS DE BUSQUEDA DE USUARIO uso ejemplo mi dni
            print("USUARIO INEXISTENTE")
            user = input("INGRESE CUIT SIN GUIONES:\t")
    elif opcion == 2:
        user = input("INGRESE DNI SIN PUNTOS:\t")
        while user != "94728705": #BASE DE DATOS DE BUSQUEDA DE USUARIO uso ejemplo mi dni
            print("USUARIO INEXISTENTE")
            user = input("INGRESE DNI SIN PUNTOS:\t")
    else:
        print("OPCION INVALIDA")

for i in range (3): # 3 intentos y se bloquea la clave
    password = input("INGRESE CONTRASEÑA:\t")
    if password != "Info2020": #aca habria que usar base de datos, ejemplo pongo esa clave de prueba
        print("CONTRASEÑA INVALIDA")
    else:
        print("INGRESO SATISFACTORIO")
        break

if i==3:
    print("Usuario bloqueado.")


if len(user) <= 8:
    #interfaz de usuario cliente
    print("Interfaz Cliente")
else:
    #interfaz de usuario empresa
    print("Interfaz Empresa")