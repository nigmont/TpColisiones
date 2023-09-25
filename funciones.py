''' TP N°1 - COLISIONES (PROGRAMACION 2) '''

#TODO "IMPORTAR BIBLIOTECA"
''' Llamar a la libreria de colorama'''
from colorama import Fore, init

''' Inicializar colorama '''
init()

import time

#--------------------------------------------------------------------
#TODO "REMOVER RUTAS"
def limpiar():
    import os
    os.system("clear")

#--------------------------------------------------------------------
#TODO "MANEJO TIEMPOS"
def esperar():
    time.sleep(2)

#--------------------------------------------------------------------
# TODO "PERSONALIZAR ENUNCIADO"
''' Esta seccion la hice para tener una introducción con la 
persona que manejará el programa, para personalizarlo.
Notar que hace uso de la libreria de colorama para emitir un
cartel de "espere" dando a entender que hay que esperar un poco
para que el programa cargue. Tambien relacionado con el tiempo
esta la linea time.sleep que se encargará de tomarse un tiempo hasta que comience'''

def saludarJugador():
    jugador=input("Ingrese su nombre...")
    longitud_nombre = len(jugador)
    borde= ("-" * len("Bienvenido: ") + "-" * longitud_nombre)*2
    puntosSuspensivos()
    print(f"\n{borde}" + Fore.RESET)
    print(Fore.CYAN + '\nBIENVENIDO: ' + jugador)
    print("-" * len("Bienvenido: ") + "-" * longitud_nombre + Fore.RESET)

#--------------------------------------------------------------------
#TODO "GENERAR PUNTOS DE ESPERA"
''' Lo que hace esta funcion es contar hasta 3 y en cada contada
agrega un punto pero no todos juntos sino que toma la funcion 
esperar que hace un suspenso de 2 segundos'''
def puntosSuspensivos():
    puntos= 3
    print(Fore.CYAN + "Cargando " + Fore.RESET)
    for i in range(puntos):
        print("     • ", end="", flush=True)
        esperar()

#--------------------------------------------------------------------
#TODO "CREAR PUNTO A COMPARAR"
''' LO QUE HACEN ESTAS FUNCIONES ES PEDIRLE AL USUARIO UN PUNTO
DE COORDENADAS PX Y PY'''
def crearPuntoX():
    print(Fore.LIGHTBLUE_EX + "Creando el punto: "+Fore.RESET)
    Px= int(input("     • Coordenada Px: "))    
    return Px

def crearPuntoY():
    Py= int(input("     • Coordenada Py: "))
    return Py

#--------------------------------------------------------------------
#TODO "CREAR CUADRADO A SER COMPARADO"
''' LO QUE HACE ESTA FUNCION ES PEDIRLE AL USER QUE INGRESE
LOS PUNTOS DEL CUADRADO Y LUEGO SE ALIMENTA DE LA FUNCION
QUE LOS EVALUA PARA IMPRIMIR SI ESTA EL PUNTO EN EL CUADRADO'''

def crearCuadradoyEvaluar():
    # Coordenada A
    print(Fore.MAGENTA + "Creando el cuadrado" + Fore.RESET)
    Ax= int(input("     • Coordenada Ax: "))
    Ay= int(input("     • Coordenada Ay: "))
    # Coordenada B
    Bx= int(input("     • Coordenada Bx: "))
    # Coordenada D
    Dy= int(input("     • Coordenada Dy: "))
    # Coordenada C
    By= Ay
    Cx= Bx
    Cy= Dy
    Dx= Ax
    # Punto solicitado
    Px= crearPuntoX()
    Py= crearPuntoY()
    evaluarPuntoEnCuadrado(Ax,Ay,Bx,By,Dy,Px,Py)
    

#--------------------------------------------------------------------    
#TODO "EVALUAR PUNTO EN CUADRADO"

def evaluarPuntoEnCuadrado(Ax,Ay,Bx,By,Dy,Px,Py):
    if (Ax <= Px and Px <= Bx):
        if (Dy <= Py and Py <= Ay):
            print(Fore.RED + "\nEl punto está dentro del cuadrado" + Fore.RESET)
            print("Representacion:\n ")
            dibujar_cuadrado_con_punto()
            
    else:
        print(Fore.RED + "\nEl punto está fuera del cuadrado" + Fore.RESET)
        dibujar_cuadrado_con_punto_afuera()
        
    input("\nPresione Enter para salir") 


def dibujar_cuadrado_con_punto():
    lado = 5  # Tamaño del cuadrado (lado)
    punto_x = 2  # Coordenada x del punto
    punto_y = 2  # Coordenada y del punto

    for y in range(lado):
        for x in range(lado):
            if (x == 0 or x == lado - 1) and (y == 0 or y == lado - 1):
                print("+", end=" ")
            elif x == 0 or x == lado - 1:
                print("|", end=" ")
            elif y == 0 or y == lado - 1:
                print("-", end=" ")
            elif x == punto_x and y == punto_y:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

def dibujar_cuadrado_con_punto_afuera():
    lado = 5  # Tamaño del cuadrado (lado)
    punto_x = 7  # Coordenada x del punto fuera del cuadrado
    punto_y = 2  # Coordenada y del punto fuera del cuadrado

    for y in range(lado + 2):  # Añadimos 2 filas adicionales para el punto afuera
        for x in range(lado + 2):  # Añadimos 2 columnas adicionales para el punto afuera
            if (x == 0 or x == lado + 1) and (y == 0 or y == lado + 1):
                print("+", end=" ")
            elif x == 0 or x == lado + 1:
                print("|", end=" ")
            elif y == 0 or y == lado + 1:
                print("-", end=" ")
            elif x == punto_x and y == punto_y:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()




def main():
    limpiar()
    saludarJugador()
    crearCuadradoyEvaluar()


# comienza juego




























'''
CA:


if(Px>Ax and Px<Bx):
        if(Py>Ay and Py>Dy):
            print(Fore.BLUE + "El punto esta dentro del cuadrado" + Fore.RESET)
            input("Presione Enter para salir")  
    if(Px>Ax and Px>Bx):
        print(Fore.RED + "El punto esta Fuera del cuadrado" + Fore.RESET)
        input("Presione Enter para salir")
    if(Px<Ax and Px<Bx):
        print(Fore.RED + "El punto esta Fuera del cuadrado" + Fore.RESET)
        input("Presione Enter para salir")
    if(Px==Ax or Px==Bx or Py==Ay or Py==Dy):
        print(Fore.BLUE + "El punto esta dentro del cuadrado" + Fore.RESET)
        input("Presione Enter para salir")
    if(Px>Ax and Px<Bx):
        if(Py>Ay and Py<Dy):
            print(Fore.BLUE + "El punto esta dentro del cuadrado" + Fore.RESET)
            input("Presione Enter para salir")    '''