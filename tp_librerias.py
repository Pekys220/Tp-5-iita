"""Escriba una función redondear() que permita redondear un número
decimal de acuerdo al criterio: Si el número es mayor a 3.50, devolver el
entero siguiente (en este caso, 4), si no devolver el entero inmediatamente
anterior (3). """

# def redondear(numero):
#     entero = int(numero)
#     fraccion = numero - entero
#     if fraccion > 0.50:
#         return entero + 1
#     else:
#         return entero


# print(redondear(3.4))

"""Coloque el módulo del ejercicio anterior dentro de un paquete. En un
módulo que esté fuera de ese paquete, cree una función de suma de
decimales que redondee el resultado haciendo uso de la función
redondear() del paquete recién creado"""

# import redondear_decimales

# def suma(a, b):
#     sumando = a + b
#     return redondear_decimales.redondear(sumando)

# print(suma(0.15, 0.30))

"""Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema."""

# import datetime
# fecha_hora = datetime.datetime.now()
# print(fecha_hora)

"""Escriba un programa que devuelva un número par al azar entre 2 y 10
(pista: para comprobar si se pueden generar todos los números, pruebe
ejecutar el programa dentro de un ciclo infinito)"""

# import random

# def devolver_numeros():
#     numero = random.randint(2, 10)
#     if numero % 2 == 0:
#         return numero
#     else:
#         return numero + 1
    
"""Bola mágica: La bola mágica (Magic 8 ball) es un popular juguete usado
para la adivinación o para buscar consejo. Su mecanismo es muy simple:
ante una pregunta del usuario, la bola responde con una de 8 posibles
respuestas:
- Es seguro que sí
- Las chances son buenas
- Puedes contar con ello
- Pregúntame de nuevo más tarde
- Concéntrate y pregunta de nuevo
- No veo con claridad, intenta de nuevo
- Mi respuesta es no
- Mis fuentes me dicen que no
Escriba una función en Python para simular la bola mágica."""

# import random

# def bola_magica():
#     input("Pregunta:")
#     numero = random.randint(1, 8)
#     if numero == 1:
#         print("Es seguro que sí")
#     elif numero == 2:
#         print("Las chances son buenas")
#     elif numero == 3:
#         print("Puedes contar con ello")
#     elif numero == 4:
#         print("Pregúntame de nuevo más tarde")
#     elif numero == 5:
#         print("Concéntrate y pregunta de nuevo")
#     elif numero == 6:
#         print("No veo con claridad, intenta de nuevo")
#     elif numero == 7:
#         print("Mi respuesta es no")
#     else:
#         print("Mis fuentes me dicen que no")

# bola_magica()

"""7. (Opcional) Sorteo: Escriba un programa que simule un sorteo donde
toman uno o más papeles al azar de un pozo para elegir los ganadores."""
#import random
#def sorteo(numero_de_participantes):
 #   ganador = random.randint(1, numero_de_participantes)
  #  return print(f"El ganador de el sorteo es el numero: '{ganador}' Felicidades")

#sorteo(23)
