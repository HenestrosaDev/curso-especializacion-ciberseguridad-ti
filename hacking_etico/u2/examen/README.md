# EXAMEN Unidad 2: Hacking ético en entornos inalámbricos

>[!NOTE]
>Este examen está incluido en la baraja de Anki disponible en la raíz del repositorio (`anki.apkg`).

[Test de Daypo](https://www.daypo.com/he-2.html)

## Preguntas y respuestas

1. ¿Cuál de los siguientes modos de operación de una tarjeta de red NO se utiliza en las redes de tipo infraestructura?
	- [ ] Master.
	- [x] Adhoc.
	- [ ] Managed.
	- [ ] Monitor.

2. ¿Cuáles de las siguientes características de una red inalámbrica se pueden averiguar monitorizando las redes Wi-FI?
	- [x] Dirección MAC de los Puntos de Acceso.
	- [x] Canales en los que opera el Punto de Acceso.
	- [x] Nombres de las redes Wi-Fi.
	- [x] Tipo de red Wi-Fi.

3. Las antenas Omnidireccionales suelen tener menor alcance de señal que las antenas direccionales. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

4. Para ampliar el radio de cobertura de un Punto de Acceso falso se pueden utilizar antenas omnidireccionales externas de mayor potencia. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

5. Indica cuáles de las siguientes maneras se pueden utilizar para poner una tarjeta Wi-Fi en modo monitor:
	- [ ] Es el modo de operación por defecto de las tarjetas Wi-Fi, no es necesario realizar ninguna acción adicional.
	- [x] En versiones actuales de la herramienta airodump-ng la tarjeta se pone en modo monitor de manera automática sin necesidad de modificar el modo de operación de la tarjeta previamente
	- [x] Haciendo uso de la herramienta airmon-ng.
	- [x] Haciendo uso del comando iwconfig.	

6. No existe ningún vector de ataque en las redes de tipo WPA/WPA2-Enterprise. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

7. Las redes de tipo WPA/WPA2-PSK permiten la trazabilidad de de los usuarios a nivel de red. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

8. La CA que genera los certificados del Punto de Acceso legítimo se puede desplegar en el cliente mediante el uso de MDM (Mobile Device Management) en sistemas Linux, macOS, Android e iOS. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

9. ¿Cuál de los siguientes tipos de redes Wi-Fi se considera adecuada para una buena gestión de los usuarios que pueden acceder a la red?
	- [ ] OPEN.
	- [x] WPA2-Enterprise.
	- [ ] WPA2-PSK.
	- [ ] WEP.

10. Indica cuál es el método utilizado para intentar obtener la clave de acceso de una red WPA/WPA2-PSK en la que hay conectados clientes legítimos de la red:
	- [ ] Capturar numerosos vectores de inicialización de la red.
	- [ ] Capturar el PMKID y realizar un proceso de cracking offline.
	- [x] Capturar el 4-way-handshake y realizar un proceso de cracking offline.
	- [ ] Establecer un punto de acceso falso con hostapd-wpe.

11. La banda inalámbrica de 2,4GHz soporta mayor velocidad de conexión que la banda de 5GHz. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

12. Indica cuál de las siguientes premisas son necesarias para poder ejecutar con éxito un ataque de Punto de Acceso falso en una red de tipo WPA/WPA2-Enterprise:
	- [x] El dispositivo cliente no tiene que validar el certificado del Punto de Acceso.
	- [ ] La autenticación de los usuarios ha de realizarse mediante certificados de cliente.
	- [ ] El dispositivo cliente tiene que validar el certificado del Punto de Acceso.
	- [x] La autenticación de los usuarios ha de realizarse mediante credenciales usuario/contraseña.

13. La CA que genera los certificados del Punto de Acceso legítimo se puede desplegar en el cliente mediante el uso de GPO (Group Policy Object) en sistemas Microsoft. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

14. El modo Master de una tarjeta de red sirve para conectarte a una red Wi-Fi como si fueras un dispositivo cliente. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

15. Las redes de tipo OPEN Permiten acceder a la red Wi-Fi sin contraseña, pero ofrecen un cifrado de canal en capa 2 del modelo OSI. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

16. Las redes de tipo WPA/WPA2-PSK permiten que cada usuario tenga sus propias credenciales de acceso a la red. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

17. Indica en cuál de los siguientes supuestos es más común encontrarte con redes de tipo WEP:
	- [ ] Para acceder a la red corporativa de la empresa.
	- [ ] Redes de Invitados.
	- [x] Sistemas SCADA o equipamiento en fábricas.
	- [ ] Para acceder a una red que se considera crítica debido a los datos con los que opera.

18. Un Beacon Frame es un paquete de información que envía el Punto de Acceso Wi-FI con información de las características de la red que publica. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

19. ¿A qué nos referimos cuando hablamos del Basic Set Identifier (BSSID) de una red Wi-Fi?
	- [x] A la dirección MAC de uno de los Puntos de Acceso de la red Wi-FI.
	- [ ] A la dirección MAC de uno de los clientes de la red Wi-FI.
	- [ ] Al nombre de la red Wi-Fi.
	- [ ] Al procedimiento de autenticación en la red Wi-Fi.

20. La banda inalámbrica de los 5GHz:
	- [x] Tiene mayor velocidad de conexión que la banda de 2,4GHZ.
	- [x] Sufre menos interferencias que la banda de 2,4GHZ.
	- [ ] Tiene mayor rango de cobertura que la banda de los 2,4GHz.
	- [x] Dispone de más canales de frecuencia que la banda de los 2,4GHz.

21. ¿Cuál de las siguientes herramientas se utiliza para suplantar un portal cautivo?
	- [ ] airodump-ng.
	- [ ] hostapd-wpe.
	- [ ] aireplay-ng.
	- [x] Wifiphisher.

22. Indica cuál de las siguientes afirmaciones es correcta con respecto al ataque en redes tipo WPA/WPA2-Enterprise:
	- [ ] El ataque se puede llevar a cabo aunque los usuarios validen los certificados de los Puntos de Acceso.
	- [ ] El ataque consiste en monitorizar un Punto de Acceso legítimo de la red y esperar los intentos de autenticación de los usuarios Legítimos. Estos intentos de autenticación se pueden utilizar para obtener las credenciales de los usuarios mediante un proceso de cracking.
	- [ ] El ataque se puede llevar a cabo aunque los usuarios se autentiquen en la red haciendo uso de un certificado de cliente.
	- [x] El ataque consiste en establecer un Punto de Acceso falso y esperar los intentos de autenticación de los usuarios legítimos. Estos intentos de autenticación se pueden utilizar para obtener las credenciales de los usuarios mediante un proceso de cracking.

23. ¿Con qué herramienta podemos realizar una inyección de tramas en la red inalámbrica?
	- [ ] airodump-ng.
	- [ ] aircrack-ng.
	- [ ] airmon-ng
	- [x] aireplay-ng.

24. Indica cuáles de las siguientes afirmaciones son correctas en el caso de las redes de tipo WEP:
	- [x] Las redes de tipo WEP son vulnerables ante ataques estadísticos para averiguar la clave de acceso.
	- [x] La longitud de la clave de acceso es de entre 5 y 13 caracteres.
	- [ ] Las redes de tipo WEP NO son vulnerables ante ataques estadísticos para averiguar la clave de acceso.
	- [ ] La longitud mínima de la clave de acceso es de 8 caracteres.

25. La banda de tipo "a" (Banda de 5GHz) utiliza los canales 1-14. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

26. ¿Qué es un paquete de tipo Probe Request?
	- [x] Un paquete, enviado por un dispositivo cliente, para averiguar si existe en su alcance alguna otra red inalámbrica de la cuál conoce la clave de acceso.
	- [ ] Un paquete, enviado por un Punto de Acceso, que tiene información de las características de la red inalámbrica.
	- [ ] Un paquete, enviado por un Punto de Acceso, para averiguar si existe en su alcance alguna otra red inalámbrica que pueda causar interferencias en la banda en la que opera.
	- [ ] Un paquete, enviado por un dispositivo cliente, que tiene información de las características de la red inalámbrica.

27. En una misma red inalámbrica no puede haber más de un punto de acceso. ¿Verdadero o falso?
	- [ ] Verdadero
	- [x] Falso

28. Las redes de tipo WEP se encuentran en desuso. ¿Verdadero o falso?
	- [x] Verdadero
	- [ ] Falso

29. Indica cual de las siguientes afirmaciones de las redes de tipo OPEN son ciertas:
	- [ ] Aunque no disponen de contraseña de acceso cifran el canal de comunicaciones.
	- [ ] Cualquier usuario que monitorice la red puede acceder a la información transmitida que se haya transmitido a través de HTTP, FTP o telnet entre otros.
	- [ ] Cualquier persona puede acceder a la red sin necesidad de conocer la contraseña.
	- [ ] Los clientes suelen tener visibilidad entre ellos pudiendo sufrir ataques de otro equipo de la red.