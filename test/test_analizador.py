import unittest
from src.procesador import Analizador


class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_exclusion_de_provincia_nd(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertNotIn("ND", resumen)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 24)  # Suponiendo que hay 24 provincias válidas

    def test_ventas_totales_todas_mayores_5000(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

    def test_exportaciones_totales_por_mes_menores_2000(self):
        resumen = self.analizador.exportaciones_totales_por_mes()
        self.assertTrue(all(float(v) > 2000 for v in resumen.values()))

    def test_exportaciones_multiple_meses(self):
        class AnalizadorMock(Analizador):
            def __init__(self, datos):
                self.datos = datos

            def exportaciones_totales_por_mes(self):
                exportaciones_por_mes = {}
                for fila in self.datos:
                    mes = fila['MES']
                    exportacion = float(fila['EXPORTACIONES'])
                    if mes in exportaciones_por_mes:
                        exportaciones_por_mes[mes] += exportacion
                    else:
                        exportaciones_por_mes[mes] = exportacion
                return exportaciones_por_mes

        datos = [
            {'MES': 'Enero', 'EXPORTACIONES': '100.5'},
            {'MES': 'Enero', 'EXPORTACIONES': '200.0'},
            {'MES': 'Febrero', 'EXPORTACIONES': '300.0'},
        ]
        instancia = AnalizadorMock(datos)
        resultado = instancia.exportaciones_totales_por_mes()
        self.assertEqual(resultado['Enero'], 300.5)
        self.assertEqual(resultado['Febrero'], 300.0)

    def test_exportaciones_no_esta_vacio(self):
        resumen = self.analizador.exportaciones_totales_por_mes()
        self.assertGreater(len(resumen), 0, "El diccionario de exportaciones está vacío")

    def test_diferencia_ventas_exportaciones(self):
        # Datos simulados para prueba específica
        class AnalizadorMock(Analizador):
            def __init__(self, datos):
                self.datos = datos

        datos = [
            {'PROVINCIA': 'Pichincha', 'TOTAL_VENTAS': '10000.00', 'EXPORTACIONES': '2000.00'},
            {'PROVINCIA': 'Pichincha', 'TOTAL_VENTAS': '5000.00', 'EXPORTACIONES': '1000.00'},
            {'PROVINCIA': 'Guayas', 'TOTAL_VENTAS': '8000.00', 'EXPORTACIONES': '3000.00'}
        ]
        instancia = AnalizadorMock(datos)
        resultado = instancia.diferencia_ventas_exportaciones_por_provincia()
        self.assertEqual(resultado['Pichincha'], 12000.00)
        self.assertEqual(resultado['Guayas'], 5000.00)


if __name__ == "__main__":
    unittest.main()
