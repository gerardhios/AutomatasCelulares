import os

def aplicarRegla(caracteres:list):
    if len(caracteres) == 2:
        sum = int(caracteres[0]) + int(caracteres[1])
        return 1 if sum == 1 else 0
    else:
        sum = int(caracteres[0]) + int(caracteres[1]) + int(caracteres[2])
        return 1 if sum == 1 else 0
    
def read_file():
    cadena = ""
    if not os.path.exists("inputtext.txt"):
        print("El archivo inputtext.txt no existe, por favor cree el archivo con la cadena de entrada")
    else:
        with open("inputtext.txt", "r") as f:
            cadena = f.readline()
    
    return cadena

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
    cadena = read_file()
    numiter = int(input("Ingrese el numero de iteraciones: "))
    triangle = triangulo(cadena, numiter)
    print_triangle(triangle)