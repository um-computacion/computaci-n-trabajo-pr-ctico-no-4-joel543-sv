def aplanar(lista):
    """
    Aplana una lista anidada de forma recursiva.
    
    Parámetros:
        lista (list): Lista potencialmente anidada que se desea aplanar.
    
    Retorna:
        list: Una lista plana con todos los elementos originales.
    """
    if not isinstance(lista, list):  # Caso base: no es una lista
        return [lista]
    
    resultado = []
    for elemento in lista:
        resultado.extend(aplanar(elemento))  # Llamada recursiva
    return resultado
