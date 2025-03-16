def calcular_promedio_temperaturas(datos_temperaturas, nombres_ciudades):
    """
    Calcula el promedio de temperaturas por ciudad en un período de tiempo determinado.

    Parámetros:
    - datos_temperaturas: Lista 3D con temperaturas organizadas por ciudad, semana y día.
    - nombres_ciudades: Lista con los nombres de las ciudades en el mismo orden que los datos.

    Retorna:
    - Un diccionario con los nombres de las ciudades como clave y su temperatura promedio como valor.
    """
    promedios_por_ciudad = {}  # Diccionario para almacenar los promedios

    for ciudad_idx, ciudad in enumerate(datos_temperaturas):
        total_temperaturas = sum(sum(semana) for semana in ciudad)  # Suma todas las temperaturas de la ciudad
        total_dias = sum(len(semana) for semana in ciudad)  # Cuenta el total de días registrados
        promedio = total_temperaturas / total_dias  # Calcula el promedio
        promedios_por_ciudad[nombres_ciudades[ciudad_idx]] = round(promedio, 2)  # Almacena el resultado redondeado

    return promedios_por_ciudad  # Devuelve el diccionario con los promedios por ciudad


# Definir las temperaturas en las ciudades y semanas
temperaturas = [
    [  # Ciudad 1
        [78, 80, 82, 79, 85, 88, 92],  # Semana 1
        [76, 79, 83, 81, 87, 89, 93],  # Semana 2
        [77, 81, 85, 82, 88, 91, 95],  # Semana 3
        [75, 78, 80, 79, 84, 87, 91]   # Semana 4
    ],
    [  # Ciudad 2
        [62, 64, 68, 70, 73, 75, 79],  # Semana 1
        [63, 66, 70, 72, 75, 77, 81],  # Semana 2
        [61, 65, 68, 70, 72, 76, 80],  # Semana 3
        [64, 67, 69, 71, 74, 77, 80]   # Semana 4
    ],
    [  # Ciudad 3
        [90, 92, 94, 91, 88, 85, 82],  # Semana 1
        [89, 91, 93, 90, 87, 84, 81],  # Semana 2
        [91, 93, 95, 92, 89, 86, 83],  # Semana 3
        [88, 90, 92, 89, 86, 83, 80]   # Semana 4
    ]
]

# Nombres de las ciudades
ciudades = ["Ciudad 1", "Ciudad 2", "Ciudad 3"]

# Llamar a la función y mostrar resultados
promedios = calcular_promedio_temperaturas(temperaturas, ciudades)

# Imprimir los promedios de temperatura por ciudad
for ciudad, promedio in promedios.items():
    print(f"{ciudad}: Promedio de temperatura = {promedio}°C")