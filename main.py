
from os import system
import time
import random  # Importamos random para numeros al azar
system('color 2')
system('cls')
# LETRAS ASCII
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=VICTORIA!!!%0A
from pygame import mixer
mixer.init()
#mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\init.mp3')
system('cls')
def rint(txt,error):
    while True:
        try:
            str = int(input(txt))
            return str
        except ValueError:
            print(error)
#mixer.music.play()
mixer.music.set_volume(0.25)
system('cls')
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  

''')
time.sleep(1)
system('cls')
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ 

''')
time.sleep(1)
system('cls')
print('''

 ██████  █████  ██████   ██████   █████  ███    ██ ██████   ██████           
██      ██   ██ ██   ██ ██       ██   ██ ████   ██ ██   ██ ██    ██          
██      ███████ ██████  ██   ███ ███████ ██ ██  ██ ██   ██ ██    ██          
██      ██   ██ ██   ██ ██    ██ ██   ██ ██  ██ ██ ██   ██ ██    ██          
 ██████ ██   ██ ██   ██  ██████  ██   ██ ██   ████ ██████   ██████  ██ ██ 

''')
time.sleep(1)
system('cls')
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
system('cls')
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


system('cls')

continuar = True

while continuar == True:
    system('cls')
    mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\main.mp3')
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
        mixer.init()
        mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\matematica.mp3')
        mixer.music.play()
        system('cls')
        cont = True
        while cont == True:
            system('cls')
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
                system('cls')
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
                    system('cls')
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
                            system('pause')
                        else:
                            print(correccion[aleatorio])
                            system('pause')
                            correcto=False
                
            elif op == 2:
                system('cls')
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
                    system('cls')
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
                            system('pause')
                        else:
                            print(correccion[aleatorio])
                            system('pause')
                            correcto=False
            elif op == 3:
                system('cls')
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
                    system('cls')
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
                            system('pause')
                        else:
                            print(correccion[aleatorio])
                            system('pause')
                            correcto=False
            elif op == 4:
                cont = False
                system('pause')
    elif opcion == 2:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\historia.mp3')
        mixer.music.play()
        system('cls')
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
                system('cls')
                print('Disponible pronto...\n')
                system('pause')
            elif opc == 2:
                system('cls')
                print('Disponible pronto...\n')
                system('pause')
            elif opc == 3:
                system('cls')
                print('Disponible pronto...\n')
                system('pause')                
            elif opc == 4:
                seguir = False
                system('pause')
    elif opcion == 3:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\ciencia.mp3')
        mixer.music.play()
        system('cls')
        seg = True
        while seg == True:
            system('cls')
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

                    system('cls')  # Limpiar pantalla
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
                        system('cls')  # Limpiar pantalla
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
                        system('pause')
                        hayganador = True  # Indicamos que hay ganador
                        break  # Salimos del while - Termina el juego

                    # COMPROBAMOS SI PERDIO

                    # Si los errores son igaules a la cantidad de oportunidades hacer:
                    if errores == len(AHORCADO)-1:
                        system('cls')  # Limpiar pantalla
                        print('''


                                ██████╗   █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗ 
                                ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗
                                ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝
                                ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗
                                ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║
                                 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝


                        ''')
                        print('\nLo sentimos no conseguido acertar todas las letras\n')
                        system('pause')
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
                            system('pause')

            if opc == 1:
                system('cls')
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Quién es el autor de E=mc^2?', 'Fórmula Química del Agua', '¿Cuántos planetas tiene el Sistema Solar?', '¿Cuál es un Ph neutro?', '¿A partir del Sol qué número de planeta es la Tierra?']

                # Respuestas
                resCiencia = ['EINSTEIN', 'H2O', 'OCHO', 'SIETE', 'TRES']

                ahorcado(pregCiencia,resCiencia)

            elif opc == 2:
                system('cls')
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Cual es la formula del Dioxido de Carbono?','¿Cual es el primer elemento de la tabla Periodica?']

                # Respuestas
                resCiencia = ['CO2','HIDROGENO']

                ahorcado(pregCiencia,resCiencia)

            elif opc == 3:
                system('cls')
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Como se llama el enlace entre un metal y un no metal?', '¿Cual es elemento de numero atomico de 50?']

                # Respuestas
                resCiencia = ['IONICO','ESTAÑO']

                ahorcado(pregCiencia,resCiencia)

            elif opc == 4:
                seg = False
                system('pause')
            else:
                print('ERROR: Opción Inválida')
                system('pause')
    elif opcion == 4:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\champions.mp3')
        mixer.music.play()
        system('cls')
        system('pause')
                
    elif opcion == 5:
        mixer.music.stop()
        mixer.init()
        mixer.music.load('C:\\Users\\William\\Documents\\TEC21\\Pensamiento Computacional\\PISA Games\\music\\creditos.mp3')
        mixer.music.play()
        system('cls')
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
        system('cls')
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
        system('cls')
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
        system('cls')
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
        system('cls')
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
        system('cls')
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
        system('pause')
    elif opcion == 6:
        system('cls')
        continuar = False
    else:
        print('ERROR: Opción Inválida')
        system('pause')


        
