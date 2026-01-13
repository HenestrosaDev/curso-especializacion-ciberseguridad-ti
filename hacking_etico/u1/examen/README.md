# EXAMEN Unidad 1: Conceptos y herramientas para la detección de vulnerabilidades

>[!NOTE]
>Este examen está incluido en la baraja de Anki disponible en la raíz del repositorio (`anki.apkg`).

[Test de Daypo](https://www.daypo.com/he-1.html)

## Preguntas y respuestas

1. Indica cuál de las siguientes herramientas no es un proxy de interceptación:
	- [x] Shellter.
	- [ ] Burp.
	- [ ] ZAP.
	- [ ] Echo Mirage.

2. Indica cuál de las siguientes afirmaciones es correcta para una auditoría con pruebas de caja blanca:
	- [ ] En este tipo de pruebas si se contempla que puedes partir de uno, varios usuarios iniciales o, que por el contrario, no dispongas de ningún usuario al iniciar las pruebas.
	- [x] Se puede disponer del código fuente del aplicativo a auditar para poder localizar vulnerabilidades en código.
	- [ ] Las pruebas se realizan sin ningún tipo de conocimiento sobre la aplicación o infraestructura a auditar.
	- [ ] No se dispone de tecnologías utilizadas, frameworks o lenguajes de programación utilizados, diagramas de red o de flujo, etc

3. ¿Cuál de las siguientes labores de la fase de Pre-engagement NO es una labor organizativa?
	- [ ] Designar personas de contacto durante el tiempo de auditoría.
	- [x] Establecer un canal de comunicación para las incidencias graves.
	- [ ] Identificar el entorno y enfoque de las pruebas.
	- [ ] Delimitar el alcance de la auditoría

4. Para poder inspeccionar los datos transmitidos y recibidos por una interfaz de red a bajo nivel, ¿qué herramienta de las siguientes hay que utilizar?
	- [ ] Nmap.
	- [ ] Netdiscover.
	- [x] Wireshark.
	- [ ] Arpscan.

5. La herramienta nmap puede utilizarse para realizar un escaneo de vulnerabilidades. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

6. Indica cuál de las siguientes herramientas se utilizan para realizar técnicas de fuerza bruta de credenciales:
	- [ ] Wireshark
	- [x] Hydra
	- [ ] goPhish
	- [ ] Echo mirage

7. ¿Cuál es la afirmación más correcta para definir un ciberdelincuente/cibercriminal?
	- [x] Persona con altas capacidades técnicas en seguridad con fines lucrativos utilizando los fallos de seguridad localizados.
	- [ ] Persona con altas capacidades técnicas en seguridad con fines sociales, ecológicos, humanitarios o que tenga repercusión en la defensa de los derechos humanos.
	- [ ] Experto de las tecnologías de comunicación e información que utiliza sus conocimientos técnicos para encontrar y resolver un problema concreto relacionado con la seguridad de la información.
	- [ ] Persona con altas capacidades técnicas.

8. Durante la presentación de resultados únicamente se presentan los resultados de la auditoría, pero no se resuelven dudas ni se dan recomendaciones para solventar las vulnerabilidades. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

9. ¿Cuál de las siguientes herramientas se utilizan en un Reconocimiento pasivo?
	- [ ] Dig
	- [x] Shodan
	- [ ] Snmpwalk
	- [ ] Nmap

10. La herramienta msfvenom se utiliza para generar payloads y shellcodes. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

11. En las pruebas de caja negra nunca se proporcionan usuarios de acceso al activo a auditar. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

12. ¿Cuáles son los tres pilares de la seguridad de la información?
	- [x] Confidencialidad, integridad y disponibilidad.
	- [ ] Confidencialidad, integridad y seguridad.
	- [ ] Confidencialidad, identidad y disponibilidad.
	- [ ] Responsabilidad, integridad y disponibilidad.

13. Indica cuál de las siguientes opciones es una afirmación correcta para la Fase de Explotación:
	- [x] El objetivo es lograr un primer acceso o de privilegios en los activos.
	- [ ] Se utilizan técnicas para poder aumentar el nivel de privilegios en este sistema.
	- [ ] Se detectan vulnerabilidades que puedan existir en los sistemas y servicios
	- [ ] Se recopila información acerca de los activos a auditar.

14. ¿Cuáles son las características del principio de integridad?
	- [x] Requiere que la información se mantenga inalterada ante incidentes o accesos malintencionados.
	- [ ] Requiere que el sistema informático se mantenga accesible sin sufrir ninguna degradación o interrupción en el servicio.
	- [ ] Requiere que no haya malas intenciones en el acceso a los activos.
	- [ ] Requiere que la información sea accesible únicamente a las personas que se encuentran autorizadas.

15. Las herramientas de tipo keylogger se ejecutan en una máquina comprometida para capturar todas las pulsaciones de teclado. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

16. ¿Qué es el estándar CVSS?
	- [ ] Un framework de trabajo que nos indica el tipo de vulnerabilidades a comprobar en una auditoría.
	- [ ] Un estándar para medir la superficie de ataque.
	- [ ] Un estándar de calidad.
	- [x] Un estándar para la medir la criticidad de una vulnerabilidad.

17. En las auditorías manuales NO se pueden utilizar herramientas automáticas. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

18. Indica cuál de las siguientes opciones NO pertenece a la Fase de "Seguimiento de las pruebas":
	- [x] Se comunicarán todas las vulnerabilidades detectadas y se procederá al cierre de la auditoría.
	- [ ] Se decidirá en qué activos o secciones incrementar el esfuerzo en las próximas semanas.
	- [ ] Se comunicarán los problemas que pudieran haber surgido desde la reunión anterior.
	- [ ] Se comunicarán al cliente los hallazgos localizados desde la reunión anterior.

19. ¿Cuál es la definición del término "vulnerabilidad"?
	- [ ] Es un evento que puede causar un incidente de seguridad en una empresa u organización produciendo pérdidas o daños potenciales en sus activos.
	- [ ] Es un objeto o recurso de valor (tangible o intangible) empleado en una empresa u organización cuya pérdida o daño constituiría un riesgo para la organización.
	- [ ] Es un activo que puede disponer de una o varias amenazas.
	- [x] Es una debilidad que puede ser explotada con la materialización de una o varias amenazas a un activo.

20. Indica cuál de las siguientes afirmaciones es correcta:
	- [ ] Una auditoría que haga uso de pruebas automáticas va a localizar las mismas vulnerabilidades que se localizarían en una auditoría con pruebas manuales.
	- [x] El objetivo de los test de intrusión es llegar a comprometer un sistema a través de una vulnerabilidad.
	- [ ] Las auditorías de tipo automático no generan muchos falsos positivos.
	- [ ] En los test de intrusión únicamente se confirman vulnerabilidades.

21. ¿Qué es una vulnerabilidad de tipo 0-Day?
	- [ ] Una vulnerabilidad que no tiene ningún tipo de impacto ni riesgo.
	- [x] Una vulnerabilidad que no es pública.
	- [ ] Una vulnerabilidad publica.
	- [ ] Una vulnerabilidad que no existe.

22. ¿En qué portal podemos buscar exploits específicos para una versión de software en concreto?
	- [ ] LinkedIn.
	- [ ] Censys.
	- [ ] Shodan.
	- [x] Exploit-db.

23. ¿Qué es la dark web?
	- [ ] Contenido utilizado por los ciberdelincuentes pero que se encuentra disponible de manera pública en internet.
	- [ ] Contenido que se encuentra disponible de manera pública en internet.
	- [x] Redes privadas utilizadas por los ciberdelincuentes para ofrecer sus servicios, vender información previamente robada, vulnerabilidades no reportadas a los fabricantes.
	- [ ] Todo el contenido privado que no se encuentra a disposición del público en general.

24. Indica cuál de las siguientes herramientas es utilizada para automatizar la búsqueda de vectores de elevación de privilegios en sistemas Linux:
	- [x] LinPEAS.
	- [ ] PrivescCheck.
	- [ ] WinPeas.
	- [ ] LinescCheck.

25. Indica cuál de las siguientes afirmaciones NO es correcta para una auditoría de tipo "Test de intrusión":
	- [ ] Tienen como objetivo comprobar el grado real de amenaza que podría producirse al aprovecharse de las vulnerabilidades localizadas durante la auditoría y verificar el impacto específico que tendrían sobre la compañía.
	- [ ] Las pruebas se realizan por un auditor de manera manual apoyándose en herramientas específicas. También se contempla el uso de sistemas secundarios para ciertos tipos de pruebas.
	- [ ] Tratan de comprometer el sistema remoto a través de una vulnerabilidad identificada.
	- [x] Debido a la forma en la que se detectan las vulnerabilidades, se producen muchos falsos positivos.

26. ¿Qué tipo de información podemos recopilar en las redes sociales?
	- [x] Averiguar tecnologías utilizadas en la compañía.
	- [ ] Direccionamiento IP y servicios expuestos en el perímetro de la empresa.
	- [ ] Activos pertenecientes a las empresas.
	- [ ] Averiguar credenciales de usuarios.