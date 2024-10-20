# Introducción al Bastionado

La ciberseguridad se apoya en tres elementos principales:
- Procesos
- Personas
- Tecnologías

## 1. Orígenes

En los 70 y 80, los _malware_ no eran tan populares. Uno de los primeros fue el [gusano Morris](https://es.wikipedia.org/wiki/Gusano_Morris), lo que motivó la creación del Computer Emergency Response Team (CERT) para contener amenazas similares futuras. A partir de finales de los años 80, prolifera el cibercrimen y problemas de ciberseguridad.

### 1.1. Necesidad

Es necesario realizar tareas de bastionado de sistemas y redes por estos dos motivos:
- Para asegurar la **confidencialidad**, la **integridad** y la **disponibilidad** de la información.
- Por requerimientos legales cuyo fin es para proteger las infraestructuras tecnológicas que almacenan la información. Los de carácter personal tienen que usar mecanismos de cifrado.

Tipos de amenazas:
- **Malware** (aka virus): 
	- [Ransomware](https://en.wikipedia.org/wiki/Ransomware): Secuestra el dispositivo cifrando los archivos. Ransom (suma de dinero exigida por la liberación de un cautivo) + ware. 
	- [Spyware](https://en.wikipedia.org/wiki/Spyware): Recopila información, la cual manda a través de Internet.
	- [Troyanos](https://en.wikipedia.org/wiki/Trojan_horse_(computing)) (trojan horses): Software dañino disfrazado de software legítimo.
	- [Zombie](https://en.wikipedia.org/wiki/Zombie_(computing)): Ordenador conectado a Internet que forma parte de una botnet controlada por un hacker para orquestar ataques DDoS. Se infecta a través de troyanos o gusanos, principalmente.
	- [Keylogger](https://en.wikipedia.org/wiki/Keystroke_logging): Registra las pulsaciones del teclado o clicks de ratón para obtener todo tipo de información.
	- [Rootkit](https://en.wikipedia.org/wiki/Rootkit): Software que permite acceso a un área de otro software que de otro modo no estaría permitido. Generalmente, los rootkit ocultan registros del acceso para que el software objetivo no sepa que ha sido vulnerado.
	- [Fileless malware](https://en.wikipedia.org/wiki/Fileless_malware): Se aprovecha directamente del sistema operativo para ejecutar scripts en la consola.
- **Vulnerabilidades**: Fallo en el código o en la configuración de un software, o en el diseño e implementación de un sistema de hardware, que permite a un atacante comprometer la seguridad del activo y hacerlo funcionar de forma antiproducente y para el que no está autorizado.
- **Fraude**: Problema más recurrente ya que la principal motivación de los ciberdelincuentes es la económica.
- **Insiders**: Ataque procedente de un miembro de la propia empresa con el fin de perjudicarla.
- **Ataques externos**: Pueden ser intencionados o no.

## 2. Bastionado o "Hardening"

**Bastionado**: Proceso para reducir las vulnerabilidades a través de políticas, medidas de seguridad o mecanismos que lo consiga.

Características:
- Eliminación de cuentas innecesarias.
- Eliminación de contraseñas por defecto.
- Instalación de firewalls, Web Application Firewalls (WAFs), etc.
- Implementar política de actualizaciones para mantener los sistemas seguros.
- Deshabilitar puertos y servicios que no se usen y securizar los que sí se utilizan.
- Desarrollar planes de contingencia que incluyan copias de seguridad y recuperación de sistemas.
- Elevar la seguridad en redes inalámbricas y usarlas únicamente si es necesario.

**Vulnerabilidad vs. amenaza**: El primero hace referencia a algo que podría presentar un daño potencial sobre un activo, mientras que el segundo es un estado o condición que tiene el activo y que podría hacer daño si se materializara. 

Ejemplo: Si tenemos escritorio remoto activado:
- **Vulnerabilidad**: Que el equipo use credenciales por defecto o poco robustas donde un ataque de fuerza bruta pueda tener éxito.
- **Amenaza**: Que un atacante conozca la IP y que intente acceder al equipo.

### 2.1. Zero trust

Propugna que no se debe confiar en ningún usuario o dispositivo sin antes verificar su identidad y nivel de seguridad. 

Características:
- **Doble factor de autenticación** (2FA) o **multifactor de autenticación** (MFA) como capa adicional al clásico usuario/contraseña.
- **Segmentación de la red** para aislar recursos y evitar que el atacante pueda moverse libremente por la red en caso de acceso.
- **Menor privilegio**, limitando el acceso a estrictamente lo necesario.
- **Supervisión constante** para identificar amenazas en tiempo real.

### 2.2. ¿Por dónde empiezo?

El **análisis de riesgos** es el primer paso para elevar el nivel de ciberseguridad en los procesos más importantes. La ciberseguridad se alinea con los procesos de la organización o empresa, nunca al revés. Podemos usar la [herramienta de autodiagnóstico del Insitituto Nacional de Ciberseguridad (INCIBE)](https://adl.incibe.es/).

## 3. Plan director de seguridad

Conjunto de actividades para **elevar el nivel de ciberseguridad**. Su ejecución resultará satisfactoria cuando, tras los **análisis de riesgos**, se consideren que los riesgos se han reducido hasta un nivel aceptable. No olvidar que **la ciberseguridad apoya al negocio**.

El plan tiene que incluir **medidas técnicas como medidas organizativas** en su ejecución con el fin de incrementar la seguridad en los **procesos más críticos**. Se basa en **ciclos de mejora continua**, ya que la situación de las empresas y otros factores cambian con el tiempo.