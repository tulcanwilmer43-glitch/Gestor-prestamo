# -*- coding: utf-8 -*-
"""
====================================================
  LoanManager Pro
  Código de documentación: pf_Algoritmos
  Autores: Wilmer Andrés Tulcan Mena
           Vanesa Lucia Vernal Ruiz
  Licencia: MIT
  Curso: Algoritmia y Programación 2026-1
  Profesor: Julián Andrés Castillo
====================================================
"""

import datetime
import csv
import os

# ====================================================
# CLASES  (requisito del profesor)
# ====================================================

class clsUsuarios:
    """Clase que representa a un amigo/usuario del sistema"""
    def __init__(self, nombre, apellido, cedula, correo, dias):
        self.nombre   = nombre
        self.apellido = apellido
        self.cedula   = cedula
        self.correo   = correo
        self.dias     = int(dias)   # Días máximos de préstamo: 5, 10, 15 o 30

    def mostrar(self):
        print("  Nombre   : " + self.nombre + " " + self.apellido)
        print("  Cédula   : " + self.cedula)
        print("  Correo   : " + self.correo)
        print("  Días perm: " + str(self.dias))


class clsPrestamo:
    """Clase que representa un préstamo activo o histórico"""
    def __init__(self, id_prestamo, cedula, id_item, fecha, dias):
        self.id_prestamo      = int(id_prestamo)
        self.cedula           = cedula
        self.id_item          = id_item
        self.fecha            = fecha       # Formato: YYYY-MM-DD
        self.dias             = int(dias)
        self.devuelto         = False
        self.fecha_devolucion = ""

    def calcular_dias_transcurridos(self):
        """Calcula cuántos días han pasado desde que se hizo el préstamo"""
        inicio     = datetime.datetime.strptime(self.fecha, "%Y-%m-%d")
        diferencia = datetime.datetime.today() - inicio
        return diferencia.days


class clsItem:
    """Clase que representa un objeto del inventario de MJ"""
    def __init__(self, id_item, nombre, categoria, precio, estado):
        self.id_item   = id_item
        self.nombre    = nombre
        self.categoria = categoria
        self.precio    = float(precio)
        self.estado    = estado
        self.prestado  = False   # True = está prestado, False = disponible

    def mostrar(self):
        disponible = "No" if self.prestado else "Sí"
        print("  ID        : " + self.id_item)
        print("  Nombre    : " + self.nombre)
        print("  Categoría : " + self.categoria)
        print("  Precio    : $" + str(self.precio))
        print("  Estado    : " + self.estado)
        print("  Disponible: " + disponible)


# ====================================================
# LISTAS GLOBALES donde se guardan los objetos
# ====================================================

lista_usuarios  = []
lista_items     = []
lista_prestamos = []

# Administradores del sistema (usuario / contraseña)
lista_admins = [
    {"usuario": "admin", "contrasena": "1234"}
]

# Datos de categorías e ítems
CATEGORIAS = ["Videojuegos", "Libros", "Música y video",
              "Herramientas", "Dinero", "Misceláneo y varios"]
PREFIJOS   = ["VJ", "LB", "MV", "HT", "DN", "MS"]

DIAS_VALIDOS = ["5", "10", "15", "30"]
Espaciado    = 60

# ====================================================
# FUNCIONES CSV — Guardar y cargar datos
# ====================================================

