import random

# Lista de caracteres
letras_minusculas=list("abcdefghijklmnñopqrstuvwxyz")
letras_mayusculas=list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")
numeros=list("0123456789")
simbolos=list("¿?/&%$#(><)!¡*+")

# Diccionario de recomendaciones
recomendaciones={
    1:"Usa contraseñas de minimo 8 carcateres.",
    2:"Combina letras mayusculas, minusculas, numeros y simbolos.",
    3:"No uses tu nombre, fecha de nacimiento o datos personales.",
    4:"No compartas tu contraseñas con otras personas.",
    5:"Cambia tus contraseñas cada cierto tiempo."
}

def mostrar_menu():
    print("------GENERADOR SEGURO DE CONTRASEÑAS------")
    print("1. Generar contraseña segura")
    print("2. Ver recomendaciones de seguridad")
    print("3. Salir")

def mostrar_recomendaciones():
    print("-----RECOMENDACIONES DE SEGURIDAD-----")
    for numero in recomendaciones:
        print(str(numero)+". " + recomendaciones[numero])

def generar_contrasena():

    longitud=int(input("Ingrese la longitud de la contraseña: "))

    if longitud<8:
        print("La contraseña debe tener mínimo 8 caracteres para ser segura.")
        return
    
    caracteres=[]

    mayusculas=input("¿Desea incluir letras mayúsculas? (si/no): ").lower()
    if mayusculas=="si":
        caracteres=caracteres+letras_mayusculas

    minusculas=input("¿Desea incluir letras minisculas? (si/no): ").lower()
    if minusculas=="si":
        caracteres=caracteres+letras_minusculas

    numeros_op=input("¿Desea incluir números? (si/no): ").lower()
    if numeros_op=="si":
        caracteres=caracteres+numeros

    simbolos_op=input("¿Desea incluir simbolos? (si/no): ").lower()
    if simbolos_op=="si":
        caracteres=caracteres+simbolos

    if len(caracteres)==0:
        print("Debe seleccionar al menos un tipo de carácter.")
        return
    
    contrasena=""

    for i in range(longitud):
        contrasena= contrasena + random.choice(caracteres)

    print("---------------------------")
    print("Contraseña generada: ", contrasena)
    print("---------------------------")

    cantidad=0

    if mayusculas=="si":
        cantidad=cantidad+1
    if minusculas=="si":
        cantidad=cantidad+1
    if numeros_op=="si":
        cantidad=cantidad+1
    if simbolos_op=="si":
        cantidad=cantidad+1

    if longitud>=12 and cantidad>=4:
        print("Nivel de seguridad: MUY ALTO")
    elif longitud>=10 and cantidad>=3:
        print("Nivel de seguridad: ALTO")
    elif longitud>=8 and cantidad>=2:
        print("Nivel de seguridad: MEDIO")
    else:
        print("Nivel de seguridad: BAJO")

    repetir=input("¿Desea generar otra contraseña? (si/no): ").lower()

    if repetir=="si":
        generar_contrasena()
    else:
        print("Regresando al men{u principal...")

def iniciar_programa():
    while True:
        mostrar_menu()
        opcion=input("Elige una opción: ")

        if opcion=="1":
            generar_contrasena()

        elif opcion=="2":
            mostrar_recomendaciones()

        elif opcion=="3":
            confirmar=input("¿Seguro que desea salir? Escribe si o no: ").lower()

            if confirmar=="si":
                print("Gracias por usar el Generador Seguro de Contraseñas.")
                break
            else:
                print("Regresando al menú principal...")

        else:
            print("Opción incorrecta. Intente nuevamente.")

# Inicio del programa
iniciar_programa()


              