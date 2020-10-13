
from os import system
import random  # Importamos random para numeros al azar

# LETRAS ASCII
# http://patorjk.com/software/taag/#p=display&f=ANSI%20Shadow&t=VICTORIA!!!%0A


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
    print('''
    
██████╗ ██╗███████╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗███████╗
██╔══██╗██║██╔════╝██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝██╔════╝
██████╔╝██║███████╗███████║    ██║  ███╗███████║██╔████╔██║█████╗  ███████╗
██╔═══╝ ██║╚════██║██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  ╚════██║
██║     ██║███████║██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗███████║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝╚══════╝
                                                                           
            \n''')
    print('1) Matemáticas')
    print('2) Historia')
    print('3) Ciencias')
    print('4) SALIR\n')
    opcion = int(input('Escribe el número de la opción que quieras: '))
    if opcion == 1:
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
            op = int(input('Escribe el número de la opción que quieras: '))
            if op == 1:
                system('cls')
                print('PRINCIPIANTE\n')
                print('Escribe las respuestas de las prguntas de la forma más simplificada y en fracción')
                p1 = input('1. Teclea la respuesta de 3/6 + 2/3: ')
                if p1 == '7/6':
                    print('¡Correcto!\n')
                    system('cls')
                    p2 = input('2. Teclea la respuesta de 4/9 + 1/2: ')
                    if p2 == '17/18':
                        print('¡Correcto!\n')
                        system('cls')
                        p3 = input('3. Teclea la respuesta de 5/6 - 6/8: ')
                        if p3 == '1/12':
                            print('¡Correcto!\n')
                            system('cls')
                            p4 = input('4. Teclea la respuesta de 3/5 - 2/8: ')
                            if p4 == '7/20':
                                print('¡Correcto!\n')
                                system('cls')
                                p5 = input(
                                    '5. Teclea la respuesta de 3/7 * 1/6: ')
                                if p5 == '1/14':
                                    print(
                                        '¡Felicidades, haz completado correctamente el nivel!\n')
                                    system('pause')
                                else:
                                    system('cls')
                                    print('INCORRECTO')
                                    print('Pasos:')
                                    print(
                                        'Multiplicar numeradores= 3*1 -> 3, y denominadores= 7*6 -> 42, el resultado sería 3/42')
                                    print(
                                        'Simplificar para que salga la respuesta correcta -> 1/14')
                                    print(
                                        'Se te regresará al menú de matemáticas')
                                    system('pause')
                            else:
                                system('cls')
                                print('INCORRECTO')
                                print('Pasos:')
                                print(
                                    'Buscar el común denominador-> 40, dividir 40 por el primer denominador y multiplicar el resultado por el numerador-> 40/5=8>> 8*3=24, se hace lo mismo con la otra fracción')
                                print(
                                    'Después, se restan los resultados -> 24-10=14, por lo que la respuesta daría 14/40')
                                print('Simplifica para que te de el resultado 7/20')
                                print('Se te regresará al menú de matemáticas')
                                system('pause')
                        else:
                            system('cls')
                            print('INCORRECTO')
                            print('Pasos:')
                            print('Buscar el común denominador-> 24, dividir 24 por el primer denominador y multiplicar el resultado por el numerador-> 24/6=4>> 4*5=20, se hace lo mismo con la otra fracción')
                            print(
                                'Después, se restan los resultados -> 20-18=2, por lo que la respuesta daría 2/24')
                            print('Simplifica para que te de el resultado 1/12')
                            print('Se te regresará al menú de matemáticas')
                            system('pause')
                    else:
                        system('cls')
                        print('INCORRECTO')
                        print('Pasos:')
                        print('Buscar el común denominador-> 18, dividir 18 por el primer denominador y multiplicar el resultado por el numerador-> 18/9=2>> 2*4=8, se hace lo mismo con la otra fracción')
                        print(
                            'Después, se suman los resultados -> 8+9=17, por lo que la respuesta daría 17/18')
                        print(
                            'Se queda 17/18 como resultado porque no se puede simplificar')
                        print('Se te regresará al menú de matemáticas')
                        system('pause')
                else:
                    system('cls')
                    print('INCORRECTO')
                    print('Pasos:')
                    print('Buscar el común denominador-> 6, dividir 6 por el primer denominador y multiplicar el resultado por el numerador-> 6/6=1>> 1*3=3, se hace lo mismo con la otra fracción')
                    print('Después, se suman los resultados -> 3+4=7, por lo que la respuesta daría 7/6')
                    print('Se queda 7/6 como resultado porque no se puede simplificar')
                    print('Se te regresará al menú de matemáticas')
                    system('pause')

            elif op == 2:
                system('cls')
                print('INTERMEDIO\n')
                print('Escribe las respuestas de las prguntas de la forma más simplificada')
                p1 = input('1. Teclea la respuesta de x + 4 = 8: ')
                if p1 == '4':
                    print('¡Correcto!\n')
                    system('cls')
                    p2 = input('2. Teclea la respuesta de 2x + 6 = 10: ')
                    if p2 == '2':
                        print('¡Correcto!\n')
                        system('cls')
                        p3 = input('3. Teclea la respuesta de 4x-3 = 21: ')
                        if p3 == '6':
                            print('¡Correcto!\n')
                            system('cls')
                            p4 = input(
                                '4. Teclea la respuesta de (x/2) - 6 = 12: ')
                            if p4 == '36':
                                print('¡Correcto!\n')
                                system('cls')
                                p5 = input(
                                    '5. Teclea la respuesta de (x/3) + 23 = 5: ')
                                if p5 == '-54':
                                    print(
                                        '¡Felicidades, haz completado correctamente el nivel!\n')
                                    system('pause')
                                else:
                                    system('cls')
                                    print('INCORRECTO')
                                    print('Pasos:')
                                    print(
                                        'Mover el 23 al otro lado del igual pero con signo contrario -> x/3 = 5 - 23; sumar los numeros -> x/3 = -18')
                                    print(
                                        'Pasar al 3 con la operación contraria (se está dividiendo, pasa multiplicando) y con el mismo signo. x = -18 * 3 -> x = -54')
                                    print('La respuesta es -54')
                                    print(
                                        'Se te regresará al menú de matemáticas')
                                    system('pause')
                            else:
                                system('cls')
                                print('INCORRECTO')
                                print('Pasos:')
                                print(
                                    'Mover el -6 al otro lado del igual pero con signo contrario -> x/2 = 12 + 6; sumar los numeros -> x/2 = 18')
                                print('Pasar al 2 con la operación contraria (se está dividiendo, pasa multiplicando) y con el mismo signo. x = 18 * 2 ->x = 36')
                                print('La respuesta es 36')
                                print('Se te regresará al menú de matemáticas')
                                system('pause')
                        else:
                            system('cls')
                            print('INCORRECTO')
                            print('Pasos:')
                            print('Mover el -3 al otro lado del igual pero con signo contrario -> 4x = 21+3; sumar los numeros -> 4x = 24')
                            print('Pasar al 4 con la operación contraria (se está multiplicando, pasa dividiendo) y con el mismo signo. x = 4/24 ->x = 6')
                            print('La respuesta es 6')
                            print('Se te regresará al menú de matemáticas')
                            system('pause')
                    else:
                        system('cls')
                        print('INCORRECTO')
                        print('Pasos:')
                        print('Mover el 6 al otro lado del igual pero con signo contrario -> 2x = 10-6; restar los numeros -> 2x = 4')
                        print('Pasar al 2 con la operación contraria (se está multiplicando, pasa dividiendo) y con el mismo signo. x = 4/2 ->x = 2')
                        print('La respuesta es 2')
                        print('Se te regresará al menú de matemáticas')
                        system('pause')
                else:
                    system('cls')
                    print('INCORRECTO')
                    print('Pasos:')
                    print(
                        'Mover el 4 al otro lado del igual pero con signo contrario -> x= 8-4')
                    print(
                        'Restar los números 8-4=2,->x = 2, por lo que la respuesta sería 4')
                    print('Se te regresará al menú de matemáticas')
                    system('pause')
            elif op == 3:
                system('cls')
                print('AVANZADO\n')
                print('Disponible pronto...\n')
                system('pause')
            elif op == 4:
                cont = False
                system('pause')
    elif opcion == 2:
        system('cls')
        seguir = True
        while seguir == True:
            print('''
            
 _   _ _     _             _       
| | | (_)   | |           (_)      
| |_| |_ ___| |_ ___  _ __ _  __ _ 
|  _  | / __| __/ _ \| '__| |/ _` |
| | | | \__ \ || (_) | |  | | (_| |
\_| |_/_|___/\__\___/|_|  |_|\__,_|
                                   
                                   

            \n''')
            print('Elige un nivel:\n')
            print('1) Principiante ')
            print('2) Intermedio ')
            print('3) Avanzado')
            print('4) Regresar\n')
            opc = int(input('Escribe el número de la opción que quieras: '))
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
        system('cls')
        seg = True
        while seg == True:
            system('cls')
            print('''
            
 _____ _                 _       
/  __ (_)               (_)      
| /  \/_  ___ _ __   ___ _  __ _ 
| |   | |/ _ \ '_ \ / __| |/ _` |
| \__/\ |  __/ | | | (__| | (_| |
 \____/_|\___|_| |_|\___|_|\__,_|
                                 
                                 
            \n''')
            print('Elige un nivel:\n')
            print('1) Principiante ')
            print('2) Intermedio ')
            print('3) Avanzado')
            print('4) Regresar\n')
            opc = int(input('Escribe el número de la opción que quieras: '))
            if opc == 1:
                system('cls')
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Quién es el autor de E=mc^2?', 'Fórmula Química del Agua', '¿Cuántos planetas tiene el Sistema Solar?', '¿Cuál es un Ph neutro?', '¿A partir del Sol qué número de planeta es la Tierra?']

                # Respuestas
                resCiencia = ['EINSTEIN', 'H2O', 'OCHO', 'SIETE', 'TRES']

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

            elif opc == 2:
                system('cls')
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Cual es la formula del Dioxido de Carbono?','¿Cual es el primer elemento de la tabla Periodica?']

                # Respuestas
                resCiencia = ['CO2','HIDROGENO']

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
                        print('\nHas conseguido acertar todas las letras\n')
                        hayganador = True  # Indicamos que hay ganador
                        system('pause')
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

            elif opc == 3:
                system('cls')
                # *****************************************************************************
                # Creamos un Juego nuevo

                # Preguntas
                pregCiencia = ['¿Como se llama el enlace entre un metal y un no metal?', '¿Cual es elemento de numero atomico de 50?']

                # Respuestas
                resCiencia = ['IONICO','ESTAÑO']

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
                        print('\nHas conseguido acertar todas las letras\n')
                        hayganador = True  # Indicamos que hay ganador
                        system('pause')
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
            elif opc == 4:
                seg = False
                system('pause')
            else:
                print('ERROR: Opción Inválida')
                system('pause')
    elif opcion == 4:
        system('cls')
        continuar = False
    else:
        print('ERROR: Opción Inválida')
        system('pause')


        
