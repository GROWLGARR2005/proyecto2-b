# Pensamiento Comutacional seccion 11
#Fecha: 20/05/2024
#autor: Gabriel Alejandro Rodriguez Riquiac 
#objetivo: Realizar todas las funciones requeridas por el laboratorio de ADN 
#entrada: Nombre de sujetos de prueba, Cadena de ADN 
#procesos: print, while, if, elif, else, .upper, .lower, len, all, next, for, in, and, split, raise, Keyerror, ValueError, return, none, continue, try, except, range, str, list, indexerror, match, case
#salida: Lista con sujetos de prueba y ADN, contenido de GC en ADN, porcentaje de bases en cadena de ADN, Secuencia mas larga y posicion, similitud entre dos sujetos de prueba, parentezco de dos cadenas


PROTEINAS_PERMITIDAS = ["G", "T", "A", "C"]

#esta funcion es utilizada como un programa funcional, a su vez es la comprobacion de que el nombre no contenga errores de ser inferior a dos palabras
def solicitar_nombre() -> str:
    nombre = input("Ingrese el nombre completo del sujeto de prueba: ")
    if len(nombre.split()) < 2:
        raise ValueError("El nombre debe constar de al menos dos palabras. Intente nuevamente.")
    return nombre

#funcion de programacion funcional, se utiliza para verifcar que el nombre no exista dentro del diccionario global de sujetos de prueba
def buscar_sujeto_de_prueba() -> str:
    nombre = solicitar_nombre()

    if nombre not in sujetos_de_prueba:
        raise KeyError("El sujeto de pruebas '{nombre}' no se encuentra dentro del listado")
    
    return nombre

#La cadena de adn es solicitada, verifica que el adn sea un caracter definido para su calculo, a su vez verifica que no sea inferior a 13 caracteres
def solicitar_adn(nombre: str) -> str:
    adn_es_valido = False
    while not adn_es_valido:
        adn = input(f"Ingrese la cadena de ADN de {nombre}: ").upper()
        if len(adn) < 13:
            print("La cadena de ADN debe tener al menos 13 caracteres Intente nuevamente.")
            continue
        
        if not all(proteina in PROTEINAS_PERMITIDAS for proteina in list(adn)): 
            print("Se introdujo una proteina invalida.")
            continue
        
        adn_es_valido = True

    return adn

#utilizado para sacar el porcentaje de cad una de las proteinas de las cadenas presentadas
def contenido_de_proteina(adn: str, proteina: str) -> float:
    contador_proteina = adn.count(proteina)
    return contador_proteina / len(adn) * 100

#funcion utilizada para el registro y verificacion continua de los sujetos de prueba
def registrar_sujetos_de_prueba() -> None:
    desea_continuar = "s"
    while desea_continuar == "s":
        try:
            nombre = solicitar_nombre()
        except ValueError as error:
            print(str(error))
            continue

        sujetos_de_prueba[nombre] = None

        desea_continuar = input("¿Desea registrar otro sujeto de prueba? (s/n): ")
    return None

#funcion utilizada para un ingreso continuo de las cadenas de adn, a su vez de existir cadena presente en el sujeto, se le pregunta al usuario si desea reemplazar la cadena de adn
def ingresar_cadena_de_adn() -> None:
    desea_continuar = "s"
    while desea_continuar == "s":
        try:
            nombre = buscar_sujeto_de_prueba()
        except KeyError as error:
            print(str(error))
            continue
        
        if nombre in sujetos_de_prueba and sujetos_de_prueba[nombre]:
            print(f"El sujeto de prueba '{nombre}' ya posee adn registrado")
            reemplazar_cadena_adn = input("Desea reemplazar la cadena de adn? (s/n): ")
            if reemplazar_cadena_adn:
                adn = solicitar_adn(nombre)
        else:
            adn = solicitar_adn(nombre)
        
        sujetos_de_prueba[nombre] = adn
        desea_continuar = input("¿Desea registrar otro adn? (s/n): ")

    return None

#funcion continua para lograr el contador en porcentaje para saber que porcentaje de proteina de gc contiene la cadena de adn
def contenido_de_gc() -> None:
    nombre = buscar_sujeto_de_prueba()
    adn = sujetos_de_prueba[nombre]

    contador_g = contenido_de_proteina(adn, "G")
    contador_c = contenido_de_proteina(adn, "C")
    print(f"Contenido de GC: {contador_g + contador_c}")

    return None

