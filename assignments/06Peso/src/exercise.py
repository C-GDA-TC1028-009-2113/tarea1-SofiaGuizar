def main():
    #escribe tu código abajo de esta línea
    pesoInicial= float(input("Dame el peso inicial: "))
    pesoFinal= float(input("Dame el peso final: "))
    meses= int(input("Dame la cantidad de meses: "))
    kilos= (pesoInicial-pesoFinal)/meses
    print ("Lo que debes bajar por mes es: " +str(kilos))
    pass



if __name__ == '__main__':
    main()
