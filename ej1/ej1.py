tienda = { 
    "terror" : ["Escapa del Marchena I","Explora el lado oscuro de la PETec"],
    "accion" : ["Simulador PETec", "Isla de JF Epstein", "Castro vs Grimma"],
    "ciencia ficcion" : ["Nuclear en la escuela","Simulador de Na + Agua"],
    "aventura" : ["Explora la PETec",]
}
biblioteca = {}
JID = 0
sino = True

while sino == True:
    opcion = input("Elija una opcion: Tienda, Jugar, Salir: ")
    if opcion == "Tienda":
        nosi = True

        print("----------------------------------")
        print("Los generos son:")
        print(tienda.keys())
        print("----------------------------------")
        genero = input("Ingrese el genero: ")
        print(tienda[genero])
        while nosi == True:
            opcion2 = input("Elija una opcion: Comprar, Ingresar, Salir: ")
            if opcion2 == "Comprar":
                JID += 1
                juego = input("Escriba el juego a comprar: ")
                biblioteca[JID] = juego
            elif opcion2 == "Ingresar":
                ingr = input("Ingrese el nombre del juego: ")
                gene = input("Ingrese el genero del juego: ")
                tienda[gene].append(ingr)
            elif opcion2 == "Salir":
                nosi = False
    if opcion == "Jugar":
        print(f'Tenes {len(biblioteca)}:')
        print(biblioteca)
        ja = input("Ingrese el nombre del juego")
        while True:
            print(f'JUgando a {ja}')
    if opcion == "Salir":
        sino = False
        






