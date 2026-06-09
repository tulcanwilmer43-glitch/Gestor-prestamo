# Plan de Versionado - LoanManager Pro
Código de documentación: pf_Algoritmos
Curso: Algoritmia y Programación 2026-1
Profesor: Julián Andrés Castillo
Autores: Wilmer Andrés Tulcan Mena - Vanesa Lucia Vernal Ruiz


## Historial de versiones

Versión v0.1.0
Fecha: 2026-03-03
Días desde el inicio: Día 1
Descripción: Inicio del proyecto. Definición del problema, integrantes y nombre del sistema LoanManager Pro. Reunión inicial del equipo y creación del repositorio en GitHub.

Versión v0.2.0
Fecha: 2026-03-10
Días desde el inicio: Día 8
Descripción: Entrega 1. Documentación inicial completa. Actas de entendimiento, reporte de visión, especificación de requisitos funcionales y no funcionales, y plan de proyecto con diagrama de Gantt.

Versión v0.3.0
Fecha: 2026-03-17
Días desde el inicio: Día 15
Descripción: Diseño del sistema. Definición de las clases clsUsuarios, clsPrestamo y clsItem con sus atributos. Boceto del menú de consola y estructura general del programa.

Versión v0.4.0
Fecha: 2026-03-24
Días desde el inicio: Día 22
Descripción: Desarrollo módulo 1. Implementación de la función RegistrarUsuario con todas las validaciones de nombre, apellido, cédula, correo y días de préstamo.

Versión v0.5.0
Fecha: 2026-03-31
Días desde el inicio: Día 29
Descripción: Desarrollo módulo 2. Implementación de la función RegistrarItem con categorías, generación automática de ID por prefijo y lógica difusa para el estado del ítem.

Versión v0.6.0
Fecha: 2026-04-07
Días desde el inicio: Día 36
Descripción: Desarrollo módulo 3. Implementación de la función RegistrarPrestamo con validación de usuario existente, listado de ítems disponibles y control de disponibilidad.

Versión v0.7.0
Fecha: 2026-04-14
Días desde el inicio: Día 43
Descripción: Desarrollo módulo 4. Implementación de la función RegistrarDevolucion con generación de certificado en archivo de texto y detección de devolución tardía con días de exceso.

Versión v0.8.0
Fecha: 2026-04-21
Días desde el inicio: Día 50
Descripción: Desarrollo módulo 5. Implementación de la función ConsultarYGenerarFactura con cálculo del impuesto por conchudez del 23%, subtotal, total y generación de factura en archivo de texto.

Versión v0.9.0
Fecha: 2026-04-28
Días desde el inicio: Día 57
Descripción: Desarrollo módulo 6. Implementación de la función ConsultarArticulosPrestados con ordenamiento burbuja de mayor a menor días y notificaciones de alerta a los 20 y 30 días.

Versión v0.10.0
Fecha: 2026-05-05
Días desde el inicio: Día 63
Descripción: Desarrollo módulo 7. Implementación del MenuAdministrador con autenticación por usuario y contraseña, y reportes estadísticos del sistema.

Versión v0.11.0
Fecha: 2026-05-12
Días desde el inicio: Día 70
Descripción: Integración de persistencia de datos. Se agregaron las funciones de guardado y carga automática con archivos CSV para usuarios, ítems y préstamos. Los datos se conservan entre ejecuciones.

Versión v1.0.0
Fecha: 2026-05-20
Días desde el inicio: Día 78
Descripción: Primera versión estable completa en un solo archivo. Todas las funciones integradas, probadas y funcionales. Código con clases y objetos según los requisitos del profesor.

Versión v1.1.0
Fecha: 2026-05-27
Días desde el inicio: Día 85
Descripción: Refactorización del código. Separación en dos archivos: funciones.py con las clases, validaciones y lógica del sistema, y main.py con el menú principal. Importación usando from funciones import.

Versión v1.2.0
Fecha: 2026-06-03
Días desde el inicio: Día 92
Descripción: Versión final. Revisión completa del código, ajuste de comentarios, generación del manual de usuario, plan de versionado y subida final al repositorio de GitHub con la estructura requerida en las carpetas src y doc.


## Resumen del proceso de desarrollo

El proyecto inició el 3 de marzo de 2026 con la definición del problema y la conformación del equipo. Durante las primeras dos semanas se realizó la planeación y documentación inicial que corresponde a la entrega 1. A partir de la semana 3 se comenzó el desarrollo por módulos, implementando una funcionalidad por semana siguiendo el cronograma del diagrama de Gantt. En la semana 10 se integró la persistencia de datos con CSV. En la semana 12 se obtuvo la primera versión estable. En la semana 14 se refactorizó el código separándolo en dos archivos. En la semana 16 se realizó la entrega final con toda la documentación completa y el código listo para sustentar.


Plan de versionado generado para LoanManager Pro v1.2.0 - pf_Algoritmos
