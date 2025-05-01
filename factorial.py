def factorial_iterativo(n):
    """
    Calcula el factorial de un número de forma iterativa.
    
    Parámetros:
        n (int): El número para calcular el factorial. Debe ser un entero no negativo.
    
    Retorna:
        int: El factorial de n.
    
    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def factorial_recursivo(n):
    """
    Calcula el factorial de un número de forma recursiva.
    
    Parámetros:
        n (int): El número para calcular el factorial. Debe ser un entero no negativo.
    
    Retorna:
        int: El factorial de n.
    
    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")
    if n == 0:
        return 1
    return n * factorial_recursivo(n - 1)
