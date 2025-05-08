import csv

class Analizador:
    def __init__(self, archivo_csv):
        """
        Inicializa el analizador con datos del archivo CSV,
        excluyendo registros con la provincia 'ND'.
        """
        self.datos = []
        try:
            try:
                with open(archivo_csv, mode="r", encoding="utf-8") as file:
                    self.datos = self._filtrar_provincias(csv.DictReader(file))
            except UnicodeDecodeError:
                with open(archivo_csv, mode="r", encoding="latin-1") as file:
                    self.datos = self._filtrar_provincias(csv.DictReader(file))
        except Exception as e:
            raise ValueError(f"Error al leer el archivo CSV: {str(e)}")

    def _filtrar_provincias(self, lector):
        """Filtra los registros, excluyendo aquellos cuya provincia sea 'ND'."""
        return [
            fila for fila in lector if fila.get("PROVINCIA", "").strip().upper() != "ND"
        ]

    def ventas_por_provincia(self):
        """
        Retorna un diccionario con las ventas totales por provincia.
        """
        resultado = {}
        for registro in self.datos:
            try:
                provincia = registro["PROVINCIA"]
                venta = float(registro["TOTAL_VENTAS"].replace(",", "."))
                resultado[provincia] = resultado.get(provincia, 0) + venta
            except (KeyError, ValueError) as e:
                print(f"Error procesando registro: {registro} -> {e}")
        return resultado

    def ventas_de_provincia(self, nombre_provincia):
        """
        Retorna las ventas totales de una provincia específica.
        """
        total = 0.0
        for registro in self.datos:
            try:
                if registro["PROVINCIA"].lower() == nombre_provincia.lower():
                    total += float(registro["TOTAL_VENTAS"].replace(",", "."))
            except (KeyError, ValueError) as e:
                print(f"Error procesando registro: {registro} -> {e}")
        return total

    def exportaciones_totales_por_mes(self):
        """
        Retorna un diccionario con las exportaciones totales por mes.
        """
        exportaciones_por_mes = {}
        for fila in self.datos:
            try:
                mes = fila["MES"]
                exportacion = float(fila["EXPORTACIONES"].replace(",", "."))
                exportaciones_por_mes[mes] = exportaciones_por_mes.get(mes, 0) + exportacion
            except (KeyError, ValueError) as e:
                print(f"Error procesando fila: {fila} -> {e}")
        return exportaciones_por_mes

    def diferencia_ventas_exportaciones_por_provincia(self):
        """
        Retorna un diccionario con la diferencia entre ventas totales y exportaciones por provincia.
        """
        resultado = {}
        for registro in self.datos:
            try:
                provincia = registro["PROVINCIA"]
                ventas = float(registro["TOTAL_VENTAS"].replace(",", "."))
                exportaciones = float(registro["EXPORTACIONES"].replace(",", "."))

                if provincia not in resultado:
                    resultado[provincia] = {"ventas": 0.0, "exportaciones": 0.0}

                resultado[provincia]["ventas"] += ventas
                resultado[provincia]["exportaciones"] += exportaciones

            except (KeyError, ValueError) as e:
                print(f"Error procesando registro: {registro} -> {e}")

        # Calcular diferencia final por provincia
        diferencia_por_provincia = {
            provincia: round(info["ventas"] - info["exportaciones"], 2)
            for provincia, info in resultado.items()
        }

        return diferencia_por_provincia
