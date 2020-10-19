
from os import system
import time
import random  # Importamos random para numeros al azar
import platform

# COMPATIBILIDAD DE SISTEMA OPERATIVO ========================================

sistema = platform.system()
SO=sistema
#print("Sistema Operativo: {}".format(SO))    


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

# ============================================================================

system('color 2')
limpiar()
# LETRAS ASCII
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=VICTORIA!!!%0A
from pygame import mixer
mixer.init()
#mixer.music.load('\music\init.mp3')
limpiar()
def rint(txt,error):
    while True:
        try:
            str = int(input(txt))
            return str
        except ValueError:
            print(error)
#mixer.music.play()
mixer.music.set_volume(0.25)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  

''')
time.sleep(1)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ 

''')
time.sleep(1)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ ██ 

''')
time.sleep(1)
limpiar()
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ ██ ██ 

''')
time.sleep(2)
import random
for i in range(100):
    for j in range(150):
        r=random.randint(0,1)
        print(r,end='')
    print()
limpiar()
mixer.music.stop()

# ****************************************************************
# ***********************  AHORCADO  *****************************
# ****************************************************************
# Tablero de Juego
AHORCADO = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']

# Preguntas
pregCiencia = []

# Respuestas
resCiencia = []

errores = 0  # Numero de veces que se equivoco el usuario

linea = []  # Lista donde estaran _ _ _ _ _ _ ...

# *****************************************************************


limpiar()

continuar = True

while continuar == True:
    limpiar()
    mixer.music.load('music/main.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.4)
    system('color 7')
    print('''

______██████████████
-____██▓▓▓▓▓▓▓▓▓ M ▓████
-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██
-__██████░░░░██░░██████
██░░░░████░░░██░░░░░░░░██
██░░░░████░░░░██░░░░░░░██
-__████░░░░░░██████████         ██████╗ ██╗███████╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗███████╗
-__██░░░░░░░░░░░░░██            ██╔══██╗██║██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
_____██░░░░░░░░░██              ██████╔╝██║███████╗███████║    ██║  ███╗███████║██╔████╔██║█████╗  ███████╗
-______██░░░░░░██               ██╔═══╝ ██║╚════██║██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
-____██▓▓████▓▓▓█               ██║     ██║███████║██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
-_██▓▓▓▓▓▓████▓▓█               ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
██▓▓▓▓▓▓███░░███░
-__██░░░░░░███████
-____██░░░░███████
-______██████████
-_____██▓▓▓▓▓▓▓▓▓██
-_____█████████████
                                                                
            \n''')
    print('1) Matemáticas')
    print('2) Historia')
    print('3) Ciencias')
    print('4) Tabla de Posiciones')
    print('5) Creditos del Juego')
    print('6) SALIR\n')
    opcion = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
    if opcion == 1:
        mixer.music.stop()
        mixer.music.load('music/mate.mp3')
        mixer.music.play()
        limpiar()
        cont = True
        while cont == True:
            limpiar()
            print('''
            
___  ___      _                       _   _           
|  \/  |     | |                     | | (_)          
| .  . | __ _| |_ ___ _ __ ___   __ _| |_ _  ___ __ _ 
| |\/| |/ _` | __/ _ \ '_ ` _ \ / _` | __| |/ __/ _` |
| |  | | (_| | ||  __/ | | | | | (_| | |_| | (_| (_| |
\_|  |_/\__,_|\__\___|_| |_| |_|\__,_|\__|_|\___\__,_|
                                                      

            \n''')
            print('Elige un nivel:\n')
            print('1) Principiante ')
            print('2) Intermedio ')
            print('3) Avanzado')
            print('4) Regresar\n')
            op = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
            if op == 1:
                limpiar()
                # PRINCIPIANTE
                
                pregunta = []
                respuesta = []
                correccion = []

                def leer_tipo(nombre_archivo,inicio,fin,salida):
                    txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                    lispreg = txtpreg.readlines()
                    for i in range(inicio,fin+1):
                        lispreg[i]=lispreg[i].replace('\n','')
                        salida.append(lispreg[i])

                leer_tipo('pregunta',1,5,pregunta)
                leer_tipo('respuesta',1,5,respuesta)
                leer_tipo('correccion',1,5,correccion)


                def buscar(lista,valor):
                    if len(lista)==0:
                        return False
                    else:
                        encontrado=False
                        for i in range(len(lista)):
                            if valor==lista[i]:
                                encontrado=True
                                return True
                                break
                            elif i == len(lista)-1 and encontrado==False:
                                return False

                repetidas=[]
                correcto=True
                while correcto==True:
                    limpiar()
                    print('PRINCIPIANTE\n')
                    print('Escribe las respuestas de las prguntas de la forma más simplificada y en fracción\n')
                    if len(repetidas)==len(pregunta):
                        print('Juego terminado')
                        correcto=False
                    else:
                        validado=False
                        while validado==False:
                            aleatorio = random.randint(0,len(pregunta)-1)
                            if buscar(repetidas,aleatorio) == False:
                                validado=True
                                repetidas.append(aleatorio)
                        print(pregunta[aleatorio])
                        res = input('\nRESPUESTA: ')
                        if res == respuesta[aleatorio]:
                            print('Muy bien')
                            pausa()
                        else:
                            print(correccion[aleatorio])
                            pausa()
                            correcto=False
                
            elif op == 2:
                limpiar()
                # INTERMEDIO

                pregunta = []
                respuesta = []
                correccion = []

                def leer_tipo(nombre_archivo,inicio,fin,salida):
                    txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                    lispreg = txtpreg.readlines()
                    for i in range(inicio,fin+1):
                        lispreg[i]=lispreg[i].replace('\n','')
                        salida.append(lispreg[i])

                leer_tipo('pregunta',8,12,pregunta)
                leer_tipo('respuesta',8,12,respuesta)
                leer_tipo('correccion',8,12,correccion)


                def buscar(lista,valor):
                    if len(lista)==0:
                        return False
                    else:
                        encontrado=False
                        for i in range(len(lista)):
                            if valor==lista[i]:
                                encontrado=True
                                return True
                                break
                            elif i == len(lista)-1 and encontrado==False:
                                return False

                repetidas=[]
                correcto=True
                while correcto==True:
                    limpiar()
                    print('INTERMEDIO\n')
                    print('Escribe las respuestas de las prguntas de la forma más simplificada\n')
                    if len(repetidas)==len(pregunta):
                        print('Juego terminado')
                        correcto=False
                    else:
                        validado=False
                        while validado==False:
                            aleatorio = random.randint(0,len(pregunta)-1)
                            if buscar(repetidas,aleatorio) == False:
                                validado=True
                                repetidas.append(aleatorio)
                        print(pregunta[aleatorio])
                        res = input('\nRESPUESTA: ')
                        if res == respuesta[aleatorio]:
                            print('Muy bien')
                            pausa()
                        else:
                            print(correccion[aleatorio])
                            pausa()
                            correcto=False
            elif op == 3:
                limpiar()
                # AVANZADO

                pregunta = []
                respuesta = []
                correccion = []

                def leer_tipo(nombre_archivo,inicio,fin,salida):
                    txtpreg = open(nombre_archivo+'.txt','r',encoding='utf8')
                    lispreg = txtpreg.readlines()
                    for i in range(inicio,fin+1):
                        lispreg[i]=lispreg[i].replace('\n','')
                        salida.append(lispreg[i])

                leer_tipo('pregunta',15,19,pregunta)
                leer_tipo('respuesta',15,19,respuesta)
                leer_tipo('correccion',15,19,correccion)


                def buscar(lista,valor):
                    if len(lista)==0:
                        return False
                    else:
                        encontrado=False
                        for i in range(len(lista)):
                            if valor==lista[i]:
                                encontrado=True
                                return True
                                break
                            elif i == len(lista)-1 and encontrado==False:
                                return False

                repetidas=[]
                correcto=True
                while correcto==True:
                    limpiar()
                    print('AVANZADO\n')
                    if len(repetidas)==len(pregunta):
                        print('Juego terminado')
                        correcto=False
                    else:
                        validado=False
                        while validado==False:
                            aleatorio = random.randint(0,len(pregunta)-1)
                            if buscar(repetidas,aleatorio) == False:
                                validado=True
                                repetidas.append(aleatorio)
                        print(pregunta[aleatorio])
                        res = input('\nRESPUESTA: ')
                        if res == respuesta[aleatorio]:
                            print('Muy bien')
                            pausa()
                        else:
                            print(correccion[aleatorio])
                            pausa()
                            correcto=False
            elif op == 4:
                cont = False
                pausa()
    elif opcion == 2:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('music/historia.mp3')
        mixer.music.play()
        limpiar()
        seguir = True
        while seguir == True:
            print('''

                              /^\\
           L L               /   \               L L
        __/|/|_             /  .  \             _|\|\__
       /_| [_[_\           /     .-\           /_]_] |_\\
      /__\  __`-\_____    /    .    \    _____/-`__  /__\\          _   _ _     _             _       
     /___] /=@>  _   {>  /-.         \  <}   _  <@=\ [___\\        | | | (_)   | |           (_)      
    /____/     /` `--/  /      .      \  \--` `\     \____\\       | |_| |_ ___| |_ ___  _ __ _  __ _ 
   /____/  \____/`-._> /               \ <_.-`\____/  \____\\      |  _  | / __| __/ _ \| '__| |/ _` |
  /____/    /__/      /-._     .   _.-  \      \__\    \____\\     | | | | \__ \ || (_) | |  | | (_| |
 /____/    /__/      /         .         \      \__\    \____\\    \_| |_/_|___/\__\___/|_|  |_|\__,_|
|____/_  _/__/      /          .          \      \__\_  _\____|
 \__/_ ``_|_/      /      -._  .        _.-\      \_|_`` _\___/
   /__`-`__\      <_         `-;           _>      /__`-`__\\
      `-`           `-._       ;       _.-`           `-`
                        `-._   ;   _.-`
                            `-._.-`

            \n''')
            print('Elige un nivel:\n')
            print('1) Principiante ')
            print('2) Intermedio ')
            print('3) Avanzado')
            print('4) Regresar\n')
            opc = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
            if opc == 1:
                limpiar()
                print('Disponible pronto...\n')
                pausa()
            elif opc == 2:
                limpiar()
                print('Disponible pronto...\n')
                pausa()
            elif opc == 3:
                limpiar()
                print('Disponible pronto...\n')
                pausa()                
            elif opc == 4:
                seguir = False
                pausa()
    elif opcion == 3:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('music/cien.mp3')
        mixer.music.play()
        limpiar()
        seg = True
        while seg == True:
            limpiar()
            print('''

                         (``',
                        / `''/
                       /    /
                    O\/    /
                    \,    /
                    (    /                    _____ _                 _       
                   /x`''7/                   /  __ (_)               (_) 
                  (x   //`\\                 | /  \/_  ___ _ __   ___ _  __ _ 
                 / `''7'`\ \\                | |   | |/ _ \ '_ \ / __| |/ _` |
                /    /   /()\\               | \__/\ |  __/ | | | (__| | (_| |
               (    /   `|~~|`                \____/_|\___|_| |_|\___|_|\__,_|
                `\'\'\'     |  |
                         |  |
                         |  |
                         |  |
                         |  |
                       /`    `\\
             ,-------'`        `'-------,
            `~~~~~~~~~~~~~~~~~~~~~~~~~~~~`            
                       
            \n''')
            print('Elige un nivel:\n')
            print('1) Principiante ')
            print('2) Intermedio ')
            print('3) Avanzado')
            print('4) Regresar\n')
            opc = rint('Escribe el número de la opción que quieras: ','Error: Opcion Incorrecta')
            def ahorcado(pregCiencia,resCiencia):
                errores = 0  # Numero de veces que se equivoco el usuario

                hayganador = False  # ¿Hay ganador?

                # Crear Juego

                # Escogemos una pregunta al azar
                pregunta = random.randint(0, len(pregCiencia)-1)

                linea = []  # Lista donde estaran _ _ _ _ _ _ ...

                # Cuántas letras tiene nuestra respuesta
                letras = len(resCiencia[pregunta])

                # For que se repite para la cantidad de letras de la respuesta
                for i in range(letras):
                    # Agregamos una '_' para cada letra de la respuesta
                    linea.append('_')

                # *****************************************************************************

                # El juego se repite hasta que haya un ganador
                while hayganador == False:  # Mientras no haya ganador hacer:

                    # TALBERO

                    limpiar()  # Limpiar pantalla
                    print('\tCiencia\n')
                    # Imprime la tabla de acuerdo a cuantos errores tenga el usuario
                    print(AHORCADO[errores]+'\n')
                    # Muestra una pregunta al azar
                    print(pregCiencia[pregunta]+'\n')

                    # LINEAS

                    # For que se repite para la cantidad de letras de la respuesta
                    for i in range(letras):
                        # Imprime lo que tengamos en la lista 'linea' sin salto de linea
                        print(linea[i], end=' ')
                    print('\n')  # Hacemos un salto de linea

                    # --------------------------------------------------------------------------------------

                    # COMPROBAMOS SI HAY GANADOR

                    contador = 0  # Contador
                    # For que se repite para la cantidad de letras de la respuesta
                    for i in range(letras):
                        # Comprobamos si la posicion actual de 'linea' NO tiene un '_'
                        if linea[i] != '_':
                            contador = contador+1  # Si es que no tiene un '_' sumamos 1 al contador

                    if contador == letras:  # Si 'linea' tiene letras en vez de '_' significa que adivino todo
                        limpiar()  # Limpiar pantalla
                        print('''
                        
                            
                                ██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗ █████╗ ██╗██╗██╗
                                ██║   ██║██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██║██╔══██╗██║██║██║
                                ██║   ██║██║██║        ██║   ██║   ██║██████╔╝██║███████║██║██║██║
                                ╚██╗ ██╔╝██║██║        ██║   ██║   ██║██╔══██╗██║██╔══██║╚═╝╚═╝╚═╝
                                 ╚████╔╝ ██║╚██████╗   ██║   ╚██████╔╝██║  ██║██║██║  ██║██╗██╗██╗
                                  ╚═══╝  ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝╚═╝╚═╝
                                                                                

                        ''')
                        print('\n\t\tFELICIDADES')
                        print('\nHas conseguido acertar todas las letras')
                        pausa()
                        hayganador = True  # Indicamos que hay ganador
                        break  # Salimos del while - Termina el juego

                    # COMPROBAMOS SI PERDIO

                    # Si los errores son igaules a la cantidad de oportunidades hacer:
                    if errores == len(AHORCADO)-1:
                        limpiar()  # Limpiar pantalla
                        print('''


                                ██████╗   █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                                ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                                 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


                        ''')
                        print('\nLo sentimos no conseguido acertar todas las letras\n')
                        pausa()
                        break  # Salimos del while - Termina el juego

                    # ----------------------------------------------------------------------------------------

                    # LOGICA

                    # Pide una letra al usuario y la convierte a Mayus
                    letra = input('Introduce una letra: ').upper()
                    encontrado = False  # Creamos una variable para saber si encontramos lo que buscamos

                    # BUSCAMOS LA LETRA EN LA RESPUESTA

                    # For que se repite para la cantidad de letras de la respuesta
                    for x in range(letras):
                        # Si 'letra' es igual a respuesta[letra actual]
                        if letra == resCiencia[pregunta][x]:
                            linea[x] = letra  # Reemplazamos '_' por la 'letra'
                            encontrado = True  # Indicamos que encotramos la 'letra' en la respuesta
                        elif x == letras-1 and encontrado == False:
                            # Si estamos en la ultima vuelta y no se ha encontrado:
                            # Indicamos que no esta
                            print(":'( "+letra+' no esta')
                            errores = errores+1  # Agregamos un error al usuario
                            # Nos pide una tecla para continuar
                            pausa()

            if opc == 1:
                limpiar()
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Quién es el autor de E=mc^2?', 'Fórmula Química del Agua', '¿Cuántos planetas tiene el Sistema Solar?', '¿Cuál es un Ph neutro?', '¿A partir del Sol qué número de planeta es la Tierra?']

                # Respuestas
                resCiencia = ['EINSTEIN', 'H2O', 'OCHO', 'SIETE', 'TRES']

                ahorcado(pregCiencia,resCiencia)

            elif opc == 2:
                limpiar()
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Cual es la formula del Dioxido de Carbono?','¿Cual es el primer elemento de la tabla Periodica?']

                # Respuestas
                resCiencia = ['CO2','HIDROGENO']

                ahorcado(pregCiencia,resCiencia)

            elif opc == 3:
                limpiar()
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Como se llama el enlace entre un metal y un no metal?', '¿Cual es elemento de numero atomico de 50?']

                # Respuestas
                resCiencia = ['IONICO','ESTAÑO']

                ahorcado(pregCiencia,resCiencia)

            elif opc == 4:
                seg = False
                pausa()
            else:
                print('ERROR: Opción Inválida')
                pausa()
    elif opcion == 4:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('music/champions.mp3')
        mixer.music.play()
        limpiar()
        pausa()
                
    elif opcion == 5:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('music/creditos.mp3')
        mixer.music.play()
        limpiar()
        print('''

        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░▒▒▒▒░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒░▒▒▒▒▒▒░░░░░▓▓
        ▓▓░░░░░░WE░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░░░░░░▓▓
        ▓▓░░░░░░░░░LOVE░░░░░░░░░░░▒▒▒▒▒░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░PYTHON░░░░░░░░▒▒▒░▒▒▒░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒░░░░░▓▓
        ▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░░░░░░▓▓
        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        _______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ______▒_______________▒▒▒▒▒▒▒▒
        _____▒________________▒▒▒▒▒▒▒▒
        ____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
        ___▒
        __▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        _▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
        ▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
        ▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
        ▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
        ▒▒

        ''')
        time.sleep(5)
        limpiar()
        print('''
   ===============================================================================================================
   ===============================================================================================================

                            ██████ ██████  ███████ ██████  ██ ████████  ██████  ███████ 
                           ██      ██   ██ ██      ██   ██ ██    ██    ██    ██ ██      
                           ██      ██████  █████   ██   ██ ██    ██    ██    ██ ███████ 
                           ██      ██   ██ ██      ██   ██ ██    ██    ██    ██      ██ 
                            ██████ ██   ██ ███████ ██████  ██    ██     ██████  ███████ 
                                                             
   ===============================================================================================================
   ===============================================================================================================
                                                             
        ''')
        time.sleep(5)
        limpiar()
        system('color 2')
        print('''
                         ██╗    ██╗██╗██╗     ██╗     ██╗ █████╗ ███╗   ███╗
                         ██║    ██║██║██║     ██║     ██║██╔══██╗████╗ ████║
                         ██║ █╗ ██║██║██║     ██║     ██║███████║██╔████╔██║
                         ██║███╗██║██║██║     ██║     ██║██╔══██║██║╚██╔╝██║
                         ╚███╔███╔╝██║███████╗███████╗██║██║  ██║██║ ╚═╝ ██║
                          ╚══╝╚══╝ ╚═╝╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝  
        ''')
        time.sleep(3)
        print('''

        ..........................................................................................
        ..........................................................................................
        ..............................................::--:.:.....................................
        ...................................:::-**##%%%%##%#*+=-::.................................
        .................................-+*#######%#%%%%@@%%%#*=-:...............................
        ...............................:*###%%##%%%@@@%%%@%%@%%%*=::..............................
        .............................:+##%%%%%%@@@@@@%@@@@@@@@@@@%+:..............................
        ............................+#%#%@@@@@@@@@@@%%@@@@@@@@@@@@%-:.............................
        ..........................:+#%%%@@@%#+++*#%%%%#####%%%%@@@@%+:............................
        ..........................-%%##%%#*=:::::--======++**##%@@@@%*............................
        ..........................:#%##*-::::..:::::----===+++*#@@@@@%:...........................
        :..........................*%%%+:::::--------=+*###**#**#@@@@+............................
        ...........................*%%%-:----=+**+-:-+#%%#**##***%@@@*............................
        ...........................#%%+:::-=+*#**-:::=###+*##%#***%@@+:...........................
        ...........................*%%-:::---=+=-::::-+**+====++++#@###:..........................
        :........................:=-*#:::::::::::::::-=+++==--=+++#%#*#-..........................
        -:.......................=:::+::::..:::::-+==*##***++=++***%#*+...........................
        -:.......................:::==::::::::--:--:=+*#*************+:...........................
        ...........................:-::::::::--::::--=+****#********+=............................
        ............................:::::::::-=======++*##%%******=-:.............................
        .............................::::::::-+-:::--==+*********+................................
        ................................:::::::::::---==+********:................................
        ................................:-:::::::::::--==++*****=.................................
        .................................:---::::::-==+******##*:::...............................
        ..................................:--======+******#####+-::...............................
        ..................................:::--==+**############@%*::.............................
        ..................................:::::::---+###########%%+--:::..........................
        ................................:++:::::::--+******######+----::::.................::.....
        .....................:----.:::..:#+::::::::--=+*******#+=:::::-----::::..:.:::::::::::::::
        ...............::-:--::::::... .:-+-:::::::--=++==++++--++*+=-::::-----:::::::::::::::::::
        ..........::----:::::-:::...   .::-=-::::::--------:-=+**#####*+=------::::::.::::::::::::
        ::::::::---:::::-:::..          :----...:::::::-===++**********++==-----:::.....::::::::::
        :::--::::::-::...             .=+=--=-.....::-=******++++++++=++===----:::......:::--:::::
        -::::--:::..                .-+=-:..-=-:::::===-=--::::-----------:......::::::::::-==::::
        ---::.......              .:=:.            --::.:.....................:::::::::----===....
        --:-::-:.:.                               ..:..:...................::::::::----====-==:...
        ------=*=-                                .....:......................:.::-----====-==:...
        +++++=+**:                               ......:........................:------=====-=:...
        ''')
        time.sleep(3)
        limpiar()
        system('color 5')
        print('''
        ███████╗███████╗███╗   ██╗██╗   ██╗███████╗ ██████╗███████╗████████╗██╗  ██╗
        ╚══███╔╝██╔════╝████╗  ██║╚██╗ ██╔╝██╔════╝██╔════╝██╔════╝╚══██╔══╝██║  ██║
          ███╔╝ █████╗  ██╔██╗ ██║ ╚████╔╝ █████╗  ██║     █████╗     ██║   ███████║
         ███╔╝  ██╔══╝  ██║╚██╗██║  ╚██╔╝  ██╔══╝  ██║     ██╔══╝     ██║   ██╔══██║
        ███████╗███████╗██║ ╚████║   ██║   ███████╗╚██████╗███████╗   ██║   ██║  ██║
        ╚══════╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝ ╚═════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
        ''')
        time.sleep(3)
        print('''
        :::::--------====--=*####%###########*+=-::::::::::::::::::::::::::...::::
        ::::::::::-----=+*######%%%####%%%%%%#**+=-::::::::::::::::::::::::::..:::
        :::::::::::---=*######%%#####***##%%%%%#**+-::::::::::::::::::::::::::::::
        ::::::::::::-+#############*+=---=+#%%%%%#*+-:::::::::::::::::::::::::::::
        ::::::::::::+###########*+=--::::::-=*%%%%#*+-::::::::::::::::::::::::::::
        :::::::::::+#####%%###*=---::::::::::-=#%%%#*+-:::::::::::::::::::::::::::
        ::::::::::=######%###+--:::::::::::::::-#%%%#*=:::::::::::::::::::::::::::
        :::::::::-*#%#%#%%##*---===--:::::::::::=#%%%#+-::::::::::::::::::::::::::
        :::::::::+#%#%%#%%#*=-+++=+***+-::::::::-*%%%%*=::::::::::::::::::::::::::
        ::::::::-##%%%#%%#*+=-:::::::=+++-:::::::=%%%%#+-:::::::::::::::::::::::::
        ::::::::=#%%%%%%%#+=:::-----:::---::::--:-#%%%#*-:::::::::::::::::::::::::
        ::::::::+%%%%%%%#+-:::-+*###==-::::.:-+**+*%%%%#=:::::::::::::::::::::::::
        :::::::-##%%%%%#+=::::::-=++=+=::::::---=+#%%%%#+-::::::::::::::::::::::::
        :::::::=%%%%%%#+-::::::::::---:::::::-=-:-*%%%%%#=-:::::::::::::::::::::::
        :::::::+%%%%%#*-:::::...:::::::::::::+#*+*#%%%%%#+-:::::::::::::::::::::::
        :::::::*%%%%%#=--:::::.....:::::::::::-=+#%%%%%%#*=--:::::::::::::::::::::
        ::::::-#%%%%%*=--:::::......::-::::..::::=%%%%%%%#+=-:::::::::::::::::::::
        ::::::=#%%%%%+=---::::::::.:::--+++-::::::*%%%%%%#*=--::::::::::::::::::::
        ::::::+#%%%%%+-----:::::::::::---:---+::::+@%%%%%##+=--:::::::::::::::::::
        :::::-*%%%%%%+----::::::::::::::::::--:::-*@%%%%%%#+=----:-:::::::::::::::
        :::::-#%%%%%%#---:::::::--=-------:::-:::=%%%%%%%##*===-----::::::::::::::
        :::::-#%%%%%%%+---:::::::-==++++++++=---=#@%%%%%%%##+=-=--------::::::::::
        :::::-#%%%%%%%*=---:::::::::---=====++==#@@@%%%%%%##*==-=---------::::::::
        :::::=#%%%%%%%+++-----:::::::---=====-=*@@@@@%%%%%%##*+===-----------::::-
        :::::*%%%%%%%#==++=----:::::::::-----=*%@@@@@%%%%%%%##*+===---------------
        ::::-#%%%%%@%*====++==---:::::::::--+*%%%%%%%%%%%%%%####**+=--------------
        ::::+%%%%%%@@+=--==+++++=--::::::--=#%%%%##%%%%%%%%%%#####*++++=----------
        :::-*%%%%@@@%=-----==+****+=-----=*%%%#######%%%%%%%#######*+++++=--------
        ::-+#%%%@@@@%--------==+***######%@%%##########%%%######%###**+==++==-----
        ::=*%%%@@@%%+-:-------=++*##%%%%%%%%%%#################%#####**+++++======
        -=*#%%%@@%##*=-----==+*##%%%%%%%%%%%%%%################%%####***+++++=====
        -+**%%@@@%##########%%%%%%%%%%%%%%%%%%%%%##########%#####%####**++++++====
        +**%%@@%%############%#%%%%%%%%%%%%%%%%%%%%######%%%%##########*+++++*+===
        ***%@@%############%%%%%%%%%#####%%%%%%%%%%%####%%%%%###########*+==+++++=
        *+#%%%%############################+#%%%%%%%%%%%%%%%%############*++==++++
        **%#%#%########################*=-:=+%%%%%%%%%%%%%%%%%##*#########**+=====
        +#%##%######################+=--=++**%%%%%%%%%###%%%%%####*########**+++==
        ######%#####################====+*#######%%%#########################*++++
        ######%%###########################################***####*###########*+++
        #######%###########################################****####*########*##*-=
        #######%%########################################*******####*#########*+=:
        ########%#########################################*******####**#%%#%##*+-:
        ########%%########################################********####**#%%%##**-:
        #########%#########################################********####++#%%###=-.
        ##########%#########################################********####++####+--.
        ###########%#########################################*******####*++###+:::

        ''')
        time.sleep(3)
        system('color 4')
        limpiar()
        print('''
                            █████╗ ███╗   ██╗ █████╗ 
                           ██╔══██╗████╗  ██║██╔══██╗
                           ███████║██╔██╗ ██║███████║
                           ██╔══██║██║╚██╗██║██╔══██║
                           ██║  ██║██║ ╚████║██║  ██║
                           ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
        ''')
        time.sleep(3)
        print('''
        *++##=-++%%@@%%%%%#%#%%##*-*+*-                      .------:::::::::::
        -+==**++*%%@@#*####%%%%#%%##**:.. :                  .:-----:::::::::::
        +-:.*##+#%@%%%%%%##%@@%%%%%+:  .-.-==:                :-----:::::::::::
        *++*##**%%%%#*#%%%%%%**###*=.. ::*=:-=...      ..     .:-:.::::::::::::
        ########%%%%#*#%#%%#***++*++**++=:-:=++*+:    ...      ::: .::::::..:::
        #####%#%%%%%#%%%%%####*+++=*###%#*+=+###+:  :   .      .:: .::::::..:::
        ######%%%%%%%%%%%%%%*=+##*####%%%%%#**###*.:=:...     ..:::::::::::::::
        *#%###%%@%@%%%%%%%%#=+#%%#%@%%%%%%%%%###+:  .-...      ..::.::.-=-=====
        #%#%#%%@%@%%%%%%%%#-=*#%%***#%%%%%%%%%#**-::.......      ....:+#**####*
        #%*#%%%%%%%%%%##%#-:=#%%*+=++*#%@%%%%%%#*=:........       .  .:==+*****
        +*%%%%%%%%%%#####+::+%%*++====+*%%%%%%%%#.. ....::.           :-=*++***
        #*##%%%%%%%#+###*-..+@#++====+##*#%%%%%%%+.   ...:.        .:+**==++*+*
        *=*%%%%%%%%*#%%#+...*%%*++++*######%%%%%%%=.  ...:.     .-+##**+=++****
        *+*%%%%###*=%%%%+.--*%%#**++*###*++*%%%%%%%-.......  .-*#***++++==++***
        #%%%%%###==+###*-.=-*%%%%##+=+**+===#%%%%%%#:.....::::-+++++++++==++***
        %%%%%%*%*=+=***=:.+=+%%%%%#*========+%%%%%%%#:---::..:-==+++++++==++***
        %%%%%%%#**##*#*=.:+=+%%%%#**===+++==+##%%%%%%#*-.::...:=-==++=++==+++**
        #%%%%%#*#**+*#*::-+++%%%#****+**+=+=+##%%%%%%%#+-::...:--++====+==+*+**
        #%#%%###*==+*+-..=***%%%%***#**+++*++#%%@%%%%%%+-::..::-=+++===+==+****
        #####*+#*=**++-.:=##*%%@%#***####*+++*%%@@%%%%%+-:::.:::+=========*****
        #####==**#**++-.-+#*#%%@@@%#####*+=++#%%%@%%%%%+-:::.:::====-==--=++***
        #####*+=:-=*++::+*#*#%%%@@@%##*++++*#%%%%%%@%%*=--::...::-:--=-:-=+****
        #####**++++*+-.=+#*##%%%%@@@%%##**#%%%%%%@@%#+*=-:::..::::::--:--==+***
        *####+++==---::++#+##%%#%@@@@@@%%%%%%%%@%%#*+==##+-:...:::::::---=++***
        *****-::::::::-*=#**##%*#%@@@@%%###%%%%##*++==%@@%%#+=-::::...-=-==****
        =++++-------===*-#*##%%*#%@%%%%%####***+*++==#@@@%@@%%%%#+:...:-:-=****
        ==+==---======+*+####%%%%%@%#######**+++++++#@@@%@@@@@%@@%%*:..::-+****
        =====-=========*#@@%#%%%@@@@%******+++**++=+@@@%@@@@@@@@@@@@%-...-=++**
        ======++=====-*%%@@@%%@@@@@@@*+++++++++++=+%@@@@@@@@@@@@@@@@@#.::-=****
        ===========+++%@@@@@%%@@@@@@@%+++++++==+==#@@@%@@@@@@@@@@@@@@%-:.:=++**
        ============+#%@@@@@@%@@@@@@@@*++====++==+@@@%@@@@@@@@@@@@@@@%+..-=+***
        ============#%%@@@@@@@@@@@@@@@%+=========%@@@@@@@@@@@@@@@@@%%%*::-=++**
        ============##%%@@@@@@@@@@@@@@@%+=======*@@@%@@@@@@@@@@@@@%@@@%:.:=+***
        +++++======+%%@@%%@@@@@@@@@@@@@@%=======%@@%@@@@@@@@@@@@@@@@@@@=..=+***
        +++++++====*@%@@@@@@@@@@@@@@@@@@@%=====#@@@@@@@@@@@@@@@@@@@@@@@*:.=++**
        +***##**#**%@@@@@@@@@@@@@@@@@@%@@@%===+@@@@@@@@@@@@@@@@@@@@@@@@#.:-+***
        **##******+@@@@@@@@@@@@@@@@@@@@%@@@#++%@@%@@@@@@@@@@@@@@@@@@@@@%..-=+**
        **********+@@@@@@@@@@@@@@@@@@@@@%@@@%%@@@@@@@@@@@@@@@@@@@@@@@@@%:.-=***
        ++++*******@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@:.-=***
        =====+++++%@@@@@@@@@@@@@@@@@@@@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:-=+**
        =========+%@@@@@@@@@@@%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@====+++
        ===--=-==+%@@@@@%#+=----========+*%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@==++***
        =------=-*%@@@%+---==-=============+%@@@@@@@@@@@@@@@@@@@@@@@@@@%==+****
        ----===--%%@@*++===-==============++%**#@@@@@@@@@@@@@@@@@@@@@@@%==+****
        :--=----=%%@**+=+*=++=====+++++++++#%++++*#%@@@@@@@@@@@@@@@@@@@%==+****
        --------=%@@@#+#*=+*++++++**#%%#**#%#**#+++++*#%@@%%@@@@@@@@@@@#+=+****
        -----:::=@@%%+##+*#++##%%@@@@@@@@%%***#*++++++++++*#%@@@@@@@@@@#+++*###
        :-:::::-=@@@#*@*+#**#@@@@@@@@@@@@@%##*#*+++++++++++++*%@%%@@@@@***+*###

        ''')
        time.sleep(3)
        limpiar()
        system('color 7')
        print('''
                                                                                
                                                                        
                                                                        
                                                                        
                              .:::---::..                               
                         :-+*######+######*=-:                          
                     .-+###########:.*#####*##*+-.                      
                   :+#############*  .#####.+#####+:                    
                 :*##############*.   *###- .*######+:                  
               :+###############+.   .###=   +########+.                
              =###############*-    .*#*-    *##########-               
            .+###############+.    :*#+.    =#**#########+.             
           .*##############*-    .=#*-     =#*.-##########*.            
          .*##############=.    -*#+.    :*#+. :#####-#####*.           
         .*#############*:    .+#*:    .=##-   -###*: *#####*           
         +#############=     -*#=     :*#+.   .*##*.  +######=          
        -############+.    .+#+:    .+#*-    .+##=    *#######:         
        *##########*-     =#*-     -*#+.    :*#*:    =########*         
       -##########+.    :*#+.    .+#*:    .+##-     =##########:        
       +#########+    .=#*:     =##=.    -*#+.    :*###########=        
       *########*    :*#=.    :*#*:    .+#*-    .=##+-#########*        
      .#########:   -##-    .+##-     =##=.    :*#*- :##########        
      :#########.  :##-    -*#+.    :*#*:    .+##=.  -##########.       
      :#########.  +#+   .+#*-    .=##=     -*#*:   .*##########.       
      .#########- .##-  .*#*.    :*#+.    .+#*-    .+###########.       
       *########*..##:  +#*.   .+##-     =##+.    :*###########*        
       +#########*.*#= =##:   .*#*:    :*#*:    .+#############=        
       -##########**#*.*#+   .*##:    =##+.    -*##############:        
        *#############*##-   *##=    +##*.   .+###############*         
        -################:  -###:   +###:   -#################:         
         +###############-  *###-  =###*   =#################+          
         .*##############*. ####* .####*  =#################*.          
          :*##############+.*####=:#####::#################*.           
           :*##############**#####*#####**################*.            
            .*#####*-------------------------------*#####*.             
             .+#####=.                           .+#####=               
               :*####*-.                       .=*####*:                
                 -*#####+-.                 .-+#####*-                  
                   -+######*+=-:       :-=+*######+:                    
                     .=*#######*       *#######+-.                      
                        .-=+*##*       *##*+=:.                         
                             .::       ::.                              
                                                                        
                                                                        
                                                                        
                                                                        

        ''')
        pausa()
    elif opcion == 6:
        limpiar()
        continuar = False
    else:
        print('ERROR: Opción Inválida')
        pausa()


        
