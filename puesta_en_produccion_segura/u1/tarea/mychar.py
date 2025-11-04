def cadena_mas_larga(lista_cadenas):
	if not lista_cadenas:
		return ""

	# Encontrar la longitud máxima
	longitud_max = max(len(cadena) for cadena in lista_cadenas)

	# Filtrar las cadenas que tienen la longitud máxima
	cadenas_maximas = [
		cadena 
		for cadena in lista_cadenas 
		if len(cadena) == longitud_max
	]

	# Devolver la primera cadena en orden alfabético
	return sorted(cadenas_maximas)[0]

def main():
	palabras = []
	for _ in range(5):
		palabra = input("Introduce una palabra: ")
		palabras.append(palabra)

	resultado = cadena_mas_larga(palabras)
	print("La cadena más larga es:", resultado)

if __name__ == "__main__":
	main()
