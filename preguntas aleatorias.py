import random

pregunta = ['1. Teclea la respuesta de 3/6 + 2/3: ']
respuesta = ['7/6']
correccion = ['Buscar el común denominador-> 6, dividir 6 por el primer denominador y multiplicar el resultado por el numerador-> 6/6=1>> 1*3=3, se hace lo mismo con la otra fracción\nDespués, se suman los resultados -> 3+4=7, por lo que la respuesta daría 7/6']

aleatorio = random.randint(0, len(pregunta)-1)

print(pregunta[aleatorio])
res = input('\nRESPUESTA: ')
if res == respuesta[aleatorio]:
    print('Muy bien')
else:
    print(correccion[aleatorio])


    