class Solution1:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window 
    substring
    of s such that every character in t (including duplicates) is included in the window. 
    If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.
    -------------------------------------------------"""
    def min_windows(self, s: str, t: str) -> str:
        ''''
        Time complexity: O(m+n)
        create a dictionary to store the count of each character in t
        '''
        t_count = {}
        for char in t:
            if char in t_count:
                t_count[char] += 1
            else:
                t_count[char] = 1
        # if we print t_count, we get {'A': 1, 'B': 1, 'C': 1} and f
        
        # create a dictionary to store the count of each character in the current window
        window_count = {}
        for char in t:
            window_count[char] = 0
        # if we print window_count, we get {'A': 0, 'B': 0, 'C': 0} and finally we get {'A': 1, 'B': 1, 'C': 1} because 
        
        
        # initialize the window
        left = 0            # left is the start of the window
        right = 0           # right is the end of the window
        min_window = ""     # initialize min_window with an empty string
        min_length = float('inf')    # initialize min_length with a large value
        required = len(t_count)      # number of unique characters in t
        formed = 0                   # number of characters of t which are present in the current window 
        
        while right < len(s):
            # expand the window
            if s[right] in window_count:        # if the character is in t
                window_count[s[right]] += 1     # increment the count of the character
                if window_count[s[right]] == t_count[s[right]]:   # if the count of the character is equal to the count in t    
                    formed += 1                                   # increment formed      
            # reducir la ventana
            while formed == required:                #condicion del while: si todos los caracteres de t están presentes en la ventana actual
                if right - left + 1 < min_length:    # si la longitud de la ventana actual es menor que la longitud de la ventana mínima
                    min_window = s[left:right+1]     # actualizar como la ventana mínima
                    min_length = right - left + 1    # Ahora, la longitud de la ventana mínima es la longitud de la ventana actual
                if s[left] in window_count:          # s[[]] significa que estamos buscando el valor de la llave s[left] en el diccionario window_count
                    window_count[s[left]] -= 1
                    if window_count[s[left]] < t_count[s[left]]:
                        formed -= 1
                left += 1
            right += 1
        return min_window

# ----------------------EJECUCIÓN-------------------
# Explica a profundidad el algoritmo con sus pormenores
# La lógica comienza por crear un diccionario que almacene la cantidad de veces que aparece cada caracter en la cadena t
# Luego se crea un diccionario para almacenar la cantidad de veces que aparece cada caracter en la ventana actual
# Se inicializa la ventana con left y right en 0, y se inicializan las variables min_window y min_length con valores que
# permitan comparar y encontrar la ventana más pequeña
# Se inicializa la variable required con la longitud del diccionario t_count y formed en 0
# formed es la cantidad de caracteres de t que están presentes en la ventana actual.
# Se itera sobre la cadena s, es decir, se recorre cada caracter de la cadena s
# expandiendo la ventana y actualizando el diccionario window_count. window_count almacena la cantidad de veces que aparece
# Luego se contrae la ventana, actualizando el diccionario window_count y comparando la longitud de la ventana actual
# con la longitud de la ventana mínima
# Finalmente se retorna la ventana mínima
# ----------------------EJECUCIÓN-------------------


# ----------------------TEST-------------------
sol = Solution1()
print(sol.min_windows(s = "ADOBECODEBANC", t = "ABC"))
# output --> "BANC"
# ---------------------------------------------  

# ----------------------COMPLEJIDAD-------------------
# Por qué la complejidad es O(m+n)?
# La complejidad del algoritmo es O(m+n) porque se itera sobre la cadena s y la cadena t, 
# y se realizan operaciones
# de inserción y actualización en los diccionarios t_count y window_count, 
# cuyas longitudes son m y n respectivamente.
#------------------------//----------------------------------------
# Cuál es la complejidad más óptima posible para este problema?
# La complejidad más óptima posible para este problema es O(m+n) porque se debe iterar
# sobre ambas cadenas para encontrar.
# La ventana mínima que contenga todos los caracteres de t.
# El algoritmo actual es óptimo para este problema.
#------------------------//----------------------------------------------------------------------------
# Qué es una ventana?
# Una ventana es un rango de índices de una cadena que contiene todos los caracteres de otra cadena.
# En este problema, se busca encontrar la ventana más pequeña que contenga todos los caracteres de t.
#------------------------//----------------------------------------
# La razón para usar diccionarios como estructura de datos es 
# porque se necesita almacenar la cantidad de veces que aparece
# cada caracter en la cadena t y en la ventana actual. 
# Los diccionarios proporcionan una forma eficiente de realizar esta tarea porque permiten
# acceso y actualización en tiempo constante. Además, los diccionarios son útiles para realizar
# comparaciones y cálculos de forma eficiente, tales como verificar si todos los caracteres de t
# están presentes en la ventana actual y calcular la longitud de la ventana actual.
# ----------------------//-------------------
# Cuáles son las parejas de llaves y valores en cada diccionario?
# Las parejas de llaves y valores en el diccionario t_count son:
# {'A': 1, 'B': 1, 'C': 1}  
# Las parejas de llaves y valores en el diccionario window_count son:
# {'A': 0, 'B': 0, 'C': 0} al inicio y {'A': 1, 'B': 1, 'C': 1} al final
# Las parejas de llaves y valores en el diccionario window_count se actualizan 
# a medida que se expande y contrae la ventana. Por ejemplo, en el caso de la cadena s = "ADOBECODEBANC" y t = "ABC",
# el diccionario window_count se actualiza a {'A': 1, 'B': 1, 'C': 1} cuando la ventana mínima es "BANC".
# la ventana MÍNIMA se obtiene comparando la longitud de la ventana actual con la longitud de la ventana mínima
# Dicha ventana está en la línea 40
# ----------------------//-------------------
# Cuál es el propósito de las variables required y formed?
# La variable required almacena la cantidad de caracteres únicos en la cadena t.
# La variable formed almacena la cantidad de caracteres de t que están presentes en la ventana actual.
# Estas variables se utilizan para verificar si todos los caracteres de t están presentes en la ventana actual.
# ----------------------//-------------------
# two numbers
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
# You can return the answer in any order.

class Solution2:
    def two_sum(self, nums, target):
        '''
        Time complexity: O(n)
        '''
        num_dict = {}
        for i, num in enumerate(nums):
            if target - num in num_dict:
                return [num_dict[target - num], i]
            num_dict[num] = i
        return []

