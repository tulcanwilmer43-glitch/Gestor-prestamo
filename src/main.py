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

#from funciones import *

# ====================================================
# CARGA INICIAL — Se ejecuta al arrancar el programa
# Lee los CSV guardados de ejecuciones anteriores
# ====================================================

print("Cargando datos guardados...")
CargarUsuariosCSV()
CargarItemsCSV()
CargarPrestamosCSV()
print("Datos cargados: " +
      str(len(lista_usuarios))  + " usuarios | " +
      str(len(lista_items))     + " ítems | " +
      str(len(lista_prestamos)) + " préstamos")

# ====================================================
# MENÚ PRINCIPAL CON BUCLE WHILE
# ====================================================

MostrarMenu = """
1. Registrar usuario
2. Registrar ítem
3. Registrar préstamo
4. Registrar devolución
5. Consultar ítems con más de 30 días
6. Consultar artículos prestados
7. Administrador
8. Salir"""

OPCIONES_VALIDAS = ["1", "2", "3", "4", "5", "6", "7", "8"]
titulo_sistema   = "LoanManager Pro"

while True:
    print("")
    print(titulo_sistema.center(Espaciado))
    print("..::Bienvenidos::..".center(Espaciado))
    print("*" * Espaciado)
    print(MostrarMenu)

    opcion = input("Favor registrar la opción deseada --> ").strip()

    if opcion in OPCIONES_VALIDAS:
        match opcion:
            case "1":
                RegistrarUsuario()
            case "2":
                RegistrarItem()
            case "3":
                RegistrarPrestamo()
            case "4":
                RegistrarDevolucion()
            case "5":
                ConsultarYGenerarFactura()
            case "6":
                ConsultarArticulosPrestados()
            case "7":
                MenuAdministrador()
            case "8":
                print("Hasta pronto. ¡Gracias por usar LoanManager Pro!")
                break
    else:
        print("Opción no válida. Intente de nuevo.")
