def registrarPersonas():
    individuo = {}
    print("\n--- FORMULARIO DE REGISTRO ---")
    
    # 1. Nombre
    individuo["nombre"] = input("Nombre completo: ").strip()
    
    # 2. Edad
    while True:
        try:
            edad = int(input("Edad: "))
            if edad >= 18:
                individuo["edad"] = edad
                break
            print("Debes ser mayor de edad (18+).")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")
            
    # 3. Ciudad
    individuo["ciudad"] = input("Ciudad: ").strip()
    
    # 4. Género del usuario
    opciones_genero = ["Masculino", "Femenino", "Otro"]
    while True:
        print(f"Opciones de género: {opciones_genero}")
        genero_ingresado = input("¿Cuál es su género?: ").strip().capitalize()
        if genero_ingresado in opciones_genero:
            individuo["genero"] = genero_ingresado
            break
        print("Opción no válida. Intenta de nuevo.\n")

    # 5. Género que busca
    opciones_busca = ["Masculino", "Femenino", "Todos"]
    while True:
        print(f"Opciones a buscar: {opciones_busca}")
        busca = input("¿Qué género busca en una pareja?: ").strip().capitalize()
        if busca in opciones_busca:
            individuo["genero_busca"] = busca
            break
        print("Opción no válida. Intenta de nuevo.\n")

    # 6. Rango de edad aceptado
    while True:
        try:
            edad_min = int(input("Edad MÍNIMA aceptada: "))
            edad_max = int(input("Edad MÁXIMA aceptada: "))
            if edad_min <= edad_max:
                individuo["edad_minima"] = edad_min
                individuo["edad_maxima"] = edad_max
                break
            print("La edad mínima no puede ser mayor que la máxima.")
        except ValueError:
            print("Ingresa números enteros válidos.")

    # 7. Intereses
    intereses_str = input("Lista de intereses (separados por coma. Ej: viajar, cine, musica): ")
    lista_intereses = [i.strip().lower() for i in intereses_str.split(",") if i.strip()]
    individuo["intereses"] = set(lista_intereses)

    # 8. Distancia máxima
    while True:
        try:
            individuo["distancia_maxima"] = float(input("Distancia máxima aceptada (km): "))
            break
        except ValueError:
            print("Ingresa una distancia numérica válida.")

    return individuo


def main():
    personas = []
    
    opcion = ""
    while opcion != "9":
        print("1. Registrar nueva persona")
        print("2. Mostrar personas registradas")
        print("3. Buscar posibles coincidencias para una persona")
        print("9. Salir")
        print("="*40)
        
        opcion = input("Selecciona una opción (1-9): ").strip()
        
        if opcion == "1":
            nueva_persona = registrarPersonas()
            personas.append(nueva_persona)
            print(f"\n¡{nueva_persona['nombre']} ha sido registrado(a) con éxito!")
            
        elif opcion == "2":
            print("\n--- PERSONAS REGISTRADAS ---")
            if not personas:
                print("No hay personas registradas aún.")
            else:
                for idx, p in enumerate(personas, 1):
                    intereses = ", ".join(p["intereses"]) if p["intereses"] else "Ninguno"
                    print(f"\n[{idx}] {p['nombre']} ({p['edad']} años) - {p['ciudad']}")
                    print(f"    Género: {p['genero']} | Busca: {p['genero_busca']}")
                    print(f"    Rango de edad aceptado: {p['edad_minima']} a {p['edad_maxima']} años")
                    print(f"    Intereses: {intereses}")
                    
        elif opcion == "9":
            print("¡Saliendo del programa!")
            
        else:
            print("Opción aún no implementada o inválida. Elige una opción correcta.")

if __name__ == "__main__":
    main()



