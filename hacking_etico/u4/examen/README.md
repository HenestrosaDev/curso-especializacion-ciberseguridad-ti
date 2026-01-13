# EXAMEN Unidad 4: Consolidación y utilización de sistemas comprometidos

>[!NOTE]
>Este examen está incluido en la baraja de Anki disponible en la raíz del repositorio (`anki.apkg`).

[Test de Daypo](https://www.daypo.com/he-4.html)

## Preguntas y respuestas

1. Indica cuál de los siguientes requerimientos es necesario para poder realizar la técnica del pivoting HTTP:
	- [ ] Hay que utilizar HTTP.
	- [ ] Hay que utilizar un certificado firmado por un agente de confianza.
	- [ ] Hay que utilizar el protocolo HTTPS.
	- [x] Hay que subir un agente a una aplicativo web comprometido.

2. Las técnicas de Password Cracking pueden provocar bloqueos de cuentas de usuario. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

3. ¿En qué Sistemas operativos puede utilizarse el payload meterpreter?
	- [ ] iOS.
	- [x] Microsoft Windows.
	- [ ] Linux.
	- [x] Android.

4. Para poder ejecutar la persistencia necesitamos un servidor de tipo C2. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

5. Es posible inyectar meterpreter enteramente en la memoria del equipo víctima. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

6. En términos de Postexplotación, ¿qué es lo que conocemos como persistencia?
	- [ ] A la capacidad de poder utilizar varios vectores sobre un mismo objetivo.
	- [x] A la capacidad de mantener el acceso en un equipo comprometido.
	- [ ] A la capacidad de obtener nuevas credenciales en el sistema.
	- [ ] A la capacidad de obtener un acceso más privilegiado en el sistema.

7. Las técnicas de Password Guessing pueden provocar bloqueos de cuentas de usuario. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

8. ¿Cuáles de los siguientes problemas se solucionan estableciendo una persistencia?
	- [x] Pérdida de shell por apagado del equipo.
	- [ ] Pérdida de shell por falta de privilegios en el sistema remoto.
	- [x] Pérdida de shell por caída del servicio o proceso.
	- [ ] Pérdida de shell debido a los mecanismos de defensa.

9. En las técnicas de Password Guessing hay que utilizar un diccionario que no sea muy extenso. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

10. ¿Qué es una rainbow table?
	- [ ] Listados de correos electrónicos y contraseñas obtenidos de "leaks".
	- [x] Listados en los que se proporciona posibles contraseñas en claro junto con su hash (hash:contraseña) en algoritmos específicos.
	- [ ] Es un listado que únicamente contiene hashes.
	- [ ] Listados de credenciales tipo usuario:contraseñas.

11. Las tareas de pivoting son propias de la fase de explotación. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

12. Las contraseñas por defecto de muchos dispositivos pueden encontrarse en los propios manuales del producto. ¿Verdadero o falso:
	- [x] Verdadero
	- [ ] Falso

13. Indica de qué manera puedes utilizar un servidor proxy:
	- [x] Utilizando el navegador Web indicando que nos conectaremos a través de un proxy.
	- [ ] Configurando el proxy como la puerta de enlace por defecto.
	- [x] Utilizando clientes específicos para proxy como proxychains.
	- [ ] Utilizando una cadena de certificados.

14. Indica cuáles de las siguientes técnicas se utilizan para realizar ataques contra las contraseñas:
	- [x] Contraseñas por defecto.
	- [x] Ataques de fuerza bruta en la autenticación de una aplicación o servicio.
	- [x] Proceso de cracking de contraseñas.
	- [x] Rainbow Tables.

15. Indica qué es lo que hace la técnica del Pivoting SSH:
	- [ ] Inicia un proxy Remoto en el equipo del atacante y tuneliza las comunicacionse por SSH a la víctima.
	- [ ] Inicia un proxy Local en el equipo de la víctima y tuneliza las comunicacionse por SSH al atacante.
	- [x] Inicia un proxy Local en el equipo del atacante y tuneliza las comunicacionse por SSH a la víctima.
	- [ ] Inicia un proxy Remoto en el equipo de la víctima y tuneliza las comunicacionse por SSH al atacante.

16. Indica cuál de las siguientes afirmaciones es cierta para la herramienta hashcat:
	- [ ] Dispone funciones matemáticas que permiten revertir un hash a su contraseña original.
	- [ ] Hascat siempre tarda el mismo tiempo en averiguar una contraseña.
	- [x] Hashcat tiene que utilizar algoritmos de hashing para generar el hash de posibles contraseñas.
	- [ ] Utiliza rainbow tables.

17. Para poder utilizar técnicas de pivoting necesitamos tener previamente el control de una máquina víctima. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

18. Una vez que se establece el pivoting con meterpreter se puede utilizar el pivoting desde cualquier herramienta fuera de Metasploit sin realizar ninguna tarea adicional. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

19. Si utilizamos la técnica del pivoting con meterpreter, para poder utilizar el pivot con herramientas fuera de Metasploit habrá que iniciar un proxy en el propio Metasploit. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

20. Indica cuáles de los siguientes son técnicas específicas de pivoting:
	- [x] Pivoting por HTTP.
	- [x] Pivoting utilizando meterpreter.
	- [x] Pivoting por SSH.
	- [ ] Pivoting utilizando SMTP.

21. Uno de los requerimientos de las técnicas de pivoting es que necesitamos disponer de privilegios elevados en la máquina que realizará el pivot. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

22. Indica cuáles de las afirmaciones son correctas a la hora de configurar el multihandler de Metasploit como C2:
	- [x] Es necesario iniciar el multihandler como un job de metasploit de esta manera puede establecer comunicación con distintas shells remotas a la vez.
	- [ ] El Multihandler ha de tener la misma configuración que la shell remota (IP del C2, Puerto y Payload).
	- [x] Es necesario iniciar el multihandler como un job de metasploit e indicar que no se detenga tras la primera comunicación con la shell.
	- [x] El Multihandler ha de tener la misma configuración que la shell remota en cuanto a IP del C2 y Puerto pero puede utilizar un Payload distinto al que utilice la shell remota.

23. Meterpreter permite realizar volcado de los hashes del sistema. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

24. Indica cuáles de de los siguientes requisitos son necesarios para poder realizar un ataque de Password guessing:
	- [ ] Utilizar aplicaciones de hashing.
	- [x] Utilizar aplicaciones de fuerza bruta.
	- [x] Disponer de un listado de nombres de usuario.
	- [x] Disponer de un listado de posibles contraseñas.

25. Indica cuáles de los siguientes son tipos de persistencia comunes:
	- [x] Persistencia en registro.
	- [x] Persistencia en servicio.
	- [x] Persistencia en Tareas programadas.
	- [x] Persistencia en CRON.

26. ¿Cuál de las siguientes herramientas se puede utilizar para realizar técnicas de password Guessing?
	- [ ] JohnTheRipper.
	- [x] Patator.
	- [ ] hashcat.
	- [ ] CeWL.

27. Indica cuáles son los motivos por los que utilizar un servidor C2 en la fase de persistencia:
	- [x] Permiten manejar varias shells a la vez.
	- [ ] Permiten tener un punto de fallo.
	- [ ] Permiten elevar privilegios más fácilmente.
	- [x] Permiten poder establecer una comunicación con las shells remotas.

28. ¿Qué requisito es indispensable para que meterpreter pueda volcar los hashes de las contraseñas de un usuario local en Microsoft Windows?
	- [ ] Necesitas que meterpreter esté cargado en memoria.
	- [ ] Necesitas que meterpreter esté inyectado en el proceso del explorer.exe.
	- [ ] Necesitas que el equipo víctima confíe en la máquina del atacante.
	- [x] Necesitas disponer de privilegios elevados.

29. ¿Cuáles de las siguientes no es una características propia de meterpreter?
	- [ ] Permite Elevar privilegios.
	- [x] Permite cifrar el disco de la víctima (Simulación de ransomware).
	- [ ] Permite la carga dinámica de módulos.
	- [ ] Permite utilizar la máquina víctima como pivoting.