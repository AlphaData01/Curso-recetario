from pathlib import Path
import os
from os import system

ruta = os.chdir("C:\Users\Luis\Recetas")

def Tabla():
    print("1- leer recta")
    print("2- crear recta")
    print("3- crear categoria")
    print("4- eliminar receta")
    print("5- Eliminar categoria")
    print("6- finalizar programa")

def leer_receta():
    #mostrar categoria
    #elegir categoria
    #Mostrar recetas
    #Elegir receta
    #leer receta

    print("Que categoria quieres: Carnes\n Ensaladas\nPastas\n, Postres\n")
    categoria = input()
    guia = Path(Path.home(),"Recetas",categoria)
    print("Las recetas son )

def crear_receta():
    # mostrar categoria
    # elegir categoria
    # crear receta nueva

def crear_categoria():
    #Crear categoria
    nombre_categoria = input("Elige un nombre para una nueva categoria: ")
    ruta = os.makedirs("C:\Users\Luis\Recetas",nombre_categoria)

def eliminar_receta():
    # mostrar categoria
    # elegir categoria
    # Mostrar recetas
    # Elegir receta
    # Eliminar receta

def Eliminar_categoria():
    # mostrar categoria
    # elegir categoria
    # eliminar categoria

while True:
    system("cls")
    print("Bienvenido a mi recetario")

    base = Path.home()
    print(f"Las recetas están en {base}")

    guia = base / "Recetas"
    contador = 0

    for txt in guia.glob("*.txt"):
        contador += 1

    print(f"Tienes {contador} recetas")

    Tabla()
    entrada = int(input("Elige una opcion: "))
    if(entrada == 1):
        system("cls")
        leer_receta()
    elif(entrada == 2):
        system("cls")
        crear_receta()
    elif(entrada == 3):
        system("cls")
        crear_categoria()
    elif(entrada == 4):
        system("cls")
        eliminar_receta()
    elif(entrada == 5):
        system("cls")
        Eliminar_categoria()
    elif(entrada == 6):
        system("cls")
        print("Hasta luego...")
        break
    else:
        print("Opcion invalida elige otra")

    input("Preciona enter para continuar...")