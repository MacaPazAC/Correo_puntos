"""Ingresa tu correo duoc con @duocuc.cl
Acomulador de puntos nickname @ break
a = 1
e = 2
i = 3
o = 4 
u = 5"""
print("Ingrese su correo duoc:")
correo = input()
contador = 0
for letra in correo: #recorrer el nickname del correo letra por letra
  if letra == "a":
    contador = contador + 1
  elif letra == "e":
    contador = contador + 2
  elif letra == "i":
    contador = contador + 3
  elif letra == "o":
    contador = contador+ 4
  elif letra == "u":
    contador = contador+ 5
  elif letra == "@":
    break
  
print("Sus puntos son "+str(contador))