# TAREA Unidad 1: Prueba de aplicaciones web y para dispositivos móviles

## Índice

- [Caso práctico](#caso-práctico)
- [¿Qué te pedimos que hagas?](#qué-te-pedimos-que-hagas)
	- [Apartado 1: Script](#apartado-1-script)
		- [Crea un script que devuelva la cadena más larga de una lista de cadenas](#crea-un-script-que-devuelva-la-cadena-más-larga-de-una-lista-de-cadenas)
	- [Apartado 2: Testing](#apartado-2-testing)
		- [Crea un programa principal donde definiremos una clase llamada Test donde probaremos nuestro software](#crea-un-programa-principal-donde-definiremos-una-clase-llamada-test-donde-probaremos-nuestro-software)
	- [Apartado 3: Verificación](#apartado-3-verificación)
		- [Ejecuta el programa final y verifica si realmente el programa `mychar.py` se comporta como esperamos](#ejecuta-el-programa-final-y-verifica-si-realmente-el-programa-mycharpy-se-comporta-como-esperamos)
		- [Si el programa que comprueba el código detecta un error, ¿nos reflejará qué dato está esperando y que ha recibido?](#si-el-programa-que-comprueba-el-código-detecta-un-error-nos-reflejará-qué-dato-está-esperando-y-que-ha-recibido)
		- [¿Qué tipo de prueba hemos realizado?](#qué-tipo-de-prueba-hemos-realizado)
- [Resultado](#resultado)
	- [Calificación](#calificación)
	- [Comentarios de retroalimentación y rúbrica](#comentarios-de-retroalimentación-y-rúbrica)

<br>

## Caso práctico

Julián cuando necesita comprobar parte de un código en Python usa la librería incluida por defecto en las distribuciones de Python llamada `unitest`.

Tiene un pequeño programa que solicita por teclado 5 palabras y devuelve la más larga. Para ello crea una pequeña función que recibe una lista de cadenas y devuelve la que tiene mayor longitud.

Para comprobar que todo funciona correctamente, decide hacer un test del software, es decir quiere verificar que una parte del código se comporta de forma esperada, para ello crea un script que importará la librería unittest y comprobará si la función que ha desarrollado como mínimo funciona correctamente para  la lista `["a", "ab", "abc", "dddd", "abcd"]`.

## ¿Qué te pedimos que hagas?

### Apartado 1: Script

#### Crea un script que devuelva la cadena más larga de una lista de cadenas

>[!NOTE]
>Para realizar esta tarea es obligatorio que uses el lenguaje Python 3, por su facilidad y por el gran acceso a librerías de evaluación de software que posee. Si aún no has programado en Python, su inmersión te será sencilla y amigable.

>- Llamaremos a este script `mychar.py`.
>- Deberías de crear un programa con su estructura completa
>- Dentro de este programa crearemos una función llamada `cadena_mas_larga` que reciba una lista de cadenas y devuelva la cadena más larga de la lista.  Si dos o más cadenas tienen la misma longitud máxima, la función debe devolver la primera de ellas si las ordenamos alfabéticamente desde la A a la Z. Si la lista está vacía, la función debe devolver una cadena vacía ("").
>- En el mismo fichero `mychar.py`, crea un programa que solicite al usuario 5 palabras y devuelva la más larga usando la función anterior.

```python
def cadena_mas_larga(lista_cadenas):
	if not lista_cadenas:
		return ""
	
	# Encontrar la longitud máxima
	longitud_max = max(len(cadena) for cadena in lista_cadenas)
	
	# Filtrar las cadenas que tienen la longitud máxima
	cadenas_maximas = [
		cadena 
		for cadena in lista_cadenas 
		if len(cadena) == long_maxima
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
```

---

### Apartado 2: Testing

#### Crea un programa principal donde definiremos una clase llamada `Test` donde probaremos nuestro software

>[!NOTE]
>Importaremos la librería de texto de software. En este caso, `unittest`.
>Crearemos nuestra clase (del tipo `unittest.TextCase`).
>Dentro de esta clase, definiremos, al menos, una función para reflejar el tipo de testeo que vamos a realizar. En este caso, tu objetivo es verificar que, para la lista `["a", "ab", "abc", "dddd", "abcd"]`, la función devuelva `"abcd"`.
>No olvides incluir todas aquellas comprobaciones que creas necesarias para testear que la función `cadena_mas_larga` funciona correctamente. No des por sentado que el programador puede hacer un "buen uso" de ella. Prepárala para "lo peor".

```python
import unittest
from mychar import cadena_mas_larga

class Test(unittest.TestCase):
	def test_cadena_mas_larga(self):
		# Caso básico
		self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "abcd")

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
```

---

### Apartado 3: Verificación

#### Ejecuta el programa final y verifica si realmente el programa `mychar.py` se comporta como esperamos

Procedemos a ejecutar el script para comprobar que funciona correctamente:

![capturas/3-1.png]

Como podemos apreciar, la cadena más larga es, efectivamente, **extralargo**.

A continuación, ejecutamos los tests para comprobar si hay algún caso que falle:

![capturas/3-2.png]

De la misma forma, los tests funcionan correctamente, lo cual es el comportamiento esperado.

#### Si el programa que comprueba el código detecta un error, ¿nos reflejará qué dato está esperando y que ha recibido?

Vamos a modificar el archivo provisto en el apartado 2 para comprobar si se cumple lo que plantea el enunciado. En este caso, vamos a modificar el siguiente caso:

```python
# Caso con una sola cadena
self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "abcd")
```

Por este otro, el cual es **erróneo**:

```python
self.assertEqual(cadena_mas_larga(["a", "ab", "abc", "dddd", "abcd"]), "dddd")
```

Ejecutamos el programa con el cambio realizado:

![capturas/3-3.png]

Como podemos apreciar, el programa de testing nos detecta que hay un error en los tests. Refleja el dato que está esperando (`Expected: 'abcd'`) y el dato que ha recibido (`Received: 'dddd'`).

#### ¿Qué tipo de prueba hemos realizado?

Se trata de un test unitario, el cual es una pequeña pieza de código diseñada para probar de manera independiente una función o método específico de una aplicación (en este caso, `cadena_mas_larga`). 

Los tests unitarios ayudan a verificar que cada componente del código funcione correctamente y que los cambios futuros no introduzcan errores.

---

## Resultado

### Calificación

- / 10,00

### Comentarios de retroalimentación y rúbrica

![](rubrica.png)