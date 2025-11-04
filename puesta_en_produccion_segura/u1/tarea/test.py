import unittest
from mychar import cadena_mas_larga

class Test(unittest.TestCase):
	def test_cadena_mas_larga(self):
		# Caso básico
		self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "dddd")

		# Caso con cadenas de la misma longitud
		self.assertEqual(cadena_mas_larga(["abc", "def", "ghi"]), "abc")

		# Caso con lista vacía
		self.assertEqual(cadena_mas_larga([]), "")

		# Caso con una sola cadena
		self.assertEqual(cadena_mas_larga(["solo"]), "solo")

		# Caso con múltiples cadenas de diferentes longitudes
		self.assertEqual(cadena_mas_larga(["cort", "largo", "muylargo", "extralargo"]), "extralargo")

		# Caso con cadenas que incluyen espacios
		self.assertEqual(cadena_mas_larga(["a b", "ab c", "abc d"]), "abc d")

		# Caso con cadenas numéricas
		self.assertEqual(cadena_mas_larga(["123", "1234", "12"]), "1234")

		# Caso con caracteres especiales
		self.assertEqual(cadena_mas_larga(["!@#", "$%^&*", "()*+"]), "$%^&*")

if __name__ == "__main__":
	unittest.main()
