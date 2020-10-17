import random
'''
for i in range(800):
    for j in range(150):
        r=random.randint(0,1)
        print(r,end='')
    print()
'''
import time
import sys

def mecanografiar(texto):

 lista = texto.split()

 for palabra in lista:
    sys.stdout.write(palabra + " ")
    sys.stdout.flush()
    time.sleep(1)

print("\n")
mecanografiar("Hola mundo Python Rules!")
print("\n")