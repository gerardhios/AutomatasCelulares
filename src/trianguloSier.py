import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def get_triangle(P):
    m = P * 0.5
    n = P * 0.5 + np.array([0.5, 0])
    k = P * 0.5 + np.array([0.25, np.sqrt(3)/4])
    return np.array([m,n,k])

if __name__ == '__main__':
    # triangulo unitario inicial
    triangle = np.array([[0, 0],
                  [1, 0],
                  [0.5, np.sqrt(3)/2]])
    
    # Crea un array que representa el triangulo Sierpinski hasta la etapa deseada
    etapa = 1
    for e in range(etapa):
        triangle = get_triangle(triangle)
    
    # Se procede a graficar el triangulo
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(111, aspect='equal')
    for t in triangle.reshape(3**etapa,3,2):
        ax1.add_patch(mpatches.Polygon(t, fc="y"))
    
    plt.show()