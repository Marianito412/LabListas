import re

#0201-304-i0506
def decodificarPisoPasillo(pCodigo):
    info = re.findall("-([\d]{3})-", pCodigo)[0]
    return f"El material bibliográfico está en el piso {info[0]} en el pasillo {info[1:]}"
