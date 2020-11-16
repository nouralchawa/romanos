import validation

simbolos = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
tipo_5 = ('V', 'D', 'L')
tipo_1 = ('I', 'X', 'C', 'M')


def romano_a_entero(romano):

    suma = 0

    for simbolo in romano:
        
        if isinstance(romano, str) and romano.upper() in simbolos:
            suma = suma + simbolos[romano.upper()]
        elif isinstance(romano, str):
            raise ValueError (f"símbolo {romano} no permitido")
        else:
            raise ValueError (f"parámetro {romano} debe ser un string")
    return suma


def conv_rom_a_ent(numero):

    if validation.comprobacion_cuatro_caracteres(numero):
        print ("Introducción de número incorrecta")
        return
    
    if validation.comprobacion_vld(numero):
        print ("Introducción de número incorrecta")
        return

    if validation.restaInvalid(numero):
        print ("Introducción de número incorrecta")
        return

    resultado = 0

    for i in range(len(numero)):

        if i < len(numero)-1:

            izq = romano_a_entero(numero[i])
            dch = romano_a_entero(numero[i+1])

            if izq >= dch :
                resultado = resultado + izq
            else:
                resultado = resultado - izq
        
        else:

            resultado = resultado + romano_a_entero(numero[i])
    
    return resultado
