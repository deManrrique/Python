import subprocess

def crear_y_subir_rama(nombre_rama):
    # Crear una nueva rama
    subprocess.run(['git', 'checkout', '-b', nombre_rama])

    # Realizar cambios en la nueva rama (opcional)

    # Confirmar los cambios
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Cambios en la nueva rama'])

    # Subir la nueva rama a GitHub
    subprocess.run(['git', 'push', 'origin', nombre_rama])

def leer_nombres_de_ramas_desde_archivo(archivo):
    with open(archivo, 'r') as file:
        nombres_ramas = [line.strip() for line in file.readlines()]
    return nombres_ramas

if __name__ == "__main__":
    nombre_de_archivo = "branches.txt"
    
    # Leer nombres de ramas desde el archivo
    nombres_de_ramas = leer_nombres_de_ramas_desde_archivo(nombre_de_archivo)

    # Crear y subir cada rama
    for nombre_rama in nombres_de_ramas:
        crear_y_subir_rama(nombre_rama)
