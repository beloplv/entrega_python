lista = []
letras_primas = []
palabra = input('ingrese una palabra: ').lower()
#limpiar caracteres especiales 
palabra = palabra.replace(' ', ' ')#sacamos los espacios
letras_sin_repetir = set(palabra)

for l in letras_sin_repetir:
     lista.append([l,palabra.count(l)])
print(lista)

def es_primo (num):
     if num <= 1:
          return False
     else:
          for i in range(2,num):
               if num % i == 0 and 1 != num:
                    return False
          return True          
aux=0
for i in lista:
     ok= es_primo(lista[aux][1])
     if ok:
          letras_primas.append(lista[aux][0])
     print ('la letra ',lista[aux][0],' aparecio ', lista[aux][1], 'veces')
     aux+=1
for y in letras_primas:
     dato =' - '.join(letras_primas)   
print ('las letras ',dato,' aparareciones un numero primo de veces')