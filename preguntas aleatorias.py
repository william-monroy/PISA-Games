import random
from os import system


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
            correcto=False
    