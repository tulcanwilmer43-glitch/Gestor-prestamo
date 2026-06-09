# Manual de Usuario - LoanManager Pro
Código de documentación: pf_Algoritmos
Curso: Algoritmia y Programación 2026-1
Profesor: Julián Andrés Castillo
Autores: Wilmer Andrés Tulcan Mena - Vanesa Lucia Vernal Ruiz
Licencia: MIT


## Qué es LoanManager Pro

LoanManager Pro es un programa de consola desarrollado en Python que permite a MJ (Michael Jackson Gamboa) gestionar de forma organizada el préstamo de objetos a sus amigos. El sistema registra usuarios, ítems, préstamos y devoluciones, y genera documentos automáticamente.


## Requisitos para ejecutar el programa

Python 3.10 o superior instalado.
Los archivos main.py y funciones.py deben estar en la misma carpeta.
No se requieren librerías externas, solo módulos incorporados de Python.


## Cómo ejecutar el programa

En Visual Studio Code:
1. Abrir la carpeta que contiene main.py y funciones.py
2. Abrir una terminal con Ctrl + ñ
3. Escribir: python main.py y presionar Enter

En Google Colab:
1. Subir ambos archivos main.py y funciones.py al entorno
2. Ejecutar la celda con: !python main.py


## Menú principal

Al iniciar el programa verá lo siguiente:

LoanManager Pro
..::Bienvenidos::..

1. Registrar usuario
2. Registrar ítem
3. Registrar préstamo
4. Registrar devolución
5. Consultar ítems con más de 30 días
6. Consultar artículos prestados
7. Administrador
8. Salir

Escriba el número de la opción deseada y presione Enter.


## Opción 1 - Registrar usuario

Registra un amigo de MJ en el sistema.

Datos requeridos:

Nombre: mínimo 3 letras, sin números.
Apellido: mínimo 3 letras, sin números.
Cédula: solo números, entre 3 y 15 dígitos, no puede estar repetida.
Correo: debe tener arroba y terminar en .com
Días de préstamo: solo se permite 5, 10, 15 o 30.

Ejemplo de uso:

Ingrese su nombre: Juan
Ingrese su apellido: Perez
Ingrese su número de cédula: 1234567
Ingrese su correo electrónico: juan@gmail.com
Días de préstamo permitidos: 5 / 10 / 15 / 30
Seleccione los días de préstamo: 15
Usuario registrado y guardado correctamente.


## Opción 2 - Registrar ítem

Registra un objeto que MJ puede prestar.

Datos requeridos:

Nombre: mínimo 3 caracteres, puede tener números.
Categoría: elegir entre las 6 opciones del menú.
Precio: número mayor a 0.
Calificación de estado: número del 1 al 10 usando lógica difusa.

Tabla de estados por lógica difusa:

Calificación 9 o 10: estado Excelente
Calificación 7 u 8: estado Bueno
Calificación 4, 5 o 6: estado Regular
Calificación 1, 2 o 3: estado Malo

Categorías disponibles y prefijos del ID:

1. Videojuegos, prefijo VJ, ejemplo VJ-001
2. Libros, prefijo LB, ejemplo LB-001
3. Música y video, prefijo MV, ejemplo MV-001
4. Herramientas, prefijo HT, ejemplo HT-001
5. Dinero, prefijo DN, ejemplo DN-001
6. Misceláneo y varios, prefijo MS, ejemplo MS-001

El ID se genera automáticamente al registrar el ítem.


## Opción 3 - Registrar préstamo

Crea un préstamo de un ítem disponible a un usuario registrado.

Pasos:
1. El sistema muestra todos los ítems disponibles con su ID.
2. Ingrese el ID del ítem a prestar, por ejemplo VJ-001.
3. Ingrese la cédula del usuario que recibe el préstamo.
4. Si el usuario no está registrado el sistema lo informará y no creará el préstamo.

Solo se puede prestar a usuarios previamente registrados en la opción 1.


## Opción 4 - Registrar devolución

Registra la devolución de un préstamo activo y genera un certificado en archivo de texto.

Pasos:
1. Ingrese la cédula del usuario.
2. El sistema muestra sus préstamos activos con los días transcurridos.
3. Ingrese el número del préstamo a devolver.
4. Se genera automáticamente un archivo .txt con el certificado.

Nombre del archivo generado:
Nombre_Apellido_YYYY-MM-DD_ID.txt
Ejemplo: Juan_Perez_2026-06-03_VJ-001.txt

El certificado indica si la devolución fue a tiempo, dentro de los días acordados, o tardía, con los días de exceso.


## Opción 5 - Consultar ítems con más de 30 días

Busca todos los préstamos activos que superen los 30 días y genera una factura de venta en archivo de texto para cada uno.

La factura incluye:
Datos del comprador.
Motivación de la venta.
Subtotal que es el precio original del ítem.
Impuesto por conchudez del 23%.
Total a pagar.

Nombre del archivo generado:
Nombre_Apellido_FACTURA_ID.txt
Ejemplo: Juan_Perez_FACTURA_VJ-001.txt


## Opción 6 - Consultar artículos prestados

Muestra todos los préstamos activos ordenados de mayor a menor días transcurridos, con estadísticas generales.

Alertas del sistema:

Si llevan 20 días o más aparece el aviso: AVISO - Más de 20 días, solicite devolución.
Si llevan más de 30 días aparece la alerta: ALERTA - Más de 30 días, genere la factura de venta.

Al final muestra el total de préstamos activos y el promedio de días.


## Opción 7 - Administrador

Acceso restringido con usuario y contraseña.

Credenciales por defecto:
Usuario: admin
Contraseña: 1234

Reportes disponibles:
Total de préstamos registrados.
Total de ítems devueltos.
Total de ventas realizadas, es decir préstamos con más de 30 días.
Total pago realizado estimado.
Lista completa de usuarios con cantidad de préstamos.
Usuario con más préstamos.
Usuario con menos préstamos.


## Opción 8 - Salir

Cierra el programa. Todos los datos ya están guardados en los archivos CSV automáticamente antes de salir.


## Archivos CSV generados automáticamente

El programa crea y actualiza estos archivos en la misma carpeta donde está el programa:

usuarios.csv: guarda todos los usuarios registrados.
items.csv: guarda todos los ítems del inventario.
prestamos.csv: guarda el historial completo de préstamos.

Estos archivos permiten que los datos no se pierdan al cerrar el programa. La próxima vez que ejecute main.py toda la información se cargará automáticamente.


## Documentos generados por el sistema

Certificado de devolución en formato .txt: se genera al registrar una devolución.
Factura de venta en formato .txt: se genera al consultar ítems con más de 30 días.
Ambos documentos se guardan en la misma carpeta donde está el programa.


## Mensajes de error comunes

Su nombre no cumple las reglas: el nombre tiene números o menos de 3 letras. Solución: ingrese solo letras, mínimo 3.
Esa cédula ya está registrada: el documento ya existe en el sistema. Solución: use una cédula diferente.
Su correo no cumple las reglas: el correo no tiene arroba o no termina en .com. Solución: use el formato nombre@gmail.com.
Días no válidos: se ingresó un número diferente a 5, 10, 15 o 30. Solución: ingrese solo esos valores.
No hay ítems disponibles: todos los ítems están prestados. Solución: espere una devolución.
Usuario no encontrado: la cédula no está registrada. Solución: registre al usuario primero en la opción 1.
Credenciales incorrectas: usuario o contraseña de administrador erróneos. Solución: verifique usuario admin y contraseña 1234.


Manual generado para LoanManager Pro v1.2.0 - pf_Algoritmos
