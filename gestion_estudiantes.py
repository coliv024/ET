estudiantes = []   # Lista vacía que contendrá los diccionarios de cada estudiante
# FUNCIONES DE VALIDACIÓN
def validar_nombre(nombre):
    """
    Valida que el nombre no esté vacío ni sea solo espacios en blanco.
    Parámetro: nombre (str) – texto ingresado por el usuario.
    Retorna  : True si es válido, False si no lo es.
    (IE 18 - 5%: condición exacta del enunciado para campo texto)
    """
    # strip() elimina espacios al inicio y al final; si queda vacío, es inválido
    return nombre.strip() != ""

def validar_edad(edad):
    """
    Valida que la edad sea un número entero mayor que cero.
    Parámetro: edad (int) – valor numérico ingresado por el usuario.
    Retorna  : True si es válido (> 0), False si no lo es.
    (IE 18 - 5%: condición exacta del enunciado para campo entero)
    """
    # La edad debe ser estrictamente mayor que cero
    return edad > 0

def validar_nota(nota):
    """
    Valida que la nota sea un número decimal entre 1.0 y 7.0 (ambos incluidos).
    Parámetro: nota (float) – valor decimal ingresado por el usuario.
    Retorna  : True si está en el rango [1.0, 7.0], False si no lo está.
    (IE 18 - 5%: condición exacta del enunciado para campo decimal)
    """
    # Se comprueba que la nota esté dentro del rango permitido por el enunciado
    return 1.0 <= nota <= 7.0

# FUNCIONES DEL MENÚ
# Se definen dos funciones separadas para mostrar y leer el menú,
# ambas se invocan en cada iteración del ciclo principal
def mostrar_menu():
    """
    Muestra las opciones del menú principal en pantalla.
    No recibe parámetros ni retorna ningún valor (IE 11 - 3%).
    """
    # Se imprime el menú tal como lo indica el enunciado
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")

def leer_opcion():
    """
    Solicita y valida la opción ingresada por el usuario.
    No recibe parámetros. Retorna el número de opción validado (int).
    Maneja excepciones si el usuario ingresa texto no numérico.
    (IE 12 - 4%)
    """
    # Ciclo que se repite hasta que el usuario ingrese una opción válida
    while True:
        try:
            # Se intenta convertir la entrada a entero
            opcion = int(input("Ingrese una opción: "))
            # Se verifica que esté dentro del rango permitido (1 a 6)
            if 1 <= opcion <= 6:
                return opcion   # Se retorna la opción válida al programa principal
            else:
                print("Opción fuera de rango. Ingrese un número entre 1 y 6.")
        except ValueError:
            # Si el usuario escribe algo que no es un número entero
            print("Entrada no válida. Debe ingresar un número entero.")


# FUNCIÓN PARA AGREGAR ESTUDIANTE
# Recibe la lista como parámetro, solicita los datos, llama a las funciones
# de validación y agrega el registro solo si todo es válido.
# Los mensajes de error se muestran aquí, no en las funciones de validación
def agregar_estudiante(lista_estudiantes):
    """
    Solicita los datos de un nuevo estudiante, los valida y, si son correctos,
    crea el diccionario y lo agrega a la lista.
    Parámetro: lista_estudiantes (list) – la lista principal de estudiantes.
    No retorna nada; modifica la lista directamente.
    (IE 6 - 5%: solo agrega cuando todos los campos son válidos)
    """
    print("\n--- Agregar Estudiante ---")

    # --- Validación del nombre ---
    nombre = input("Ingrese el nombre del estudiante: ")
    if not validar_nombre(nombre):
        # Mensaje de error mostrado aquí, no en la función de validación
        print("Error: El nombre no puede estar vacío ni contener solo espacios.")
        return  # Se sale de la función sin agregar ningún registro

    # --- Validación de la edad ---
    try:
        # Se intenta convertir la entrada a entero
        edad = int(input("Ingrese la edad del estudiante: "))
    except ValueError:
        print("Error: La edad debe ser un número entero.")
        return

    if not validar_edad(edad):
        print("Error: La edad debe ser un número entero mayor que cero.")
        return

    # --- Validación de la nota ---
    try:
        # Se intenta convertir la entrada a decimal
        nota = float(input("Ingrese la nota del estudiante (1.0 - 7.0): "))
    except ValueError:
        print("Error: La nota debe ser un número decimal.")
        return

    if not validar_nota(nota):
        print("Error: La nota debe estar entre 1.0 y 7.0 (incluidos).")
        return

    # --- Construcción del diccionario del estudiante ---
    # Solo se llega aquí si TODOS los datos son válidos
    # El diccionario contiene exactamente las claves indicadas en el enunciado
    # con sus tipos de dato correspondientes: str, int, float, bool
    nuevo_estudiante = {
        "nombre"  : nombre.strip(),   # str – nombre del estudiante sin espacios extra
        "edad"    : edad,             # int – edad del estudiante
        "nota"    : nota,             # float – nota entre 1.0 y 7.0
        "aprobado": False             # bool – siempre False al crear el registro
    }

    # Se agrega el diccionario a la lista usando append()
    lista_estudiantes.append(nuevo_estudiante)
    print(f"Estudiante '{nombre.strip()}' agregado exitosamente.")