#utiliza contadores para lograr saber exactamente el porcentaje de cada una de las proteinas en la cadena de adn 
def resumen_de_secuencia_de_adn() -> None:
    nombre = buscar_sujeto_de_prueba()
    adn = sujetos_de_prueba[nombre]

    contador_g = contenido_de_proteina(adn, "G")
    contador_t = contenido_de_proteina(adn, "T")
    contador_a = contenido_de_proteina(adn, "A")
    contador_c = contenido_de_proteina(adn, "C")

    print(f"Resumen de secuencia de ADN: '{nombre}'")
    print(f"Contenido G: {contador_g}")
    print(f"Contenido T: {contador_t}")
    print(f"Contenido A: {contador_a}")
    print(f"Contenido C: {contador_c}")

    return None

#la secuencia mas larga es determinada en esta funcion 
def secuencia_mas_larga() -> None:
    nombre = buscar_sujeto_de_prueba()
    adn = sujetos_de_prueba[nombre]

    secuencia_mas_larga = ""
    posicion_inicial = 0

    longitud_actual = 1
    secuencia_actual = adn[0]
    posicion_actual = 0

    for i in range(1, len(adn)):
        if adn[i] == adn[i-1]:
            longitud_actual += 1
        else:
            if longitud_actual > len(secuencia_mas_larga):
                secuencia_mas_larga = secuencia_actual * longitud_actual
                posicion_inicial = posicion_actual
            secuencia_actual = adn[i]
            longitud_actual = 1
            posicion_actual = i

    if longitud_actual > len(secuencia_mas_larga):
        secuencia_mas_larga = secuencia_actual * longitud_actual
        posicion_inicial = posicion_actual

    print(f"Nombre del sujeto: {nombre}")
    print(f"Secuencia de ADN: {adn}")
    print(f"Secuencia más larga: {secuencia_mas_larga}")
    print(f"Longitud: {longitud_actual}")

    return None

#compara dos cadenas de adn de sujetos distintos para comparar el parentezco, sin importar que cantidad de adn tenga el sujeto 
def porcentaje_de_similitud() -> None:
    nombre1 = buscar_sujeto_de_prueba()
    nombre2 = buscar_sujeto_de_prueba()

    adn1 = sujetos_de_prueba[nombre1]
    adn2 = sujetos_de_prueba[nombre2]

    # ACCGGTTTATTAT
    # ACCGGTTTATTGTGCTA
    # =================
    # 11111111111010000

    mas_grande = max(len(adn1), len(adn2))
    resultado = []
    for posicion in range(mas_grande):
        try:
            proteina_adn1 = list(adn1)[posicion]
        except IndexError:
            proteina_adn1 = ""

        try:
            proteina_adn2 = list(adn2)[posicion]
        except IndexError:
            proteina_adn2 = ""

        if proteina_adn1 == proteina_adn2:
            resultado.append(1)
        else:
            resultado.append(0)

    coincidencia = sum(resultado) * 100 / mas_grande

    mensaje_inicial = f"{coincidencia}% coincidencia"
    if coincidencia >= 50:
        print(f"{mensaje_inicial} = padre o hijo")
    elif coincidencia >= 25 and coincidencia < 50:
        print(f"{mensaje_inicial} = abuelo, nieto, tío o tía, sobrino, medio hermano")
    elif coincidencia >= 12.5 and coincidencia < 25:
        print(f"{mensaje_inicial} = primo hermano, bisabuelo, bisnieto, tío abuelo o tía abuela, sobrino abuelo o sobrina nieta, medio tío o tía, medio sobrino o sobrina")
    else:
        print(f"{mensaje_inicial} = sin relación")

    return None


def resumen_de_sujetos_de_prueba() -> None:
    print("Nombre - ADN")
    print("============")
    for nombre in sujetos_de_prueba.keys():
        print(f"{nombre} - {sujetos_de_prueba[nombre]}")

    return None


if __name__ == "__main__":
    sujetos_de_prueba = {}
    while True:
        print("----- MENÚ -----")
        print("1. Registrar sujetos de prueba")
        print("2. Ingresar cadena de ADN")
        print("3. Contenido GC")
        print("4. Resumen de secuencia de ADN")
        print("5. Secuencia más larga")
        print("6. Porcentaje de similitud")
        print("7. Resumen de sujetos de prueba")
        print("8. Salir")
        opcion = int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                registrar_sujetos_de_prueba()
            case 2:
                ingresar_cadena_de_adn()
            case 3:
                contenido_de_gc()
            case 4:
                resumen_de_secuencia_de_adn()
            case 5:
                secuencia_mas_larga()
            case 6:
                porcentaje_de_similitud()
            case 7:
                resumen_de_sujetos_de_prueba()
            case 8:
                print("Vuelva pronto")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")
