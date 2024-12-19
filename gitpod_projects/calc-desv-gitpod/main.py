# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

print(mean_var_std.calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))

# Run unit tests automatically
main(module='test_module', exit=False)

from mean_var_std import calculate

def main():
    # Lista de 9 números
    input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    try:
        # Calcular estadísticas
        result = calculate(input_list)
        
        # Imprimir el resultado
        print("Resultados de los cálculos estadísticos:")
        for key, value in result.items():
            print(f"{key}: {value}")
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()

# -----