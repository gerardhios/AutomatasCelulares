def aplicarRegla(caracteres:list):
    zeros = 0
    ones = 0
    for c in caracteres:
        if c == '0':
            zeros += 1
        elif c == '1':
            ones += 1
    return 1 if ones > zeros else 0

def mayorityrule(cadena, numiter):
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

def print_out_text(triangle):
    with open("mayorityrule.txt", "w") as f:
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
    triangle = mayorityrule(cadena, numiter)
    print_out_text(triangle)