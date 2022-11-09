def aplicarRegla(caracteres:list):
    if len(caracteres) == 2:
        sum = int(caracteres[0]) + int(caracteres[1])
        return 1 if sum == 1 else 0
    else:
        sum = int(caracteres[0]) + int(caracteres[1]) + int(caracteres[2])
        return 1 if sum == 1 else 0

def triangulo(cadena, numiter):
    triangulo = [cadena]
    actual = cadena
    cont = 0
    while(cont < numiter):
        nueva = ""
        for i in range(len(actual)):
            if i == 0:
                nueva += str(aplicarRegla([actual[i], actual[i+1]]))
            elif i == len(actual) - 1:
                nueva += str(aplicarRegla([actual[i-1], actual[i]]))
            else:
                nueva += str(aplicarRegla([actual[i-1], actual[i], actual[i+1]]))
        triangulo.append(nueva)
        actual = nueva
        cont += 1
    return triangulo

def print_triangle(triangle):
    with open("triangle.txt", "w") as f:
        for line in triangle:
            for char in line:
                if char == "1":
                    f.write("X")
                else:
                    f.write(" ")
            f.write("\n")
        
if __name__ == "__main__":
    while True:
        cadena = input("Ingrese la cadena (0|1):\n")
        numiter = int(input("Ingrese el numero de iteraciones:\n"))
        if len(cadena) < 2:
            print("La cadena debe tener al menos 2 caracteres")
        else:
            break
    triangle = triangulo(cadena, numiter)
    print_triangle(triangle)