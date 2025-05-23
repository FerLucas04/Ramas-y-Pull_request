#Práctica de estructuras de control repetitivas (bucles)
saldo= 10000

while True:  #menú principal
    print("-----Cajero automático-----")
    print("(1) Consultar saldo")
    print("(2) Depositar dinero")
    print("(3) Retirar dinero")
    print("(4) Salir")

    while True: #Verificación de operación correcta
        print("\n--")
        operador = input("Ingrese la operación a realizar: ")
        if operador in ["1", "2", "3", "4"]:
            break
        else:
            print("Operación incorrecta, ingreselo de nuevo")

    if operador == "1":  #Consulta de saldo actual
        print("SALDO ACTUAL")
        print("--")
        print(f"\nSu saldo actual es ${saldo}\n")
    elif operador == "2": #Monto a depositar
        print("DEPOSITO DE SALDO")
        print("--")
        while True:
            monto = input("Ingrese un monto de depositar: ")
            if monto.isdigit():
                monto = int(monto)
                if monto < 1:
                    print("El monto debe ser mayor a 0")
                else:
                    print(f"\nSe ha depositado correctamente ${monto}\n")
                    saldo = saldo + monto
                    break
            else:
                print("Debe ingresar un monto numérico")
    elif operador == "3": #Monto a retirar
        print("RETIRO DE SALDO")
        print("--")
        print(f"\nSu saldo actual es ${saldo}\n")
        while True:
            if saldo == 0:
                print("No cuenta con saldo en su cuenta para retirar\n")
                break

            retiro = input("Ingrese la cantidad a retirar: ")
            if retiro.isdigit():
                retiro = int(retiro)
                if retiro < 1:
                    print("El monto a retirar debe ser mayor a 0")
                elif retiro > saldo:
                    print("El saldo a retirar no puede ser mayor al saldo actual")
                else:
                    print(f"\nSe retiró con exito ${retiro}\n")
                    saldo = saldo - retiro
                    break
            else:
                print("Debe ingresar un monto numérico")
    elif operador == "4": #Finalizar programa
        print("\nPROGRAMA FINALIZADO - ADIOS!!\n")
        exit()
    else:
        print("Operación incorrecta\n")