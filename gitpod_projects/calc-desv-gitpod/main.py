# This entrypoint file to be used in development. Start by reading README.md
from mean_var_std import calculate
from unittest import main


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