# FUNCIÓN DE BÚSQUEDA
# Recibe la lista y el nombre a buscar; retorna la posición o -1
def buscar_estudiante(lista_estudiantes, nombre_buscar):
    """
    Busca un estudiante por nombre en la lista.
    Parámetros:
        lista_estudiantes (list) – la lista principal de estudiantes.
        nombre_buscar     (str)  – nombre exacto que se desea encontrar.
    Retorna:
        int – índice (posición) del registro si existe, o -1 si no existe.
    (IE 8 - 5%: retorna posición o indicador explícito de ausencia)
    """
    # Se recorre la lista usando range() para obtener el índice de cada elemento
    # Se necesita el índice (posición) para retornarlo → se usa for con range
    for indice in range(len(lista_estudiantes)):
        # Se compara el campo "nombre" del diccionario con el nombre buscado
        if lista_estudiantes[indice]["nombre"] == nombre_buscar:
            return indice   # Se retorna la posición donde se encontró el estudiante

    # Si el ciclo termina sin encontrar el nombre, se retorna -1 como centinela
    return -1
# FUNCIÓN PARA ELIMINAR ESTUDIANTE
# Invoca buscar_estudiante() para no duplicar lógica de búsqueda
def eliminar_estudiante(lista_estudiantes):
    """
    Solicita el nombre del estudiante a eliminar, llama a buscar_estudiante()
    y, si existe, lo elimina de la lista.
    Parámetro: lista_estudiantes (list) – la lista principal de estudiantes.
    No retorna nada; modifica la lista directamente.
    (IE 9 - 5%: usa resultado de búsqueda; no reimplementa la búsqueda)
    """
    print("\n--- Eliminar Estudiante ---")
    nombre = input("Ingrese el nombre del estudiante a eliminar: ")

    # Se llama a la función de búsqueda (no se reimplementa la lógica aquí)
    posicion = buscar_estudiante(lista_estudiantes, nombre)

    if posicion != -1:
        # Si la posición es válida, se elimina el registro en esa posición
        lista_estudiantes.pop(posicion)
        print(f"Estudiante '{nombre}' eliminado exitosamente.")
    else:
        # Si retorna -1, se muestra el mensaje exacto indicado en el enunciado
        print(f"El estudiante '{nombre}' no se encuentra registrado.")
# FUNCIÓN PARA ACTUALIZAR ESTADOS
# Recorre la lista y actualiza "aprobado" según la nota de cada estudiante
def actualizar_estados(lista_estudiantes):
    """
    Recorre todos los registros y actualiza el campo "aprobado":
        - True  si la nota es >= 4.0
        - False si la nota es <  4.0
    Parámetro: lista_estudiantes (list) – la lista principal de estudiantes.
    No retorna nada; modifica los diccionarios directamente.
    (IE 16 - 5%: función dedicada que recibe la lista y aplica la regla)
    """
    # Se usa for-in porque no se necesita el índice; solo se modifica el campo
    # del diccionario referenciado por la variable "estudiante"
    for estudiante in lista_estudiantes:
        # Si la nota es mayor o igual a 4.0, el estudiante aprueba
        if estudiante["nota"] >= 4.0:
            estudiante["aprobado"] = True    # Condición activa 
        else:
            estudiante["aprobado"] = False   # Condición inactiva

