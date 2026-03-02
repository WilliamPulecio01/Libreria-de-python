"""
Aplicación de Noticias Colombia

Este programa consulta noticias en tiempo real desde
medios colombianos utilizando feeds RSS.

Se hace uso de:
- requests (para peticiones HTTP)
- ElementTree (para procesar XML)
"""

import requests
import os
from xml.etree import ElementTree

# Encabezados para simular que la petición viene desde un navegador real
# Algunos sitios bloquean peticiones si no detectan un User-Agent válido
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

# Diccionario con los medios disponibles y sus enlaces RSS
FUENTES = {
    "1": {
        "nombre": "El Tiempo",
        "url": "https://www.eltiempo.com/rss"
    },
    "2": {
        "nombre": "La FM",
        "url": "https://www.lafm.com.co/rss"
    }
}


def limpiar_pantalla():
    """Limpia la consola para una mejor visualización."""
    os.system("cls" if os.name == "nt" else "clear")


def obtener_noticias(url):
    """
    Realiza la petición HTTP al feed RSS
    y devuelve el XML procesado.
    """
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)

        # Verificamos si la respuesta fue exitosa
        if response.status_code == 200:
            return ElementTree.fromstring(response.content)
        else:
            print("Error al obtener las noticias.")
            return None

    except requests.exceptions.RequestException:
        print("Error de conexión. Verifica tu internet.")
        return None


def mostrar_noticias(root):
    """
    Extrae y muestra los titulares del XML.
    """
    if root is None:
        return

    print("\nÚltimas noticias:\n")

    # Buscamos todos los elementos <item> del RSS
    items = root.findall(".//item")

    for i, item in enumerate(items[:10], start=1):
        titulo = item.find("title").text
        enlace = item.find("link").text

        print(f"{i}. {titulo}")
        print(f"   {enlace}\n")


def menu():
    """
    Muestra el menú principal
    y permite seleccionar la fuente.
    """
    while True:
        limpiar_pantalla()
        print("=== Aplicación de Noticias Colombia ===\n")
        print("Seleccione un medio:\n")

        for clave, fuente in FUENTES.items():
            print(f"{clave}. {fuente['nombre']}")

        print("0. Salir")

        opcion = input("\nOpción: ")

        if opcion == "0":
            print("Gracias por usar la aplicación.")
            break

        elif opcion in FUENTES:
            fuente = FUENTES[opcion]
            print(f"\nConsultando noticias de {fuente['nombre']}...\n")

            root = obtener_noticias(fuente["url"])
            mostrar_noticias(root)

            input("\nPresione Enter para continuar...")

        else:
            print("Opción inválida.")
            input("Presione Enter para continuar...")


# Punto de entrada del programa
if __name__ == "__main__":
    menu()