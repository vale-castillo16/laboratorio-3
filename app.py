from src.procesador import Analizador
import os

def main():
    ruta_csv = os.path.join('data', 'sri_ventas_2024.csv')
    analizador = Analizador(ruta_csv)

    print("Ventas totales por provincia:")
    ventas = analizador.ventas_por_provincia()
    for provincia, total in ventas.items():
        print(f"\t{provincia}: ${total:.2f}")
        
    

if __name__ == "__main__":
    main()
