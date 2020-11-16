# Python3 programa para chequear si hay mas de tres caracteres conecutivios iguales 
import re

def comprobacion_cuatro_caracteres(str):

    # Regex para chequear si hay mas de tres caracteres consecutivos
    regex = r"(.)\1{3}"


    p = re.compile(regex)

    # Si está vacio devolver falso

    if (str == None):
        return False

    # Devolver si True o False

    if(re.search(p, str)):
        print("Simbolo repetido más de tres veces consecutivas")
        return True
    else:
        return False



    # Función para comprobar que los numero 5, 50 y 500 no se repiten 

def comprobacion_vld(str):

    regex = r"(L|V|D)\1{1}"

    p = re.compile(regex)

    if (str == None):
        return False

    m = re.search(p, str)
    if m:
        print("Simbolo repetido dos veces o más consecutivas")
        print(m.group(0))
        return True
    else:
        return False



    # Resta no permitida

def restaInvalid(str):

    regex = r"(IC|IM|IL|ID|XM|XD|VL|VD|LD|VX|VC|VM|LC|LM|DM|IIX|IIC|IIM|IIV|XXC|XXM|CCM|IIL|IID|XXL|XXD|CCD|DDM|VVX|VVL|VVC|VVD|VVM)"

    p = re.compile(regex)

    if (str == None):
        return False

    m = re.search(p, str)
    if m:
        print("Resta no permitida, estos dos símbolos no pueden unirse")
        print(m.group(0))
        return True
    else:
        return False

