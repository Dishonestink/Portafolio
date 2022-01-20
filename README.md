# Portafolio
Portafolio con programas proyectos y códigos que representan mi experiencia y conocimiento en el área de la programación

#Pasos para usar la aplicación (en desarrollo) del lector de ping
1. Dar click en el botón de inicio.
2. Escribir "cmd" y abrir la consola.

Proceso por si no conoce su número ip del dispositivo
2.1 Escribir "ipconfig" y copiar el número correspondiente a "Puerta de enlace predeterminada". Este será el número ip.
Ejemplo: Puerta de enlace predeterminada.......: 192.168.0.4

3. Escribir "(echoe fecha & date & ping -t <<número ip>>) > <<ruta de carpeta a guardar>>\<<nombre deseado del archivo>>.txt"
4. Esperar el tiempo que considere adecuado para tener una buena cantidad de datos para análisis.
5. Oprimir las teclas "ctrl" + "c" en la consola.
6. Abrir el archivo LectorPing.py en una aplicación capáz de leer archivos python (.py).
7. Dar ejecutar el código
8. Cuando el programa le pida el nombre del archivo debe ingresar el mismo nombre que se dio a la consola.
9. Finalmente el programa le mostrará una gráfica con los picos medidos en ms de los paquetes de internet. 