def GuardarUsuariosCSV():
    archivo  = open("usuarios.csv", "w", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre", "apellido", "cedula", "correo", "dias"])
    for u in lista_usuarios:
        escritor.writerow([u.nombre, u.apellido, u.cedula, u.correo, u.dias])
    archivo.close()

def CargarUsuariosCSV():
    if not os.path.exists("usuarios.csv"):
        return
    archivo = open("usuarios.csv", "r", encoding="utf-8")
    lector  = csv.DictReader(archivo)
    for fila in lector:
        usuario = clsUsuarios(fila["nombre"], fila["apellido"],
                              fila["cedula"], fila["correo"], fila["dias"])
        lista_usuarios.append(usuario)
    archivo.close()

def GuardarItemsCSV():
    archivo  = open("items.csv", "w", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow(["id_item", "nombre", "categoria", "precio", "estado", "prestado"])
    for i in lista_items:
        escritor.writerow([i.id_item, i.nombre, i.categoria,
                           i.precio, i.estado, i.prestado])
    archivo.close()

def CargarItemsCSV():
    if not os.path.exists("items.csv"):
        return
    archivo = open("items.csv", "r", encoding="utf-8")
    lector  = csv.DictReader(archivo)
    for fila in lector:
        item         = clsItem(fila["id_item"], fila["nombre"], fila["categoria"],
                               fila["precio"], fila["estado"])
        item.prestado = (fila["prestado"] == "True")
        lista_items.append(item)
    archivo.close()

def GuardarPrestamosCSV():
    archivo  = open("prestamos.csv", "w", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    escritor.writerow(["id_prestamo", "cedula", "id_item",
                       "fecha", "dias", "devuelto", "fecha_devolucion"])
    for p in lista_prestamos:
        escritor.writerow([p.id_prestamo, p.cedula, p.id_item,
                           p.fecha, p.dias, p.devuelto, p.fecha_devolucion])
    archivo.close()

def CargarPrestamosCSV():
    if not os.path.exists("prestamos.csv"):
        return
    archivo = open("prestamos.csv", "r", encoding="utf-8")
    lector  = csv.DictReader(archivo)
    for fila in lector:
        prestamo                  = clsPrestamo(fila["id_prestamo"], fila["cedula"],
                                               fila["id_item"], fila["fecha"], fila["dias"])
        prestamo.devuelto         = (fila["devuelto"] == "True")
        prestamo.fecha_devolucion = fila["fecha_devolucion"]
        lista_prestamos.append(prestamo)
    archivo.close()

# ====================================================
# FUNCIONES DE VALIDACIÓN
# (mismas del ejemplo del profesor)
# ====================================================

def ValidarNombreApellido(nombre: str) -> bool:
    longitud = len(nombre)
    if longitud >= 3:
        numeros = "1234567890"
        for letra in nombre:
            if letra in numeros:
                return False
        return True
    else:
        return False

def ValidarCedula(cedula: str) -> bool:
    longitud = len(cedula)
    if longitud >= 3 and longitud <= 15:
        if cedula.isnumeric():
            return True
        else:
            return False
    else:
        return False

def ValidarCorreo(correo: str) -> bool:
    correo = correo.strip()
    if " " in correo:
        return False
    if correo.count("@") != 1:
        return False
    usuario, dominio = correo.split("@")
    if len(usuario) == 0 or len(dominio) == 0:
        return False
    if "." not in dominio:
        return False
    if dominio.startswith(".") or dominio.endswith("."):
        return False
    return True

def ValidarPrecio(precio: str) -> bool:
    punto = False
    if len(precio) == 0:
        return False
    for caracter in precio:
        if caracter == ".":
            if punto:
                return False
            punto = True
        elif caracter not in "0123456789":
            return False
    if float(precio) <= 0:
        return False
    return True

def ValidarDias(dias: str) -> bool:
    return dias in DIAS_VALIDOS

def ValidarCategoria(opcion: str) -> bool:
    if opcion.isnumeric():
        if 1 <= int(opcion) <= 6:
            return True
    return False

def ValidarEstadoItem(cal: str) -> bool:
    if cal.isnumeric():
        if 1 <= int(cal) <= 10:
            return True
    return False

# ====================================================
# FUNCIONES DE APOYO
# ====================================================

def ObtenerFechaHoy() -> str:
    return datetime.datetime.today().strftime("%Y-%m-%d")

def EstadoDifuso(calificacion: int) -> str:
    """
    Lógica difusa: convierte un número del 1 al 10
    en una descripción del estado del ítem.
    """
    if calificacion >= 9:
        return "Excelente"
    elif calificacion >= 7:
        return "Bueno"
    elif calificacion >= 4:
        return "Regular"
    else:
        return "Malo"

def BuscarUsuarioPorCedula(cedula: str):
    """Retorna el objeto clsUsuarios si lo encuentra, o None si no existe"""
    for u in lista_usuarios:
        if u.cedula == cedula:
            return u
    return None

def BuscarItemPorId(id_item: str):
    """Retorna el objeto clsItem si lo encuentra, o None si no existe"""
    for i in lista_items:
        if i.id_item == id_item:
            return i
    return None

def GenerarIdItem(categoria: str) -> str:
    """Genera un ID único como VJ-001, LB-002, etc."""
    indice   = CATEGORIAS.index(categoria)
    prefijo  = PREFIJOS[indice]
    contador = 1
    for item in lista_items:
        if item.id_item.startswith(prefijo):
            contador += 1
    numero = str(contador).zfill(3)
    return prefijo + "-" + numero

def Separador(caracter: str = "="):
    print(caracter * Espaciado)

def Titulo(texto: str):
    Separador()
    print(texto.center(Espaciado))
    Separador()

# ====================================================
# OPCIÓN 1 — REGISTRAR USUARIO
# ====================================================

def RegistrarUsuario():
    Titulo("REGISTRAR USUARIO")

    nombre = input("Ingrese su nombre: ").strip()
    if not ValidarNombreApellido(nombre):
        print("Cordial saludo, su nombre no cumple las reglas.")
        print("Debe tener mínimo 3 letras y no puede contener números.")
        return

    apellido = input("Ingrese su apellido: ").strip()
    if not ValidarNombreApellido(apellido):
        print("Cordial saludo, su apellido no cumple las reglas.")
        print("Debe tener mínimo 3 letras y no puede contener números.")
        return

    cedula = input("Ingrese su número de cédula: ").strip()
    if not ValidarCedula(cedula):
        print("Cordial saludo, su cédula no cumple las reglas.")
        print("Solo números, entre 3 y 15 dígitos.")
        return
    if BuscarUsuarioPorCedula(cedula) is not None:
        print("Esa cédula ya está registrada en el sistema.")
        return

    correo = input("Ingrese su correo electrónico: ").strip()
    if not ValidarCorreo(correo):
        print("Cordial saludo, su correo no cumple las reglas.")
        print("Debe tener '@' y terminar en '.com'.")
        return

    print("Días de préstamo permitidos: 5 / 10 / 15 / 30")
    dias = input("Seleccione los días de préstamo: ").strip()
    if not ValidarDias(dias):
        print("Días no válidos. Solo se permiten: 5, 10, 15 o 30.")
        return

    # Creamos el objeto clsUsuarios y lo guardamos
    nuevo_usuario = clsUsuarios(nombre.capitalize(), apellido.capitalize(),
                                cedula, correo.lower(), dias)
    lista_usuarios.append(nuevo_usuario)
    GuardarUsuariosCSV()

    print("")
    print("¡Usuario registrado y guardado correctamente!")
    nuevo_usuario.mostrar()

# ====================================================
# OPCIÓN 2 — REGISTRAR ÍTEM
# ====================================================

def RegistrarItem():
    Titulo("REGISTRAR ÍTEM")

    nombre = input("Ingrese el nombre del ítem: ").strip()
    if len(nombre) < 3:
        print("El nombre debe tener al menos 3 caracteres.")
        return

    print("Categorías disponibles:")
    for i in range(len(CATEGORIAS)):
        print("\t" + str(i + 1) + ". " + CATEGORIAS[i])

    opcion_cat = input("Seleccione la categoría (1-6): ").strip()
    if not ValidarCategoria(opcion_cat):
        print("Opción de categoría no válida.")
        return
    categoria = CATEGORIAS[int(opcion_cat) - 1]

    precio = input("Ingrese el precio de compra: $").strip()
    if not ValidarPrecio(precio):
        print("Precio no válido. Debe ser un número mayor a 0.")
        return

    id_item = GenerarIdItem(categoria)
    print("ID asignado al ítem: " + id_item)

    print("Calificación del estado del ítem:")
    print("  1-3 = Malo  |  4-6 = Regular  |  7-8 = Bueno  |  9-10 = Excelente")
    cal = input("Calificación (1-10): ").strip()
    if not ValidarEstadoItem(cal):
        print("Calificación no válida. Ingrese un número del 1 al 10.")
        return
    estado = EstadoDifuso(int(cal))
    print("Estado registrado: " + estado)

    # Creamos el objeto clsItem y lo guardamos
    nuevo_item = clsItem(id_item, nombre, categoria, float(precio), estado)
    lista_items.append(nuevo_item)
    GuardarItemsCSV()

    print("")
    print("¡Ítem registrado y guardado correctamente!")
    nuevo_item.mostrar()

# ====================================================
# OPCIÓN 3 — REGISTRAR PRÉSTAMO
# ====================================================

def RegistrarPrestamo():
    Titulo("REGISTRAR PRÉSTAMO")

    # Filtramos ítems disponibles (no prestados)
    disponibles = []
    for item in lista_items:
        if not item.prestado:
            disponibles.append(item)

    if len(disponibles) == 0:
        print("No hay ítems disponibles para prestar en este momento.")
        return

    print("Ítems disponibles en inventario:")
    Separador("-")
    for item in disponibles:
        print("  ID: " + item.id_item + " | " + item.nombre +
              " | $" + str(item.precio) + " | Estado: " + item.estado)
    Separador("-")

    id_elegido = input("Ingrese el ID del ítem a prestar: ").strip().upper()

    item_elegido = None
    for item in disponibles:
        if item.id_item == id_elegido:
            item_elegido = item
            break

    if item_elegido is None:
        print("ID no encontrado o ítem no disponible.")
        return

    cedula = input("Ingrese la cédula del usuario: ").strip()
    usuario = BuscarUsuarioPorCedula(cedula)

    if usuario is None:
        print("Usuario no encontrado. El préstamo no se puede realizar.")
        print("Por favor registre primero al usuario nuevo.")
        return

    # Creamos el objeto clsPrestamo
    nuevo_prestamo            = clsPrestamo(len(lista_prestamos) + 1, cedula,
                                            item_elegido.id_item, ObtenerFechaHoy(),
                                            usuario.dias)
    item_elegido.prestado     = True

    lista_prestamos.append(nuevo_prestamo)
    GuardarPrestamosCSV()
    GuardarItemsCSV()

    print("")
    print("¡Préstamo registrado y guardado correctamente!")
    print("  N° Préstamo : " + str(nuevo_prestamo.id_prestamo))
    print("  Usuario     : " + usuario.nombre + " " + usuario.apellido)
    print("  Ítem        : " + item_elegido.nombre + " (" + item_elegido.id_item + ")")
    print("  Fecha       : " + nuevo_prestamo.fecha)
    print("  Días máx.   : " + str(nuevo_prestamo.dias))

# ====================================================
# OPCIÓN 4 — REGISTRAR DEVOLUCIÓN
# ====================================================

def RegistrarDevolucion():
    Titulo("REGISTRAR DEVOLUCIÓN")

    cedula  = input("Ingrese la cédula del usuario: ").strip()
    usuario = BuscarUsuarioPorCedula(cedula)

    if usuario is None:
        print("Usuario no encontrado en el sistema.")
        return

    # Buscamos préstamos activos (no devueltos) del usuario
    activos = []
    for p in lista_prestamos:
        if p.cedula == cedula and not p.devuelto:
            activos.append(p)

    if len(activos) == 0:
        print("No se puede registrar la devolución.")
        print(usuario.nombre + " no tiene préstamos activos.")
        return

    print("Préstamos activos de " + usuario.nombre + " " + usuario.apellido + ":")
    Separador("-")
    for p in activos:
        dias = p.calcular_dias_transcurridos()
        print("  N°" + str(p.id_prestamo) +
              " | Ítem: " + p.id_item +
              " | Fecha: " + p.fecha +
              " | Días transcurridos: " + str(dias))
    Separador("-")

    num = input("Ingrese el número del préstamo a devolver: ").strip()
    if not num.isnumeric():
        print("Número no válido.")
        return

    prestamo_elegido = None
    for p in activos:
        if p.id_prestamo == int(num):
            prestamo_elegido = p
            break

    if prestamo_elegido is None:
        print("Número de préstamo no encontrado.")
        return

    # Registramos la devolución
    fecha_hoy                         = ObtenerFechaHoy()
    prestamo_elegido.devuelto         = True
    prestamo_elegido.fecha_devolucion = fecha_hoy

    # El ítem vuelve a estar disponible
    item_devuelto = BuscarItemPorId(prestamo_elegido.id_item)
    if item_devuelto is not None:
        item_devuelto.prestado = False

    dias_pasados = prestamo_elegido.calcular_dias_transcurridos()

    GuardarPrestamosCSV()
    GuardarItemsCSV()

    if dias_pasados <= prestamo_elegido.dias:
        resultado = "DEVOLUCIÓN A TIEMPO ✓"
    else:
        exceso    = dias_pasados - prestamo_elegido.dias
        resultado = "DEVOLUCIÓN TARDÍA — " + str(exceso) + " días de exceso"

    # Generamos el certificado de devolución en texto plano
    # Nombre del archivo: Nombre_Apellido_Fecha_IDitem.txt
    nombre_archivo = (usuario.nombre + "_" + usuario.apellido +
                      "_" + fecha_hoy + "_" +
                      prestamo_elegido.id_item + ".txt").replace(" ", "_")

    linea_cert = "=" * 52
    certificado = (
        linea_cert + "\n"
        "     CERTIFICADO DE DEVOLUCIÓN\n"
        "     LoanManager Pro | pf_Algoritmos\n" +
        linea_cert + "\n"
        "Fecha emisión      : " + fecha_hoy + "\n"
        "Usuario            : " + usuario.nombre + " " + usuario.apellido + "\n"
        "Cédula             : " + usuario.cedula + "\n"
        "Correo             : " + usuario.correo + "\n"
        "-" * 52 + "\n"
        "N° Préstamo        : " + str(prestamo_elegido.id_prestamo) + "\n"
        "ID del ítem        : " + prestamo_elegido.id_item + "\n"
        "Fecha de préstamo  : " + prestamo_elegido.fecha + "\n"
        "Fecha de devolución: " + fecha_hoy + "\n"
        "Días transcurridos : " + str(dias_pasados) + "\n"
        "Días acordados     : " + str(prestamo_elegido.dias) + "\n"
        "-" * 52 + "\n"
        "RESULTADO: " + resultado + "\n" +
        linea_cert + "\n"
    )

    archivo = open(nombre_archivo, "w", encoding="utf-8")
    archivo.write(certificado)
    archivo.close()

    print("")
    print("¡Devolución registrada correctamente!")
    print("Resultado          : " + resultado)
    print("Certificado generado: " + nombre_archivo)

# ====================================================
# OPCIÓN 5 — CONSULTAR ÍTEMS CON MÁS DE 30 DÍAS / FACTURA
# ====================================================

def ConsultarYGenerarFactura():
    Titulo("ÍTEMS CON MÁS DE 30 DÍAS — GENERAR FACTURA")

    IMPUESTO    = 0.23   # 23% impuesto por conchudez
    encontrados = 0

    for p in lista_prestamos:
        if p.devuelto:
            continue
        dias = p.calcular_dias_transcurridos()
        if dias <= 30:
            continue

        usuario = BuscarUsuarioPorCedula(p.cedula)
        item    = BuscarItemPorId(p.id_item)

        if usuario is None or item is None:
            continue

        subtotal       = item.precio
        valor_impuesto = round(subtotal * IMPUESTO, 2)
        total          = round(subtotal + valor_impuesto, 2)
        fecha_hoy      = ObtenerFechaHoy()

        Separador("-")
        print("  Usuario : " + usuario.nombre + " " + usuario.apellido)
        print("  Ítem    : " + item.nombre + " (" + item.id_item + ")")
        print("  Días    : " + str(dias))
        print("  Total   : $" + str(total))

        # Nombre del archivo: Nombre_Apellido_FACTURA_IDitem.txt
        nombre_archivo = (usuario.nombre + "_" + usuario.apellido +
                          "_FACTURA_" + item.id_item + ".txt").replace(" ", "_")

        linea_fact = "=" * 52
        factura = (
            linea_fact + "\n"
            "        FACTURA DE VENTA\n"
            "        LoanManager Pro | pf_Algoritmos\n" +
            linea_fact + "\n"
            "Fecha           : " + fecha_hoy + "\n"
            "Comprador       : " + usuario.nombre + " " + usuario.apellido + "\n"
            "Cédula          : " + usuario.cedula + "\n"
            "Correo          : " + usuario.correo + "\n"
            "-" * 52 + "\n"
            "MOTIVACIÓN DE LA VENTA:\n"
            "  El ítem '" + item.nombre + "' fue prestado hace " + str(dias) + " días,\n"
            "  superando el límite de 30 días acordado.\n"
            "  Según el acuerdo, el amigo debe comprarlo\n"
            "  al precio original de adquisición de MJ.\n"
            "-" * 52 + "\n"
            "Ítem            : " + item.nombre + " (" + item.id_item + ")\n"
            "Categoría       : " + item.categoria + "\n"
            "Estado          : " + item.estado + "\n"
            "-" * 52 + "\n"
            "Subtotal             : $" + str(subtotal) + "\n"
            "Impuesto conchudez   : $" + str(valor_impuesto) + " (23%)\n"
            "TOTAL A PAGAR        : $" + str(total) + "\n" +
            linea_fact + "\n"
        )

        archivo = open(nombre_archivo, "w", encoding="utf-8")
        archivo.write(factura)
        archivo.close()

        print("  Factura : " + nombre_archivo)
        encontrados += 1

    Separador("-")
    if encontrados == 0:
        print("No hay préstamos activos con más de 30 días.")

# ====================================================
# OPCIÓN 6 — CONSULTAR ARTÍCULOS PRESTADOS
# ====================================================

def ConsultarArticulosPrestados():
    Titulo("ESTADO GENERAL DE PRÉSTAMOS")

    activos = []
    for p in lista_prestamos:
        if not p.devuelto:
            activos.append(p)

    if len(activos) == 0:
        print("No hay préstamos activos actualmente.")
        return

    # Ordenamos de mayor a menor días con ordenamiento burbuja
    for i in range(len(activos)):
        for j in range(i + 1, len(activos)):
            dias_i = activos[i].calcular_dias_transcurridos()
            dias_j = activos[j].calcular_dias_transcurridos()
            if dias_i < dias_j:
                activos[i], activos[j] = activos[j], activos[i]

    total_dias = 0
    for p in activos:
        dias      = p.calcular_dias_transcurridos()
        usuario   = BuscarUsuarioPorCedula(p.cedula)
        item      = BuscarItemPorId(p.id_item)
        nombre_u  = usuario.nombre + " " + usuario.apellido if usuario else "Desconocido"
        nombre_it = item.nombre if item else "Desconocido"
        total_dias += dias

        Separador("-")
        print("  N° Préstamo : " + str(p.id_prestamo))
        print("  Usuario     : " + nombre_u)
        print("  Ítem        : " + nombre_it + " (" + p.id_item + ")")
        print("  Fecha inicio: " + p.fecha)
        print("  Días pasados: " + str(dias))

        if dias > 30:
            print("  [!!!] ALERTA: Más de 30 días — Genere la factura de venta.")
        elif dias >= 20:
            print("  [ ! ] AVISO : Más de 20 días — Solicite devolución.")

    Separador("-")
    total   = len(activos)
    promedio = round(total_dias / total, 1)
    print("  Total activos : " + str(total))
    print("  Promedio días : " + str(promedio))

# ====================================================
# OPCIÓN 7 — ADMINISTRADOR
# ====================================================

def MenuAdministrador():
    Titulo("ACCESO ADMINISTRADOR")

    usr = input("Usuario    : ").strip()
    pwd = input("Contraseña : ").strip()

    acceso = False
    for a in lista_admins:
        if a["usuario"] == usr and a["contrasena"] == pwd:
            acceso = True
            break

    if not acceso:
        print("Credenciales incorrectas. Acceso denegado.")
        return

    Titulo("PANEL DE ADMINISTRACIÓN")

    # --- Calculamos estadísticas ---
    total_prestamos   = len(lista_prestamos)
    total_devueltos   = 0
    total_ventas      = 0
    total_cobrado     = 0.0

    for p in lista_prestamos:
        if p.devuelto:
            total_devueltos += 1
        elif p.calcular_dias_transcurridos() > 30:
            total_ventas += 1
            item = BuscarItemPorId(p.id_item)
            if item is not None:
                total_cobrado += item.precio * 1.23

    print("  Total préstamos registrados : " + str(total_prestamos))
    print("  Total ítems devueltos       : " + str(total_devueltos))
    print("  Total ventas realizadas     : " + str(total_ventas))
    print("  Total pago realizado        : $" + str(round(total_cobrado, 2)))

    Separador("-")
    print("  LISTA DE USUARIOS")
    Separador("-")

    usuario_max  = ""
    usuario_min  = ""
    max_prest    = -1
    min_prest    = 999999

    for u in lista_usuarios:
        cantidad = 0
        for p in lista_prestamos:
            if p.cedula == u.cedula:
                cantidad += 1
        print("  " + u.nombre + " " + u.apellido +
              " | Cédula: " + u.cedula +
              " | Préstamos: " + str(cantidad))
        if cantidad > max_prest:
            max_prest   = cantidad
            usuario_max = u.nombre + " " + u.apellido
        if cantidad < min_prest:
            min_prest   = cantidad
            usuario_min = u.nombre + " " + u.apellido

    Separador("-")
    if len(lista_usuarios) > 0:
        print("  Más préstamos  : " + usuario_max + " (" + str(max_prest) + ")")
        print("  Menos préstamos: " + usuario_min + " (" + str(min_prest) + ")")
