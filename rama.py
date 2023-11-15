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

if __name__ == "__main__":
    nombre_de_rama = "nuevaRama"  # Cambia esto al nombre que desees
    crear_y_subir_rama(nombre_de_rama)
