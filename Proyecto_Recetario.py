from pathlib import Path
import os
from os import system

def contador_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def Tabla():
    print("1- leer recta")
    print("2- crear recta")
    print("3- crear categoria")
    print("4- eliminar receta")
    print("5- Eliminar categoria")
    print("6- finalizar programa")

def leer_receta():
    print("leer recta")
    #mostrar categoria
    #elegir categoria
    #Mostrar recetas
    #Elegir receta
    #leer receta

def crear_receta():
    print("crear receta")
    # mostrar categoria
    # elegir categoria
    # crear receta nueva

def crear_categoria():
    #Crear categoria
    nombre_categoria = input("Elige un nombre para una nueva categoria: ")
    ruta_base = r"C:\Users\Luis\Recetas"
    ruta_categoria = os.path.join(ruta_base, nombre_categoria)

def eliminar_receta():
    print("eliminar receta")
    # mostrar categoria
    # elegir categoria
    # Mostrar recetas
    # Elegir receta
    # Eliminar receta

def Eliminar_categoria():
    print("eliminar categoria")
    # mostrar categoria
    # elegir categoria
    # eliminar categoria

while True:
    system("cls")
    print("=" * 47 )
    print("Bienvenido a mi recetario")
    print("=" * 47)
    mi_ruta = Path(Path.home(),"Recetas")
    print(f"Las recetas están en {mi_ruta}")
    print(f"Total de recetas en {contador_recetas(mi_ruta)}")

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