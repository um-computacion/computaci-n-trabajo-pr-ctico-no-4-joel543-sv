def fibonacci_iterativo(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci de forma iterativa.
    
    Parámetros:
        n (int): La posición en la secuencia de Fibonacci (0 o mayor).
    
    Retorna:
        int: El n-ésimo número de Fibonacci.
    
    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no está definida para números negativos.")
    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursivo(n):
    """
    Calcula el n-ésimo número de la secuencia de Fibonacci de forma recursiva.
    
    Parámetros:
        n (int): La posición en la secuencia de Fibonacci (0 o mayor).
    
    Retorna:
        int: El n-ésimo número de Fibonacci.
    
    Lanza:
        ValueError: Si n es negativo.
    """
    if n < 0:
        raise ValueError("La secuencia de Fibonacci no está definida para números negativos.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
