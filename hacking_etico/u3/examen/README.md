# EXAMEN Unidad 3: Ataque y defensa en entorno de pruebas de redes y sistemas para acceder a sistemas de terceros

>[!NOTE]
>Este examen está incluido en la baraja de Anki disponible en la raíz del repositorio (`anki.apkg`).

[Test de Daypo](https://www.daypo.com/he-3.html)

## Preguntas y respuestas

1. Indica cuáles de las siguientes técnicas se pueden utilizar para realizar una interceptación de las comunicaciones:
	- [x] Punto de Acceso falso.
	- [ ] ICMP Spoofing.
	- [ ] SNMP Spoofing.
	- [x] ARP Spoofing.

2. ¿Cuál de las siguientes herramientas se pueden utilizar en un escaneo de red?
	- [x] arp-scan.
	- [ ] Nessus.
	- [ ] Maltego.
	- [ ] GVM.

3. ¿Qué es un Escaneo de servicios?
	- [ ] En este tipo de escaneo se comprueba si existe algún tipo de vulnerabilidad en base al tipo de servicio y la versión del mismo.
	- [ ] Un escaneo destinado a obtener mayor información sobre la red objetivo, direccionamiento IP y la arquitectura utilizada para sustentar toda la infraestructura objetivo.
	- [ ] En este tipo de escaneo se obtienen posibles usuarios en el sistema remoto.
	- [x] Un escaneo que tiene como objetivo identificar los servicios que se ofrecen en la red escaneada.

4. Indica cuál es la afirmación correcta que describe los módulos de tipo "Auxiliary" en Metasploit:
	- [ ] Módulos cuyo objetivo es modificar el código del payload con la intención de ofuscarlo y evadir elementos de seguridad como Antivirus o IDS.
	- [x] Módulos de apoyo que nos proporcionan herramientas propias de la Fase de Enumeración y Escaneo así como otras herramientas para realizar ataques de fuerza bruta.
	- [ ] Módulos que realizan la explotación de vulnerabilidades.
	- [ ] Módulos que nos ayudan en las actividades posteriores a la explotación de un sistema.

5. Un escaneo de red permite localizar vulnerabilidades basadas en el software y versión utilizadas en un determinado servicio. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

6. ¿Cuáles de los siguientes son vectores de acceso válidos en la fase de explotación?
	- [x]  Ejecución de un programa malintencionado (Malware).
	- [x]  Contraseñas por defecto o poco robustas.
	- [x]  Explotación de una vulnerabilidad conocida.
	- [x]  Ejecución remota de comandos.

7. Indica cuáles de las siguientes herramientas se utilizan para realizar un escaneo en frameworks específicos:
	- [ ] nc.
	- [x] CMSMap
	- [x] Wpscan.
	- [x] JoomScan.

8. Indica cuál es el tipo de phishing en el que el intento de engaño se realiza a través de SMS:
	- [x] Smishing.
	- [ ] Pharming.
	- [ ] Vishing.
	- [ ] Whaling.

9. La enumeración SMTP nos permite verificar si una determinada cuenta de correo es válida. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

10. La herramienta nmap soporta varios tipos de escaneo TCP distintos para tratar de evadir los sistemas firewalls. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

11. Indica cuáles de las siguientes herramientas se utilizan para detectar vectores de elevación de privilegios en sistemas Linux:
	- [ ] Watson.
	- [x] LinPEAS.
	- [ ] PrivescCheck.
	- [x] Linenum.

12. La herramienta msfvenom dispone de los mismos exploits disponibles en la herramienta Metasploit. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

13. En un reconocimiento activo se utilizan fuentes de terceros para obtener información del objetivo. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

14. La correcta ejecución de las técnicas de elevación de privilegios nos otorgan un primer acceso al sistema remoto. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

15. Indica cuáles de los siguientes vectores nos permite elevar los privilegios en un sistema Linux:
	- [x] Escritura de cron.
	- [x] Binarios con SUID.
	- [ ] Binarios con ZUID.
	- [ ] Modificación de claves del registro.

16. En la Fase de reconocimiento se pueden ejecutar técnicas de escaneo de vulnerabilidades. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

17. Una shellcode de tipo Bind es adecuada para conseguir una shell remota en un equipo que se encuentra tras un firewall. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

18. Indica el tipo de shellcode que utilizarías para establecer una shell en un sistema expuesto en internet de una compañía objetivo de la auditoría:
	- [ ] Shellcode local tipo reverse.
	- [ ] Shellcode remota tipo bind.
	- [ ] Shellcode local tipo bind.
	- [x] Shellcode remota tipo reverse.

19. ¿Qué tipos de reconocimiento conoces?
	- [x] Reconocimiento pasivo.
	- [ ] Reconocimiento híbrido.
	- [ ] Reconocimineto de vulnerabilidades.
	- [x] Reconocimiento activo

20. Los tipos de exploits pueden clasificarse en Remotos o Locales. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

21. Los payloads de tipo Staged se transmite en varias partes con la finalidad de evitar posibles bloqueos que pudieran realizarse debido a los dispositivos de seguridad existentes en la red. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

22. Indica cuál de los siguientes comandos nos permite ver las opciones de configuración que tiene un determinado módulo en Metasploit:
	- [ ] show.
	- [ ] search.
	- [ ] set.
	- [x] info.

23. ¿Qué es un payload?
	- [ ] Es el código encargado de explotar la vulnerabilidad
	- [ ] Es la parte de código de nmap que se encarga de comprobar si un determinado está abierto o cerrado.
	- [x] Es el código o set de instrucciones que se ejecutan una vez explotada la vulnerabilidad.
	- [ ] Es el código encargado de comprobar si una determinada vulnerabilidad existe en el sistema.

24. La herramienta nmap se puede utilizar en la fase de escaneo de vulnerabilidades. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

25. En cuáles de los siguientes recursos y herramientas se pueden encontrar exploits públicos:
	- [x] Metasploit.
	- [x] searchexploit.
	- [x] Github.
	- [x] exploit-db.

26. ¿En cuál de los siguientes portales NO podemos buscar vulnerabilidades?:
	- [ ] Common vulnerabilities and Exposures (CVE).
	- [ ] exploit-db.
	- [x] Shodan.
	- [ ] vulners.

27. ¿Cuáles de las siguientes técnicas o herramientas NO se utilizan durante un escaneo pasivo?
	- [ ] Recopilación de información en buscadores.
	- [x] Enumeración DNS.
	- [ ] Email harvesting.
	- [ ] Recopilación de infoormación en redes sociales.

28. Indica cuáles de los siguientes vectores nos permite elevar los privilegios en un sistema Windows:
	- [ ] Configuración incorrecta de sudo.
	- [x] Unquoted paths.
	- [ ] Binarios con SUID
	- [x] dllHijacking.

29. Indica cuáles de las siguientes acciones son acciones englobadas en la metodología de phishing:
	- [x] Comprar dominios necesarios.
	- [x] Generar la campaña.
	- [x] Recopilar datos del objetivo.
	- [x] Establecer el tipo de phishing.
	
30. Uno de los requerimientos de la técnica ARP Spoofing, es que el atacante y la víctima han de estar en el mismo dominio de colisión broadcast. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso