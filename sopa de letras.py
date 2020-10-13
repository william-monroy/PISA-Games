import random
from os import system

system('cls')

tablero = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
           [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]

palabras = ['HOLA', 'COMO', 'ESTAS', 'MI', 'NOMBRE', 'ES', 'WILLIAM', 'DOMINGO',
            'LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES', 'SABADO', 'DOMINGO']

# Intentar llenar

for p in range(len(palabras)):
    # Tipo de llenado
    '''
    1. Derecha
    2. Izquierda
    3. Arriba
    4. Abajo
    '''
    r_llenar = random.randint(1, 4)
    l = len(palabras[p])
    #print('Llenado: ' + str(r_llenar))
    if r_llenar == 1:
        posible = False
        while not posible:
            # Posicion inicial de Intento de llenado
            r_pos_i = random.randint(0, 11)
            r_pos_j = random.randint(0, 11)

            disponibles = 12 - r_pos_j
            while disponibles < l:
                r_pos_j = random.randint(0, 11)
                disponibles = 12 - r_pos_j
            vacio = False
            cont = 0
            for j in range(r_pos_j, r_pos_j+l):
                if tablero[r_pos_i][j] == ' ':
                    cont += 1
            if cont == l:
                vacio = True
            if vacio:
                letra = 0
                for j in range(r_pos_j, r_pos_j+l):
                    tablero[r_pos_i][j] = palabras[p][letra]
                    letra += 1
                posible = True

    elif r_llenar == 2:
        posible = False
        while not posible:
            # Posicion inicial de Intento de llenado
            r_pos_i = random.randint(0, 11)
            r_pos_j = random.randint(0, 11)
            disponibles = r_pos_j + 1
            while disponibles < l:
                r_pos_j = random.randint(0, 11)
                disponibles = r_pos_j + 1
            vacio = False
            cont = 0
            for j in range(r_pos_j, r_pos_j-l, -1):
                if tablero[r_pos_i][j] == ' ':
                    cont += 1
            if cont == l:
                vacio = True
            if vacio:
                letra = 0
                for j in range(r_pos_j, r_pos_j-l, -1):
                    tablero[r_pos_i][j] = palabras[p][letra]
                    letra += 1
                posible = True
    elif r_llenar == 3:
        pass
    elif r_llenar == 4:
        pass


def printTablero(matriz):
    print('    a b c d e f g h i j k l')
    print('')
    for i in range(len(matriz)):
        if i < 10:
            cor = ' '+str(i)
        else:
            cor = str(i)
        print(cor, end='  ')
        for j in range(len(matriz[i])):
            if matriz[i][j] == '*':
                print("\033[43;44m"+str(matriz[i][j])+"\033[0m", end=' ')
            else:
                print(matriz[i][j], end=' ')
        print('')


def llenarAleatorio(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == ' ':
                letra = chr(random.randint(65, 90))
                matriz[i][j] = letra


def seleccionar(matriz, recorrido):
    print('\nCoordenadas de inicio:')
    ini = input('fila,columna : ').strip().split(',')
    print('\nCoordenadas de fin:')
    fin = input('fila,columna : ').strip().split(',')
    print(ini)
    print(fin)
    if recorrido == 1:
        letra = ''
        for j in range(conver_Letra(ini[1]), conver_Letra(fin[1])+1):
            letra = matriz[int(ini[0])][j]
            matriz[int(ini[0])][j] = '*'
    elif recorrido == 2:
        pass
    elif recorrido == 3:
        pass
    elif recorrido == 4:
        pass


def conver_Letra(letra):
    if letra == 'a':
        return 0
    elif letra == 'b':
        return 1
    elif letra == 'c':
        return 2
    elif letra == 'd':
        return 3
    elif letra == 'e':
        return 4
    elif letra == 'f':
        return 5
    elif letra == 'g':
        return 6
    elif letra == 'h':
        return 7
    elif letra == 'i':
        return 8
    elif letra == 'j':
        return 9
    elif letra == 'k':
        return 10
    elif letra == 'l':
        return 11


#llenarAleatorio(tablero)
printTablero(tablero)
seleccionar(tablero, 1)
print('------------------------------')
printTablero(tablero)
seleccionar(tablero, 1)
print('------------------------------')
printTablero(tablero)
