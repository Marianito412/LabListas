import re

#0201-304-i0506
def decodificarPisoPasillo(pCodigo):
    info = re.findall("-([\d]{3})-", pCodigo)[0]
    return f"está en el piso {info[0]} en el pasillo {info[1:]}"

def decodificarAreaYTipo(pCodigo):
    listaTipos=["1","un libro","2","una revista","3","un folleto"]
    tipo=listaTipos[listaTipos.index(pCodigo[1])+1]
    listaArea=["1","cientifica","2","tecnologica","3","legislativa","4","medica"]
    area=listaArea[listaArea.index(pCodigo[3])+1]
    return f"es {tipo} del área {area}"

def decodificarDetalle(pCodigo):
    listaLados=["i","izquierdo","d","derecho"]
    lado=listaLados[listaLados.index(pCodigo[9])+1]
    fila=pCodigo[10:12]
    columna=pCodigo[12:]
    return f"está al lado {lado}, en la fila {fila} columna {columna}"

def decodificarCompleto(pCodigo):
    return f"{decodificarAreaYTipo(pCodigo)}, {decodificarPisoPasillo(pCodigo)}, {decodificarDetalle(pCodigo)}"
