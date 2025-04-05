# Escritura y lectura de archivos en Python

# --- ESCRITURA DE ARCHIVO ---

# Abrimos (o creamos si no existe) el archivo my_notes.txt en modo escritura ('w')
archivo = open("my_notes.txt", "w")

# Escribimos tres líneas de notas personales
archivo.write("Me apasiona entrenar en el gimnasio y mantenerme activo.\n")
archivo.write("Actualmente trabajo como entrenador mientras estudio.\n")
archivo.write("Mi meta es conseguir el título de Ingeniero en Tecnologías de la Información y ejercer mi profesión.\n")

# Cerramos el archivo para guardar los cambios
archivo.close()


# --- LECTURA DE ARCHIVO ---

# Abrimos el archivo en modo lectura ('r')
archivo = open("my_notes.txt", "r")

# Leemos línea por línea y mostramos cada una en la consola
for linea in archivo:
    print(linea.strip())  # strip() elimina los saltos de línea extra al final de cada línea

# Cerramos el archivo después de la lectura
archivo.close()