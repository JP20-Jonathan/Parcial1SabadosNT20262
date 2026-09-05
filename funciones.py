def registrar_comercios():
    comercios = []

    cantidad = None
    while cantidad is None:
        entrada = input("¿Cuántos comercios desea registrar?: ")
        if entrada.isdigit() and int(entrada) > 0:
            cantidad = int(entrada)
        else:
            print("Ingrese un numero entero mayor que 0.")

    for i in range(1, cantidad + 1):
        print(f"\n--- Registro del comercio {i} de {cantidad} ---")

        nit = input("NIT: ")
        nombre = input("Nombre comercial: ")

        tipo = input("Tipo (Tienda/Restaurante/Peluqueria): ")
        while tipo not in ("Tienda", "Restaurante", "Peluqueria"):
            print("Tipo invalido. Debe ser Tienda, Restaurante o Peluqueria.")
            tipo = input("Tipo (Tienda/Restaurante/Peluqueria): ")

        empleados = None
        while empleados is None:
            entrada = input("Cantidad de empleados: ")
            if entrada.isdigit() and int(entrada) > 0:
                empleados = int(entrada)
            else:
                print("Ingrese un numero entero mayor que 0.")

        meta_semanal = None
        while meta_semanal is None:
            entrada = input("Meta semanal de consumo (kWh): ")
            try:
                valor = float(entrada)
                if valor > 0:
                    meta_semanal = valor
                else:
                    print("La meta debe ser mayor que 0.")
            except ValueError:
                print("Ingrese un numero valido.")

        comercio = {
            "nit": nit,
            "nombre": nombre,
            "tipo": tipo,
            "empleados": empleados,
            "meta_semanal": meta_semanal,
            "consumos": []
        }
        comercios.append(comercio)

    return comercios


def registrar_consumos(comercios):
    for comercio in comercios:
        print(f"\n--- Consumos semanales de {comercio['nombre']} ---")
        consumos = []

        for semana in range(1, 5):
            consumo = None
            while consumo is None:
                entrada = input(f"Consumo semana {semana} (kWh): ")
                try:
                    valor = float(entrada)
                    if valor > 0:
                        consumo = valor
                    else:
                        print("El consumo debe ser mayor que 0.")
                except ValueError:
                    print("Ingrese un numero valido.")
            consumos.append(consumo)

        comercio["consumos"] = consumos

    return comercios


def calcular_promedio(consumos):
    acumulador = 0
    for consumo in consumos:
        acumulador += consumo
    promedio = acumulador / len(consumos)
    return promedio


def calcular_variacion(consumos):
    semana1 = consumos[0]
    semana4 = consumos[3]
    variacion = ((semana4 - semana1) / semana1) * 100
    return variacion


def clasificar_consumo(promedio, meta, variacion):
    if promedio <= meta and variacion <= 5:
        return "Eficiente"
    elif promedio <= meta and variacion > 5:
        return "En observacion"
    elif promedio > meta and promedio <= meta * 1.2:
        return "Alto"
    else:
        return "Critico"


def generar_informe(comercios):
    print("\n===== INFORME DE CONSUMO ENERGETICO =====")

    conteo_eficiente = 0
    conteo_observacion = 0
    conteo_alto = 0
    conteo_critico = 0

    mayor_promedio = 0
    comercio_mayor_promedio = ""

    for comercio in comercios:
        promedio = calcular_promedio(comercio["consumos"])
        variacion = calcular_variacion(comercio["consumos"])
        clasificacion = clasificar_consumo(promedio, comercio["meta_semanal"], variacion)

        print(f"\nComercio: {comercio['nombre']}")
        print(f"  Promedio de consumo: {promedio:.2f} kWh")
        print(f"  Variacion semana 1 -> semana 4: {variacion:.2f}%")
        print(f"  Clasificacion: {clasificacion}")

        if clasificacion == "Eficiente":
            conteo_eficiente += 1
        elif clasificacion == "En observacion":
            conteo_observacion += 1
        elif clasificacion == "Alto":
            conteo_alto += 1
        else:
            conteo_critico += 1

        if promedio > mayor_promedio:
            mayor_promedio = promedio
            comercio_mayor_promedio = comercio["nombre"]

    print("\n===== RESUMEN GENERAL =====")
    print(f"Comercios Eficientes: {conteo_eficiente}")
    print(f"Comercios En observacion: {conteo_observacion}")
    print(f"Comercios Altos: {conteo_alto}")
    print(f"Comercios Criticos: {conteo_critico}")
    print(f"\nEl comercio con mayor promedio de consumo fue '{comercio_mayor_promedio}' con {mayor_promedio:.2f} kWh")
