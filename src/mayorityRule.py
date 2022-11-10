import os
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

def read_file():
    cadena = ""
    if not os.path.exists("inputtext.txt"):
        print("El archivo inputtext.txt no existe, por favor cree el archivo con la cadena de entrada")
    else:
        with open("inputtext.txt", "r") as f:
            cadena = f.readline()
    
    return cadena

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
    cadena = read_file()
    numiter = int(input("Ingrese el numero de iteraciones:\n"))
    triangle = mayorityrule(cadena, numiter)
    print_out_text(triangle)