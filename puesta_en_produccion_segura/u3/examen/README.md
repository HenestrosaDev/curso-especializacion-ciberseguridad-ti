# EXAMEN Unidad 3: Detección y corrección de vulnerabilidades de aplicaciones web

>[!NOTE]
>Este examen está incluido en la baraja de Anki disponible en la raíz del repositorio (`anki.apkg`).

[Test de Daypo](https://www.daypo.com/ps-03.html)

## Preguntas y respuestas

1. ¿Qué es la autorización?
	- [ ] Proceso de gestión de los derechos de una base de datos.
	- [x] Proceso de asignación de permisos que sucede después de la autenticación.
	- [ ] Proceso de logado de un usuario en un sistema.
	- [ ] Conjunto de instrucciones que se lleva a cabo durante el login del usuario.

2. ¿Qué necesita un WAF cuando lo instalamos?
	- [ ] Un administrador de red y otro de seguridad.
	- [ ] Software especifico.
	- [ ] Cambios en el aplicativo.
	- [x] Un tiempo para aprender sobre el aplicativo, los datos y usuarios.

3. Un WAF nos puede ayudar a detectar y bloquear ataques de botnets. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

4. Los formularios mal configurados son uno de los vectores de entrada de los aplicativos web. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

5. ¿De qué manera podemos proteger las contraseñas almacenadas?
	- [ ] Almacenándolas en texto claro.
	- [ ] De ninguna manera.
	- [x] Mediante cifrados y funciones hash.
	- [ ] En la práctica no es viable.

6. El proceso de autenticación Basic Auth es ideal cuando:
	- [x] Cuando no se va a manejar datos sensibles ó que tengan muchas restricciones de uso.
	- [ ] Cuando trabajamos con datos que son de carácter personal.
	- [ ] Cuando no trabajamos ni con aplicativos REST o SOAP.
	- [ ] Cuando trabajemos en distintas capas de seguridad.

7. OWASP ofrece un Top de riesgos para móviles y para web. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

8. ¿Qué tipos de funciones Hash se recomienda usar?
	- [ ] md5.
	- [ ] Diffie-Hellman.
	- [x] SHA.
	- [ ] RSA.

9. ¿Es recomendable almacenar contraseñas y datos personales por parte de las aplicaciones?
	- [ ] Sí, según el tipo de dato manejado por la aplicación.
	- [x] Depende, lo ideal es que la aplicación guarde unicamente los datos realmente necesarios y en caso de ser datos relevantes los securice de alguna manera.
	- [ ] No.
	- [ ] Sí, siempre.

10. ¿Qué tipo de ataques se considera de tipo Client Side Injection?
	- [ ] Brute Forcing.
	- [x] Session Hijacking.
	- [ ] SQl Transversal.
	- [ ] SQL Inyection.

11. ¿Qué cambio suele ser habitual para configurar un WAF?
	- [ ] Cambiar los CAPTCHAs.
	- [x] Cambiar registros DNS.
	- [ ] Cambiar el código fuente de nuestro aplicativo.
	- [ ] Avisar al administrador de red.

12. El TOP10 de OWASP tiene el objetivo de identificar riesgos. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

13. La seguridad del código fuente es lo único que interviene en hacer un aplicativo seguro. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

14. Podemos ayudar a la seguridad del software añadiendo contramedidas tanto a nivel de sistemas como de software adicional como CAPTCHAs. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

15. Un WAF no es más que un Firewall con más capacidades. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

16. ¿Qué significa HSTS?
	- [ ] High Security Transport Standard.
	- [x] HTTP Strict-Transport-Security.
	- [ ] High Standard HTTP Security.
	- [ ] High Standard Transport Security.

17. ¿Cuál de los siguientes NO es un elemento clásico de un formulario?
	- [ ] Botón.
	- [x] Reconocimiento facial.
	- [ ] Campo de texto.
	- [ ] Checkbox.

18. CSP es una contramedida para evitar ataques como los de inyección de código. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

19. ¿De qué lado se suele producir los ataques de robo de sesión?
	- [ ] De ninguno de los anteriores.
	- [ ] Del lado del aplicativo.
	- [x] Del lado del cliente.
	- [ ] Del lado del servidor.

20. ¿Cuál de las siguientes se considera una fundación sin ánimo de lucro que ayuda en identificar riesgos y adoptar medidas al respecto?
	- [ ] OVBA.
	- [x] OWASP.
	- [ ] VBSA.
	- [ ] OSINT.

21. Para securizar un aplicativo deberemos controlar la entrada de datos en los formularios. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

22. ¿Qué significa WAF?
	- [ ] Web Advanced Firewall.
	- [ ] Web Advanced Forwarder.
	- [x] Web Application Firewall.
	- [ ] Wave App Firewall.

23. Los niveles de aplicación definidos en el ASVS tienen en cuenta el dato manejado y el entorno de la aplicación. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

24. Los WAFs son entorno de cloud. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

25. ¿Qué versión de OAuth es la más utilizada?
	- [x] v2.
	- [ ] v8.
	- [ ] v3.
	- [ ] v6.

26. Debemos de apoyarnos en la lista de OWASP para entender los riesgos que puede sufrir nuestro software. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

27. Las aplicaciones de nivel 1 del ASVS no tienen que cumplir ningún requisito. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso