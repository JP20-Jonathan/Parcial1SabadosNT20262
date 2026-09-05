from funciones import registrar_comercios, registrar_consumos, generar_informe


def main():
    comercios = registrar_comercios()
    comercios = registrar_consumos(comercios)
    generar_informe(comercios)


if __name__ == "__main__":
    main()
