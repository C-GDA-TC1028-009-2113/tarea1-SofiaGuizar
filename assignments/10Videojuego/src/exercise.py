def main():
    #escribe tu código abajo de esta línea
    juegosNuevos= int(input("Dame la cantidad de juegos nuevos: "))
    juegosUsados= int(input("Dame la cantidad de juegos usados: "))
    precioJN= 1000
    precioJU= 350
    precioTotal= (precioJN*juegosNuevos)+(precioJU*juegosUsados)
    print("El total de la compra es: " +str(precioTotal))
    pass




if __name__ == '__main__':
    main()
