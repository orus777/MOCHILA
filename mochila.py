def mochila(valor, xx, yy):
    """
      valor: una lista de valores de los elementos
      xx: Una lista de pesos de los artículos
      yy: El peso máximo que puede soportar la mochila
      retorno: El valor máximo que se puede obtener seleccionando elementos de la lista dada de valores y pesos
    """
    n = len(valor)
    # Cree una lista 2D de tamaño (n+1)x(yy+1) para almacenar la tabla de programación dinámica
    dp = [[0 for x in range(yy + 1)] for y in range(n + 1)]

    # Rellenar la tabla de forma ascendente
    for i in range(n + 1):
        for yy in range(yy + 1):
            if i == 0 or yy == 0:
                # Caso base: si ningún artículo o peso máximo es 0, entonces el valor es 0
                dp[i][yy] = 0
            elif xx[i - 1] <= yy:
                # Si el peso del elemento actual es menor o igual que el peso actual, entonces tenemos dos opciones:
                # 1. Incluir el artículo y pasar al siguiente artículo con un peso reducido
                # 2. No incluir el artículo y pasar al siguiente artículo con el mismo peso
                dp[i][yy] = max(valor[i - 1] + dp[i - 1][yy - xx[i - 1]], dp[i - 1][yy])
            else:
                # Si el peso del artículo actual es mayor que el peso actual, entonces no podemos incluir el artículo
                # Entonces, pasamos al siguiente elemento con el mismo peso
                dp[i][yy] = dp[i - 1][yy]

    return dp[n][yy]


#Ejemplo de uso:
valor = [90, 50, 500]
xx = [30, 40, 50]
yy = 100
print("el resultado con las variables asignadas es: ")
print(mochila(valor, xx, yy))



"""
    
La función mochila()toma en tres parámetros:

valor: Una lista de valores de los artículos.
xx: Una lista de pesos de los artículos.
yy: El peso máximo que puede soportar la mochila
La función comienza inicializando una lista 2D dode tamaño (n+1)x(yy+1) para almacenar la tabla de programación dinámica. n es el número de artículos en el problema de la mochila. Luego, la función llena la tabla de forma ascendente, comenzando desde los casos base, cuando ningún artículo o peso máximo es 0, entonces el valor es 0.

Cuando el peso del elemento actual es menor o igual que el peso actual, tenemos dos opciones:

Incluir el artículo y pasar al siguiente artículo con un peso reducido
No incluir el artículo y pasar al siguiente artículo con el mismo peso
De lo contrario, cuando el peso del elemento actual es mayor que el peso actual, no podemos incluir el elemento, por lo que pasamos al siguiente elemento con el mismo peso.

Finalmente, la función devuelve el valor máximo que se puede obtener seleccionando elementos de la lista de valores y pesos dada, donde el peso máximo permitido es "yy".

En el ejemplo de uso, la función se llama con la siguiente entrada: valor = [60, 100, 120] xx = [10, 20, 30] yy = 50 La función devuelve un valor de 220, el valor máximo que se puede obtener seleccionando elementos de la lista dada de valores y pesos, donde el peso máximo permitido es "yy" = 50.
    """