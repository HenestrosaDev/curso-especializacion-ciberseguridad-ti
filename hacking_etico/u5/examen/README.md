# EXAMEN Unidad 5: Ataque y defensa en entorno de pruebas de aplicaciones web

>[!NOTE]
>Este examen está incluido en la baraja de Anki disponible en la raíz del repositorio (`anki.apkg`).

[Test de Daypo](https://www.daypo.com/he-5.html)

## Preguntas y respuestas

1. ¿Cuáles de las siguientes afirmaciones correspondientes con los atributos de las cookies es correcta?
	- [ ] El atributo "domain" indica que únicamente es posible conectarte al aplicativo web si te encuentras situado en la red interna de la oficina.
	- [x] El atributo "HttpOnly" especifica que la cookie no puede ser consultada o transmitida desde scripts de cliente (como JavaScript).
	- [x] El atributo "secure" fuerza al navegador del usuario a transmitir la cookie sólo mediante canales cifrados HTTPS.
	- [ ] El atributo "Path" indica la ruta actual a la que se accede en cada momento.

2. ¿Cuál es la función del Modelo en la arquitectura Modelo Vista controlador?
	- [ ] Realiza las operaciones lógicas de la aplicación, se apoya en el código del aplicativo para esta tarea.
	- [x] Gestiona y mantiene los datos de la aplicación, se apoya en la Base de Datos para esta tarea.
	- [ ] Es la representación visual de los datos y como son presentados al cliente.
	- [ ] Recoger y gestionar los datos de los usuarios para que sean tratados.

3. ¿Qué definición se ajusta más para describir las vulnerabilidades "referencias inseguras a objetos de manera directa - IDOR"?
	- [x] Un atacante puede acceder a información de otro usuario.
	- [ ] Un atacante puede modificar objetos del Sistema Operativo.
	- [ ] Un atacante puede modificar el comportamiento del servidor web.
	- [ ] Un atacante puede acceder a información interna del Sistema Operativo.

4. En un aplicativo, la capa del controlador es con la que interactúa un usuario. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

5. El atributo de las cookies "HttpOnly" disminuye el riesgo en caso de localizar una vulnerabilidad de tipo Cross Site Scripting. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

6. Indica cuáles de las siguientes opciones se corresponden con las características más importantes que presenta un proxy de interceptación HTTP:
	- [x] Interceptan toda la comunicación entre un navegador y el aplicativo web alojado en el servidor. Para ello se sitúan en medio de la comunicación.
	- [x] Permiten modificar la petición HTTP realizada por el navegador antes de ser enviada al servidor.
	- [x] Permiten modificar la respuesta HTTP realizada por el servidor antes de ser interpretada por el navegador.
	- [ ] Permiten conocer si un determinado usuario existe o no.

7. Indica cuál de las siguientes afirmaciones NO es correcta a la hora de referirnos a una vulnerabilidad de Cross Site Scripting Almacenado:
	- [x] Tiene un valor CVSS más bajo que una vulnerabilidad de tipo Cross Site Scripting Reflejado.
	- [ ] El código inyectado se almacena en el aplicativo Web vulnerable.
	- [ ] El usuario del aplicativo web ejecutara el código inyectado cuando acceda visualice la información almacenada por el atacante.
	- [ ] Se produce por una mala validación de los datos de entrada (la aplicación no elimina caracteres especiales)

8. Indica cuáles de estas vulnerabilidades son vulnerabilidades que afectan al cliente de un aplicativo web:
	- [ ] Escalada de privilegios.
	- [x] Cross Site Scripting almacenado.
	- [x] HTTP Splitting.

9. La vulnerabilidad de Cross Site Scripting Almacenado se considera una vulnerabilidad persistente. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

10. El proxy de interceptación web ZAProxy dispone de una versión web y de una versión de pago. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

11. Indica cuáles de estas vulnerabilidades son vulnerabilidades que afectan al servidor de un aplicativo web:
	- [x] Inyección remota de código.
	- [x] Denegación de servicio.
	- [ ] Bloqueo de la cuenta de usuario.
	- [ ] Suplantación de identidad.

12. ¿Qué son los parámetros de una petición HTTP?
	- [ ] Representan la ruta dentro del dominio al que se quiere acceder.
	- [ ] Son los datos que indican la versión del navegador utilizado por el cliente.
	- [ ] Protegen los identificadores de sesión para que no puedan ser usurpados.
	- [x] Es un par clave/valor que utiliza el protocolo HTTP para entregar los datos de entrada a la funcionalidad indicada.

13. En las pruebas de recolección de información podemos extraer información que nos puede ser de utilidad en los metadatos de los archivos que maneja la aplicación. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

14. ¿Qué indican los códigos de estado de tipo 500 del protocolo HTTP?
	- [ ] Respuestas que han sido procesadas correctamente y no retornan ningún tipo de error.
	- [ ] Errores causados por el cliente.
	- [ ] Respuestas de redirección. Indica que el cliente necesita realizar otra petición a la dirección URL indicada por el servidor en la cabecera de respuesta.
	- [x] Errores causados por el servidor.

15. ¿Cuál de las siguientes herramientas nos permite obtener rápidamente las tecnologías, librerías, frameworks, etc. que se utilizan en un aplicativo web?
	- [ ] Wpscan
	- [ ] CMSMap
	- [x] Whatweb
	- [ ] Joomscan

16. Indica cuáles de las siguientes afirmaciones sobre la vulnerabilidad Cross Site Scripting Reflejado es correcta:
	- [ ] Se considera un tipo de ataque persistente que afecta al servidor que sustenta la aplicación.
	- [x] Mediante esta vulnerabilidad se puede inyectar código JavaScript que será ejecutado en el navegador del usuario en caso que no se validen los parámetros de entrada del aplicativo.
	- [x] En ningún momento el código inyectado se guarda en el servidor, sino que habría que generar la dirección URL con la inyección en el parámetro y utilizar técnicas de ingeniería social para enviar el enlace a los usuarios e intentar que accedan al mismo.
	- [ ] El código inyectado se almacena en el servidor y es ejecutado por los navegadores de los usuarios al visitar la sección o funcionalidad afectada.

17. ¿Para qué se utiliza un servidor proxy como Burp Suite a la hora de realizar un análisis de hacking ético en un aplicativo web?
	- [x] Para poder interceptar y modificar peticiones HTTP.
	- [ ] Para navegar más rápido.
	- [ ] Para evitar ser rastreado.
	- [ ] A modo de VPN.

18. ¿Cuáles de las siguientes técnicas se pueden utilizar para detectar paneles de administración expuestos?
	- [ ] Fuerza bruta en el formulario de inicio de sesión.
	- [x] Google Dorks.
	- [ ] Monitorizar las cabeceras "Server" de la respuesta HTTP.
	- [x] Enumeración de directorios.

19. En la versión Community del proxy de interceptación web BurpSuite se puede utilizar el navegador web Chromium que viene integrado. ¿Verdadero o falso?
	- [ ] Verdadero
	- [ ] Falso

20. ¿Cuáles de los siguientes tipos de autenticación presentan más riesgos en caso de sufrir un ataque de tipo Man in the Middle?
	- [x] Uso de APIKey.
	- [ ] Autenticación basada en tokens.
	- [x] Autenticación HTTP Basic.
	- [ ] Autenticación basada en cookies.

21. ¿Qué indica el error HTTP de tipo 403 devuelto en la primera línea de la respuesta del servidor?
	- [ ] "Service Unavailable" – Ha habido un error en el servidor y no se puede procesar la petición.
	- [x] "Forbidden" – La página solicitada existe pero no tienes privilegios para acceder a la misma.
	- [ ] "Redirect" – La navegación del usuario se redirige a otra página distinta.
	- [ ] "Not Found"- La página solicitada no existe

22. ¿Qué método HTTP permite que podamos incluir datos en el cuerpo de la petición?
	- [ ] INCLUDE
	- [ ] GET
	- [x] POST
	- [ ] TRACE

23. La cabecera "set-cookie" es una cabecera propia de la respuesta HTTP. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

24. En la versión Community del proxy de interceptación web BurpSuite se puede utilizar el escáner de vulnerabilidades. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

25. Indica cuáles de las siguientes se consideran vulnerabilidades de lógica de negocio:
	- [ ] Vulnerabilidad presente en una tienda online, a través de la vulnerabilidad identificada un atacante puede ejecutar comandos en el Sistema Operativo de manera remota.
	- [x] Vulnerabilidad presente en una aplicación bancaria por la cual un atacante puede enviar transferencias internacional evitando pagar la comisión establecida.
	- [ ] Vulnerabilidad presente en una aplicación bancaria por la cual un atacante puede hacerse pasar por otro usuario legítimo de la plataforma.
	- [x] Vulnerabilidad presente en una tienda online, a través de la vulnerabilidad identificada, un atacante, generar códigos de descuento.

26. Las vulnerabilidades de lógica de negocio tienen la misma criticidad y riesgo en cualquier aplicativo y no dependen de la naturaleza del aplicativo web ni de los datos que maneje. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

27. ¿Cuál de las siguientes medidas de seguridad es la más indicada para contener ataques de tipo fuerza bruta en un aplicativo web?
	- [x] Utilizar un sistema de tipo Captcha.
	- [ ] Bloquear los usuarios del aplicativo tras 3 intentos fallidos de inicio de sesión.
	- [ ] Mantener los sistemas actualizados.
	- [ ] Identificar y bloquear la dirección IP que esté realizando el ataque.

28. Indica cuáles de estas técnicas pueden ser utilizadas para realizar pruebas de "Evasión del proceso de autenticación" en un aplicativo web:
	- [x] Intentar predecir cómo se generan los identificadores de sesión para localizar identificadores de sesión de otros usuarios.
	- [x] Acceso directo a la parte privada.
	- [x] Inyección de código SQL en el formulario de acceso a la aplicación.
	- [x] Comprobar la existencia de un parámetro que indique si se está autenticado y modificar su valor para tratar de engañar al aplicativo web.

29. En el proxy de interceptación web BurpSuite se puede utilizar la funcionalidad del intruder para automatizar la autenticación de un usuario mediante tokens. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso