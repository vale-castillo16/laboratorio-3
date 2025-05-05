from src.procesador import Analizador
import os

def main():
    ruta_csv = os.path.join('data', 'sri_ventas_2024.csv')
    analizador = Analizador(ruta_csv)

    print("Ventas totales por provincia:")
    ventas = analizador.ventas_por_provincia()
    for provincia, total in ventas.items():
        print(f"\t{provincia}: ${total:.2f}")

    print("Compras para una provincia")
    provincia = input ("\nIngrese el nombre de una provincia: ")
    
    try:
        ventas = analizador.ventas_de_provincia(provincia)
        print(f"\tVentas de {provincia}: ${ventas:,.2f}")
    except KeyError as e:
        print(e)
    
    exportaciones = analizador.exportaciones_totales_por_mes()
    for mes, total in exportaciones.items():
        print(f"\t{mes}: ${total:,.2f}")

if __name__ == "__main__":
    main()
