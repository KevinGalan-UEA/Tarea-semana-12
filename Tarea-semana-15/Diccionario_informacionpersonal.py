def crear_diccionario():
    # Crear un diccionario con información personal
    informacion_personal = {
        "nombre": "Juanito Calva",
        "edad": 30,
        "ciudad": "Quito",
        "profesion": "Ingeniero"
    }
    return informacion_personal


def modificar_ciudad(diccionario):
    # Modificar el valor de "ciudad"
    diccionario["ciudad"] = "Guayaquil"


def agregar_profesion(diccionario):
    # Agregar una nueva clave-valor para la "profesion"
    diccionario["profesion"] = "Desarrollador de Software"


def verificar_y_agregar_telefono(diccionario):
    # Verificar si la clave "telefono" existe y agregarla si no está
    if "telefono" not in diccionario:
        diccionario["telefono"] = "0987654321"


def eliminar_edad(diccionario):
    # Eliminar la clave "edad" del diccionario
    if "edad" in diccionario:
        del diccionario["edad"]


def main():
    # Crear diccionario y realizar modificaciones
    informacion = crear_diccionario()

    # Modificar ciudad, agregar profesión, verificar teléfono y eliminar edad
    modificar_ciudad(informacion)
    agregar_profesion(informacion)
    verificar_y_agregar_telefono(informacion)
    eliminar_edad(informacion)

    # Imprimir el diccionario final
    print("Diccionario final:", informacion)


# Llamar a la función principal
if __name__ == "__main__":
    main()