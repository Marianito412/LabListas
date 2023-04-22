#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 19/04/2023 12:25am
#Ultima version: 21/04/2023 5:34pm
#Version: 3.10.6

#Importacion de bibliotecas
import re
import funciones

#Definición de funciones
def validarCodigos(pCodigos):
    """
    Funcionalidad: Valida una lista de códigos dados
    Entradas:
    -pCodigos(list): La lista de codigos a validar
    Salidas:
    -return(list): La lista de códigos validados o False si algun código no es válido
    """
    for codigo in pCodigos.split(","):
        codigo = codigo.strip()
        print(codigo)
        if not validarCodigo(codigo):
            return False
    return [codigo.strip() for codigo in pCodigos.split(",")]

def validarCodigo(pCodigo):
    """
    Funcionalidad: Valida un código dado
    Entradas:
    -pCodigo(str): El código a validar
    Salidas:
    -return(bool): True si el código es válido y False si no 
    """
    if re.match("0[123]0[1234]-[\d]{3}-[id][\d]{4}", pCodigo):
        return True
    else:
        return False

def validarBin(pEntrada):
    """
    Funcionalidad: Valida un sí o no y retorna el binario
    Entradas:
    -pEntrada(str): Texto conteniendo sí o no
    Salida:
    return(bool): True si sí, False si no 
    """
    while True:
        if pEntrada.upper().replace("Í", "I") == "SI":
            return True
        elif pEntrada.lower() == "no":
            return False
        else:
            pEntrada = input("Entrada incorrecta, vuelva a intentar ( ingrese sí o no) ")

def validarEntero(pnumero):
    """
    Funcionalidad: Valida un número entero
    Entradas:
    -pCodigo(str): El número a validar a validar
    Salidas:
    -return(int): El número validado
    """
    while True:
        try:
            pnumero = int(pnumero)
            if pnumero >=1 and pnumero<=5:
                break
            else:
                print("Ingrese un valor positivo")
        except ValueError:
            try:
                pnumero = float(pnumero)
                print("El número debe ser entero")
            except ValueError:
                print("Ingrese un valor numérico")
        pnumero = input("Ingrese un número: ")
    return pnumero

def menuDecodificar(pDecodificar, pCodigos):
    """
    Funcionalidad: Muestra un menu de opciones para decodificar
    Entradas: NA
    Salidas: NA
    """
    print(
        "1. Decodificar area y tipo\n"
        "2. Decodificar piso y pasillo\n"
        "3. Decodificar detalle\n"
        "4. Decodificación completa\n"
        "5. Salir"
    )
    opcion = validarEntero(input("Ingrese su elección: "))
    if opcion == 1:
        return "El material bibliográfico "+funciones.decodificarAreaYTipo(pDecodificar) + "."
    elif opcion == 2:
        return "El material bibliográfico "+funciones.decodificarPisoPasillo(pDecodificar) + "."
    elif opcion == 3:
        return "El material bibliográfico "+funciones.decodificarDetalle(pDecodificar) + "."
    elif opcion == 4:
        return "El material bibliográfico "+funciones.decodificarCompleto(pDecodificar) + "."
    elif opcion == 5:
        funciones.graba("biblioteca", pCodigos)
        exit()

def menu():
    """
    Funcionalidad: Solicita información al usuario
    Entradas: NA
    Salidas: NA
    """
    seguirRegistrando=True
    codigos = []
    while seguirRegistrando:
        codigosAgregar = validarCodigos(input("Ingrese los códigos que desea registrar (separelos con una coma): "))
        if codigosAgregar == False:
            print("Código inválido")
        else:
            codigos += codigosAgregar
        seguirRegistrando = validarBin(input("Desea ingresar más códigos (si/no)? "))
    
    seguirDecodificando = True
    while seguirDecodificando:
        codigoDecodificar = input("Ingrese el código que desea decodificar: ")
        if validarCodigo(codigoDecodificar):
            if codigoDecodificar in codigos:
                print(menuDecodificar(codigoDecodificar, codigos))
            else:
                print("El código no existe")
        else:
            print("Código inválido")

#Programa principal
menu()
