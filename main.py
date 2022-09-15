#Bienvenidos  a la trivia:
#libreria random
import random
nombre = input("Escribe tu nombre: ")
edad = int(input("\nDigita tu edad: "))
#Implementación de Puntos de 0,20
puntos = random.randint(0, 20)

print("\n"Hola", nombre, "de",edad, "años" "Bienvenido a mi trivia sobre Historia Universal")
print("\nAquí veremos cuanto sabes sobre  historia Universal")
print( nombre, "Actualmente tienes: " , puntos, "puntos:")
print("\nResponda las siguientes preguntas escribiendo la letra de la respuesta correcta seguidamente precione enter para procesar tu respuesta:\n")
#Inicio de las preguntas:
print("Pregunta 1. ¿Quien fundo Roma?")
print("a) Octavio")
print("b) Servio Tulio")
print("c) Julio Cesar")
print("d) Romulo")
respuesta_1 = input("\nTu respuesta es: ")
while respuesta_1 not in ("a","b","c","d"):
  respuesta_1 = input("Caracter desconocido Ingresa respuesta valida: a, b, c, d: ")
if respuesta_1 == "a":
  print("Incorrecto", nombre, "Octavio nacio tiempo despues de la fundación de Roma")
  puntos = puntos/2
elif respuesta_1 == "b":
  print("Incorrecto", nombre, "Servio Tulio fue el sexto rey de Roma" )
  puntos = puntos +5
elif respuesta_1 == "c":
  print("Incorrecto", "Julio cesar fue un emperador de Roma")
  puntos = puntos -5
else:
  print("¡Bien Hecho!" ,nombre ,"Respuesta correcta")
  puntos = puntos *2
#Pregunta 2
print("Pregunta 2. ¿En que Peninsula se desarrollo lacultura Griega?")
print("a) Peninsula de los Balcanes  ")
print("b) Peninsula Italica")
print("c) Peninsula Ibérica")
print("d) Peninsula escandinava")
respuesta_2 = input("\nTu respuesta es:")
while respuesta_2 not in ("a","b","c","d"):
  respuesta_2 = input("Caracter desconocido Ingresa respuesta valida: a, b, c, d: ")
if respuesta_2 == "a":
  print("Respuesta Correcta")
  puntos = puntos *2
elif respuesta_2 == "b":
  print("Incorrecto" ,nombre,  "en la Peninsula Italica se desarrollo Roma ")
  puntos = puntos +5
elif respuesta_2 == "c":
  print("Incorrecto", nombre ,"En La Peninsula Ibérica se desarrollaron pueblos como son los Ibéricos y Celtas ")
  puntos = puntos -5
else:
  print("Respuesta Incorrecta", nombre, "En la Peninsula escandinava se encontraban los Vikingos")
  puntos = puntos /2
  #Pregunta 3:
print("Pregunta 3. ¿En que pais actual se originó la cultura Persa?")
print("a) Irak")
print("b) Arabia Saudita")
print("c) Iran")
print("d) Pakistán")
respuesta_3 = input("\nTu respuesta es:")
#Implementacion ciclo while en caso de caracter desconocido
while respuesta_3 not in ("a","b","c","d"):
  respuesta_3 = input("Caracter desconocido Ingresa respuesta valida: a, b, c, d: ")
if respuesta_3 == "c":
  print("Respuesta Correcta", nombre)
  puntos = puntos *2
elif respuesta_3 == "a":
  print("Respuesta Incorrecta", nombre, "En Irak se desarrollo Mesopotamia")
  puntos = puntos +5
elif respuesta_3 == "b":
  print("Respuesta Incorrecta" ,nombre , "Mayormente en Arabia Saudita se encontraba un paso importante para los persas, mespopotamios, etc.")
  puntos = puntos -5
else:
  print("Respuesta Incorrecta" ,nombre, "En Pakistán se desarrollo la  Cultura del Valle del Indo")
  puntos = puntos /2
  #Pregunta 4
print("Pregunta 4. ¿Donde se Inició 'La Primera Revolución Industrial'?")
print("a) Francia")
print("b) Rusia")
print("c) China")
print("d) Inglaterra")
respuesta_4 = input("\nTu respuesta es:")
while respuesta_4 not in ("a","b","c","d"):
  respuesta_4 = input("Caracter desconocido Ingresa respuesta valida: a, b, c, d: ")
if respuesta_4 == "d":
  print(nombre, "Respuesta Correcta")
  puntos = puntos *2
elif respuesta_4 == "a":
  print("Incorrecto" , nombre, "En Francia se desarrollo la 'Revolución Francesa' en 1789")
  puntos = puntos +5
elif respuesta_4 == "b":
  print("Incorrecto", nombre, "En Rusia se desarrollo la 'Revolución Rusa' en 1917")
  puntos = puntos /2

else:
  print("Respuesta Incorrecta" , nombre, "En china se desarrollo la Revolución Comunista China en 1949")
  puntos = puntos -5
print("\nGracias", nombre, "Por jugar mi trivia, alcanzaste", puntos, "puntos")