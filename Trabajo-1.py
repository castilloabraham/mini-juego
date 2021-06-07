def ingreso(coordenadas, option, barcos):
    disparos = 0
    contador = 0
    while contador < 3:
        while option == "Y":
            letra = input("ingresa la letra de la columna donde desea disparar: ")
            while letra.upper() not in "ABCD":
                print("Ingreso invalido, ingrese una la letra valida: (A, B, C, D)")
                letra = input("ingresa la letra de la columna donde desea dispara:r ")
            letra = letra.upper()

            numero = input("ingresa el numero de la fila donde desea disparar: ")
            while numero not in "123":
                print("Ingreso invalido, ingrese un numero valido: (1, 2, 3)")
                numero = input("ingresa el numero de la fila donde desea disparar: ")
            coordenada = letra+numero
            if coordenada not in coordenadas:
                coordenadas.append(coordenada)
                option == "N"
                break
            else:
                print("Ya disparaste a esta celda, no puedes repetir la coordenada de disparo, intente de nuevo")
                option =="Y"  
        if coordenada in barcos:
            print("¡Hundiste el acorazado!")
            contador += 1
            disparos += 1
        else:
            print("¡Fallaste!")
            disparos += 1
    print("¡Has hundido todos los acorazado!")
    print(f"Necesitaste {disparos} para ganar")

def tabla():
    print(" ! A ! B ! C ! D")
    print("1! x ! · ! · ! ·")
    print("2! · ! x ! · ! ·")
    print("3! · ! · ! x ! ·")

def main():
    celdas = ["B1", "C1", "D1", "A2", "C2", "D2", "A3", "B3", "D3"]
    barcos = ["A1", "B2", "C3"]
    coordenadas = []
    option = "Y"
    tabla()
    ingreso(coordenadas, option, barcos)

main()
