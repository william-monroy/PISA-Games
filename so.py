import platform
from os import system

sistema = platform.system()
SO=sistema
print("Sistema Operativo: {}".format(SO))    


def limpiar():
    if SO == 'Windows':
        system('cls')
    elif SO == 'Darwin' or SO == 'Linux':
        system('clear')

def pausa():
    if SO == 'Windows':
        system('pause')
    elif SO == 'Darwin' or SO == 'Linux':
        input('Presione enter para continuar...')

def colores(color):
    if color == 'rojo':
        if SO == 'Windows':
            system('color 4')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 1')
    elif color == 'verde':
        if SO == 'Windows':
            system('color 2')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 2')
    elif color == 'amarillo':
        if SO == 'Windows':
            system('color 6')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 3')
    elif color == 'celeste':
        if SO == 'Windows':
            system('color 3')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 6')
    elif color == 'azul':
        if SO == 'Windows':
            system('color 1')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 4')
    elif color == 'morado':
        if SO == 'Windows':
            system('color 5')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 5')
    elif color == 'blanco':
        if SO == 'Windows':
            system('color 7')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 7')
    elif color == 'gris':
        if SO == 'Windows':
            system('color 8')
        elif SO == 'Darwin' or SO == 'Linux':
            system('tput setaf 8')

def inf_colores():
    if SO == 'Windows':
        print('''0 = Negro       8 = Gris
1 = Azul        
2 = Verde
3 = Celeste
4 = Rojo
5 = Púrpura
6 = Amarillo
7 = Blanco''')

    elif SO == 'Darwin' or SO == 'Linux':
        print('''1. Rojo
2. Verde
3. Amarillo
4. Azul
5. Morado
6. Celeste
7. Blanco
8. Gris''')

