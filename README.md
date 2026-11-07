# TPI: Virtualización con VirtualBox

Trabajo Práctico Integrador de Arquitectura y Sistemas Operativos.

## Datos académicos

- **Alumno:** Nahuel Klen
- **Comisión:** A26 C1-07
- **Profesor:** Aristiaran Martín León
- **Tutor:** Llaneza Nicolás Emanuel
- **Modalidad:** individual

## Objetivo

Implementar un entorno Linux virtualizado sobre Windows 11 y verificar su funcionamiento mediante una aplicación Python, comprobaciones de recursos y pruebas de conectividad.

## Entorno utilizado

| Componente | Configuración |
|---|---|
| Sistema anfitrión | Windows 11 |
| Procesador físico | Intel Core i3-10100 |
| RAM del equipo | 8 GB |
| Hipervisor | Oracle VirtualBox |
| Sistema invitado | Lubuntu, base Ubuntu 24.04.5 LTS |
| CPU virtuales | 2 |
| RAM de la VM | 2048 MB |
| Disco virtual | VDI de 25 GB, dinámico, almacenado en E |
| Red | NAT |
| Python | 3.12.3 |

## Archivos

- [Informe técnico y evidencias](Klen_Nahuel_TPI_Virtualizacion_Informe.pdf)
- [Código fuente](promedio.py)

## Cómo ejecutar el programa

Se necesita Python 3. No requiere bibliotecas externas.

Desde la carpeta donde se encuentre el archivo:

```bash
python3 promedio.py
```

El programa solicita tres notas entre 0 y 10, valida las entradas y muestra el promedio con dos decimales. Acepta decimales con coma o punto.

## Pruebas realizadas

| Entrada | Resultado |
|---|---|
| 7, 8 y 9 | Promedio 8.00 |
| Texto `hola` | Rechazado; solicita nuevamente la nota |
| Nota 11 | Rechazada por estar fuera de rango |
| 7,5; 8; 10 | Promedio 8.50 |

## Verificación del entorno

Se utilizaron los siguientes comandos:

```bash
cat /etc/os-release
python3 --version
nproc
free -h
df -h /
ip -br addr
ip route
ping -c 4 1.1.1.1
ping -c 4 ubuntu.com
```

Se verificaron 2 CPU virtuales, aproximadamente 2 GiB de RAM y conectividad mediante NAT.

El ping a 1.1.1.1 no presentó pérdida. La prueba a ubuntu.com resolvió el nombre, pero registró 25 % de pérdida y una respuesta duplicada; su causa no fue determinada.

## Dificultades y aprendizajes

- Se repitió la instalación por falta de espacio en C y se ubicó el disco virtual en E.
- Se corrigieron errores de transcripción del código.
- Se utilizó `python3` porque el comando `python` no estaba disponible.
- Se creó la instantánea **Linux y Python funcionando** con la VM apagada. No se probó su restauración.

Las capturas y el análisis se encuentran en el informe.

## Uso de inteligencia artificial

Se utilizó asistencia de IA para orientación, revisión del código y organización del informe. La instalación, ejecución de comandos, pruebas y capturas fueron realizadas por el estudiante.

## Referencias

- [Documentación de VirtualBox](https://www.virtualbox.org/manual/)
- [Imágenes oficiales de Lubuntu](https://cdimage.ubuntu.com/lubuntu/releases/24.04/release/)
- [Documentación de Python 3.12](https://docs.python.org/3.12/)
