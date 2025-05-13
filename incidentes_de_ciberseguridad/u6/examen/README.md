# EXAMEN Unidad 6: IDS/IPS Snort

[Test de Daypo](https://www.daypo.com/ic-06.html)

## Preguntas y respuestas

1. ¿Para qué se utiliza el protocolo SSH?
	- [ ] Para las dos funciones anteriores.
	- [ ] Para transferir archivos entre máquinas remotas
	- [x] Para abrir sesiones en máquinas remotas.

2. ¿Qué capa de la Torre ISO-OSI controla la transferencia de datos en la red?
	- [ ] Capa Sesión.
	- [ ] Capa Presentación.
	- [ ] Capa Aplicación.
	- [ ] Capa Red.
	- [ ] Capa Transporte.
	- [x] Capa Enlace de Datos.
	- [ ] Capa Física.

3. ¿Qué estrategia permite estar preparado ante cualquier incidente?
	- [ ] Las instalaciones gemelas que pueden entrar en acción en cualquier momento.
	- [ ] El análisis forense.
	- [ ] Los planes de respuesta.
	- [ ] Los planes de acción.
	- [ ] Las políticas consistentes de respaldos.
	- [x] Todas las anteriores.

4. ¿Qué entidad técnica utiliza Snort para enviar la información de logging a una máquina remota?
	- [x] Una Linux Facility.
	- [ ] Un Socket.
	- [ ] Un Linux Pipe.

5. ¿Cuáles de las siguientes labores se asocian con el segundo principio pragmático de la Ciberseguridad?
	- [x] La detección y análisis rápido de los incidentes de seguridad.
	- [ ] La dotación de políticas de respaldo.
	- [ ] La instalación de la última versión del software infraestructural y de aplicación.

6. ¿Cuál es la misión de Snort en el SOC?
	- [ ] Monitorización de la información.
	- [ ] Filtrado de la información de los logs.
	- [ ] Almacenamiento de la información.
	- [x] Detección y Prevención de Intrusiones.

7. ¿Para qué sirve el protocolo ICMP?
	- [x] Para comprobar la alcanzabilidad de una máquina.
	- [ ] Para implementar las primitivas de mantenimiento remoto.
	- [ ] Para transmitir información de señalización.
	- [ ] Para ninguna opción de las anteriores.

8. ¿Qué capa de la Torre ISO-OSI introduce el direccionamiento y la comunicación entre diferentes redes?
	- [ ] Capa Sesión.
	- [ ] Capa Presentación.
	- [ ] Capa Aplicación.
	- [x] Capa Red.
	- [ ] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [ ] Capa Física.

9. ¿Con qué reglas de detección puede trabajar Snort?
	- [ ] Con las reglas de la comunidad si se arranca en Modo Community.
	- [ ] Con las reglas personalizadas si se arranca en Modo Custom.
	- [x] Siempre funciona con las reglas de la comunidad y las personalizadas a la vez.

10. ¿En qué posición de una regla Snort se sitúa la "Acción de la Regla"?
	- [x] Header.
	- [ ] No Aplica.
	- [ ] Trailer.

11. ¿Qué capa de la Torre ISO-OSI se compone de los servicios de comunicación estándar a disposición de cualquier usuario?
	- [ ] Capa Sesión.
	- [ ] Capa Presentación.
	- [x] Capa Aplicación.
	- [ ] Capa Red.
	- [ ] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [ ] Capa Física.

12. ¿En qué capa de la Torre ISO-OSI se sitúa el protocolo ICMP?
	- [ ] Capa Sesión.
	- [ ] Capa Presentación.
	- [ ] Capa Aplicación.
	- [x] Capa Red.
	- [ ] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [ ] Capa Física.

14. ¿Qué capa de la Torre ISO-OSI asegura que la información se transfiere de forma comprensible para un sistema?
	- [ ] Capa Sesión.
	- [x] Capa Presentación.
	- [ ] Capa Aplicación.
	- [ ] Capa Red.
	- [ ] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [ ] Capa Física.

15. ¿En qué posición de una regla Snort se sitúa el "Protocolo"?
	- [x] Header.
	- [ ] No Aplica.
	- [ ] Trailer.

16. ¿En qué posición de una regla Snort se sitúa el "Mensaje"?
	- [ ] No Aplica.
	- [ ] Header.
	- [x] Trailer.

17. ¿En qué posición de una regla Snort se sitúa la "Dirección de la Operación"?
	- [x] Header.
	- [ ] Trailer.
	- [ ] No Aplica.

18. ¿En qué posición de una regla Snort se sitúa el "Puerto IP Origen"?
	- [ ] No Aplica.
	- [x] Header.
	- [ ] Trailer.

20. ¿Qué capa de la Torre ISO-OSI introduce el concepto de Integridad, asegurando que los datos no se deterioran durante la transferencia?
	- [ ] Capa Sesión.
	- [ ] Capa Presentación.
	- [ ] Capa Aplicación.
	- [ ] Capa Red.
	- [x] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [ ] Capa Física.

21. ¿En qué posición de una regla Snort se sitúan las "Opciones"?
	- [ ] No Aplica.
	- [x] Trailer.
	- [ ] Header.

22. ¿En qué posición de una regla Snort se sitúa el "Puerto IP Destino"?
	- [ ] Trailer.
	- [ ] No Aplica.
	- [x] Header.

23. ¿Qué capa de la Torre ISO-OSI define el hardware de conexión?
	- [ ] Capa Sesión.
	- [ ] Capa Presentación.
	- [ ] Capa Aplicación.
	- [ ] Capa Red.
	- [ ] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [x] Capa Física.

24. ¿Qué capa de la Torre ISO-OSI habilita el inicio, desarrollo y fin de una transmisión?
	- [x] Capa Sesión.
	- [ ] Capa Presentación.
	- [ ] Capa Aplicación.
	- [ ] Capa Red.
	- [ ] Capa Transporte.
	- [ ] Capa Enlace de Datos.
	- [ ] Capa Física.

25. ¿Cuál es la condición básica para activar Snort como un IPS?
	- [ ] Que Snort esté conectado con una base de datos relacional.
	- [x] Disponer de una máquina con al menos dos interfaces de red.
	- [ ] Que Snort esté en la misma máquina que el SIEM.

26. ¿Qué funcionalidad tiene Snort?
	- [ ] Es un IDS con algunas funciones de IPS.
	- [ ] Es sólo un IDS.
	- [x] Es un IDS/IPS totalmente funcional.

27. ¿En qué posición de una regla Snort se sitúa la "Dirección IP Origen"?
	- [ ] Trailer.
	- [ ] No Aplica.
	- [x] Header.
