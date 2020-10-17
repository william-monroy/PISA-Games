from os import system

h1 = ['  __   ','  __   ','  ___  ','  __   ',' _  _ ','  ___  ','  ___  ','  ___  ','   ___  ','  ___  '] 
h2 = [' /  \\  ',' /  |  ',' (_  | ',' |__`. ','| || |',' | __| ',' / __| ',' |_  | ','  / _ \\ ',' / _ \\  ']
h3 = ['| // | ',' `7 |  ','  / /  ','  |_ | ','`._  _|',' `._`. ','| ,_ \\ ','  / /  ',' ) _ ( ',' \__ / ']
h4 = [' \__/  ','  |_|  ',' |___| ',' |__.\' ','   |_| ',' !__.\' ',' \___/ ',' |_/   ',' \___/ ','  /_/  ']


system('cls')

def numero(numero):
  if len(str(numero))==1:
    n1 = 0
    n2 = 0
    n3 = 0
    n4 = numero
  elif len(str(numero))==2:
    n1 = 0
    n2 = 0
    n3 = int(str(numero)[0])
    n4 = int(str(numero)[1])
  elif len(str(numero))==3:
    n1 = 0
    n2 = int(str(numero)[0])
    n3 = int(str(numero)[1])
    n4 = int(str(numero)[2])

  elif len(str(numero))==4:
    n1 = int(str(numero)[0])
    n2 = int(str(numero)[1])
    n3 = int(str(numero)[2])
    n4 = int(str(numero)[3])
  print("\033[1;101;93m"+'           PUNTUACION            '+"\033[0m")
  print("\033[1;101;93m",h1[n1],h1[n2],h1[n3],h1[n4],"\033[0m")
  print("\033[1;101;93m",h2[n1],h2[n2],h2[n3],h2[n4],"\033[0m")
  print("\033[1;101;93m",h3[n1],h3[n2],h3[n3],h3[n4],"\033[0m")
  print("\033[1;101;93m",h4[n1],h4[n2],h4[n3],h4[n4],"\033[0m")

numero(666)


