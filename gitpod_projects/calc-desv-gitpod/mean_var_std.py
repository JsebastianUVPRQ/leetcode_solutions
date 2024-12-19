import numpy as np


def calculate(input_list):

    """
    Calcula la media, varianza, desviación estándar, máximo, mínimo y suma
    de una matriz 3x3 generada a partir de una lista de 9 números.

    Parámetros:
    input_list (list): Lista de 9 números.

    Retorna:
    dict: Diccionario con los cálculos estadísticos.
    
    Excepciones:
    ValueError: Si la lista no contiene exactamente 9 números.
    """
    if len(input_list) != 9:
        raise ValueError("La lista debe contener nueve números")
    
    # Convertir la lista en una matriz 3x3 de NumPy
    matrix = np.array(input_list).reshape(3, 3)
    
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),  # Media por columna
            matrix.mean(axis=1).tolist(),  # Media por fila
            matrix.mean()                  # Media de todos los elementos
        ],
        'variance': [
            matrix.var(axis=0).tolist(),    # Varianza por columna
            matrix.var(axis=1).tolist(),    # Varianza por fila
            matrix.var()                    # Varianza de todos los elementos
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),     # Desviación estándar por columna
            matrix.std(axis=1).tolist(),     # Desviación estándar por fila
            matrix.std()                     # Desviación estándar de todos los elementos
        ],
        'max': [
            matrix.max(axis=0).tolist(),     # Máximo por columna
            matrix.max(axis=1).tolist(),     # Máximo por fila
            matrix.max()                     # Máximo de todos los elementos
        ],
        'min': [
            matrix.min(axis=0).tolist(),     # Mínimo por columna
            matrix.min(axis=1).tolist(),     # Mínimo por fila
            matrix.min()                     # Mínimo de todos los elementos
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),     # Suma por columna
            matrix.sum(axis=1).tolist(),     # Suma por fila
            matrix.sum()                     # Suma de todos los elementos
        ]
    }
    
    # Convertir todos los valores escalares a listas
    for key in ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']:
        # Asegurar que el tercer elemento (aplanado) sea una lista
        if isinstance(
            calculations[key][2], (int, float, np.integer, np.floating)):
            calculations[key][2] = [calculations[key][2]]
    
    return calculations

