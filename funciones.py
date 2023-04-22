#Elaborado por: Nicole Tatiana Parra Valverde y Mariano Soto
#Fecha de creacion: 19/04/2023 12:25am
#Ultima version: 21/04/2023 5:34pm
#Version: 3.10.6

#Importación de bibliotecas
import re
import pickle

#Definición de funciones
def decodificarPisoPasillo(pCodigo):
    """
    Funcionalidad: Decodifica el piso y pasillo del codigo dado
    Entrada:
    -pCodigo(str): Codigo a decodificar
    Salida:
    -return(str): Información extraida del código dado 
    """
    info = re.findall("-([\d]{3})-", pCodigo)[0]
    return f"está en el piso {info[0]} en el pasillo {info[1:]}"

def decodificarAreaYTipo(pCodigo):
    """
    Funcionalidad: Decodifica el area y tipo del codigo dado
    Entrada:
    -pCodigo(str): Codigo a decodificar
    Salida:
    -return(str): Información extraida del código dado 
    """
    listaTipos=["1","un libro","2","una revista","3","un folleto"]
    tipo=listaTipos[listaTipos.index(pCodigo[1])+1]
    listaArea=["1","cientifica","2","tecnologica","3","legislativa","4","medica"]
    area=listaArea[listaArea.index(pCodigo[3])+1]
    return f"es {tipo} del área {area}"

def decodificarDetalle(pCodigo):
    """
    Funcionalidad: Decodifica el detalle del codigo dado
    Entrada:
    -pCodigo(str): Codigo a decodificar
    Salida:
    -return(str): Información extraida del código dado 
    """
    listaLados=["i","izquierdo","d","derecho"]
    lado=listaLados[listaLados.index(pCodigo[9])+1]
    fila=pCodigo[10:12]
    columna=pCodigo[12:]
    return f"está al lado {lado}, en la fila {fila} columna {columna}"

def decodificarCompleto(pCodigo):
    """
    Funcionalidad: Decodifica la totalidad del codigo dado
    Entrada:
    -pCodigo(str): Codigo a decodificar
    Salida:
    -return(str): Información extraida del código dado 
    """
    return f"{decodificarAreaYTipo(pCodigo)}, {decodificarPisoPasillo(pCodigo)}, {decodificarDetalle(pCodigo)}"

def graba(nomArchGrabar,lista):
    #Función que graba un archivo con una lista de estudiantes
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(lista,f)
        f.close()
        print("Archivo Guardado!")
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)
