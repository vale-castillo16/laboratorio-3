from src.procesador import Analizador
import os

def main():
    # Ruta del archivo CSV
    ruta_csv = os.path.join('data', 'sri_ventas_2024.csv')

    # Crear instancia del analizador
    try:
        analizador = Analizador(ruta_csv)
    except ValueError as e:
        print(f"Error al cargar el archivo: {e}")
        return

    # Ventas totales por provincia
    print("\n📊 Ventas totales por provincia:")
    ventas = analizador.ventas_por_provincia()
    for provincia, total in ventas.items():
        print(f"\t{provincia}: ${total:,.2f}")

    # Consulta de ventas para una provincia específica
    print("\n🔍 Consulta de ventas por provincia")
    provincia = input("Ingrese el nombre de una provincia: ").strip()
    total_ventas = analizador.ventas_de_provincia(provincia)
    
    if total_ventas > 0:
        print(f"\tVentas de {provincia}: ${total_ventas:,.2f}")
    else:
        print(f"\tNo se encontraron registros para la provincia: {provincia}")

    # Exportaciones totales por mes
    print("\n🌐 Exportaciones totales por mes:")
    exportaciones = analizador.exportaciones_totales_por_mes()
    for mes, total in sorted(exportaciones.items()):
        print(f"\t{mes}: ${total:,.2f}")

    # Diferencia entre ventas y exportaciones por provincia
    print("\n📉 Diferencia entre ventas y exportaciones por provincia:")
    diferencias = analizador.diferencia_ventas_exportaciones_por_provincia()
    for provincia, diferencia in diferencias.items():
        print(f"\t{provincia}: ${diferencia:,.2f}")

if __name__ == "__main__":
    main()