# FUNCIÓN PARA MOSTRAR ESTUDIANTES
# Primero actualiza los estados, luego imprime cada registro con el formato
# indicado en el enunciado.
def mostrar_estudiantes(lista_estudiantes):
    """
    Actualiza los estados llamando a actualizar_estados() y luego imprime
    cada estudiante con el formato indicado en el enunciado.
    Parámetro: lista_estudiantes (list) – la lista principal de estudiantes.
    No retorna nada.
    """
    # Paso 1: actualizar estados antes de mostrar (según enunciado, opción 5)
    actualizar_estados(lista_estudiantes)

    print("\n=== LISTA DE ESTUDIANTES ===")

    # Se verifica si la lista está vacía para informar al usuario
    if len(lista_estudiantes) == 0:
        print("No hay estudiantes registrados.")
        return

    # Se recorre la lista con for-in porque solo se necesita leer cada elemento
    for estudiante in lista_estudiantes:
        # Se muestra el estado en texto legible según el valor booleano
        estado = "APROBADO" if estudiante["aprobado"] else "REPROBADO"

        # Formato de salida exacto indicado en el enunciado
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad  : {estudiante['edad']}")
        print(f"Nota  : {estudiante['nota']}")
        print(f"Estado: {estado}")

# PROGRAMA PRINCIPAL
# Declara la lista, llama a mostrar_menu() y leer_opcion() en cada iteración,
# dirige la ejecución según la opción elegida y pasa la lista como argumento
# (nunca como variable global) a cada función que la necesita 
# El ciclo continúa hasta que el usuario elige la opción 6
def main():
    """
    Función principal del programa.
    Controla el ciclo del menú y delega cada operación a la función
    correspondiente, pasando la lista como argumento explícito.
    """
    # La lista se declara en el ámbito principal y se pasa como parámetro
    # a cada función que la necesita; nunca se accede como variable global
    lista_estudiantes = []   #lista vacía antes de operar

    # Ciclo que mantiene el menú activo hasta que el usuario elige salir
    while True:
        # En cada vuelta se llama a ambas funciones del menú
        mostrar_menu()                       # Muestra las opciones en pantalla
        opcion = leer_opcion()               # Lee y retorna la opción validada

        # Se dirige la ejecución según la opción elegida
        if opcion == 1:
            agregar_estudiante(lista_estudiantes)    # Pasar lista como argumento

        elif opcion == 2:
            # Búsqueda: el programa principal gestiona el resultado
            print("\n--- Buscar Estudiante ---")
            nombre = input("Ingrese el nombre del estudiante a buscar: ")
            posicion = buscar_estudiante(lista_estudiantes, nombre)

            if posicion != -1:
                # La posición es válida: se muestran los datos del estudiante
                estudiante = lista_estudiantes[posicion]
                estado = "APROBADO" if estudiante["aprobado"] else "REPROBADO"
                print(f"\nEstudiante encontrado en la posición {posicion}:")
                print(f"Nombre: {estudiante['nombre']}")
                print(f"Edad  : {estudiante['edad']}")
                print(f"Nota  : {estudiante['nota']}")
                print(f"Estado: {estado}")
            else:
                # Posición -1: el estudiante no existe
                print(f"El estudiante '{nombre}' no se encuentra registrado.")

        elif opcion == 3:
            eliminar_estudiante(lista_estudiantes)   # Pasar lista como argumento

        elif opcion == 4:
            actualizar_estados(lista_estudiantes)    # Pasar lista como argumento
            print("Estados de todos los estudiantes actualizados.")

        elif opcion == 5:
            mostrar_estudiantes(lista_estudiantes)   # Pasar lista como argumento

        elif opcion == 6:
            # Opción de salida: se imprime despedida y se rompe el ciclo
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break   # El ciclo se detiene de forma limpia

# PUNTO DE ENTRADA DEL PROGRAMA
# Se invoca main() solo si el script se ejecuta directamente.
main()
