#Ejercicio 2 - Condicionales
import turtle
import time
#Creación de Rosalinda!
rosalinda = turtle.Pen()
rosalinda.shape("turtle")
#Configuración del tamaño de la ventana
screen = turtle.Screen()
screen.setup(400,400)

#Función para dibujar un cuadrado
def draw_square():
    for i in range(4):
        rosalinda.forward(100)
        rosalinda.left(90)
#Función para dibujar un círculo
def draw_circle():
    rosalinda.circle(50)

#Función para escribir un mensaje en pantalla
def say_message(message):
    rosalinda.color("red")
    rosalinda.write(message,font=("Arial", 14, "normal"))

# Código del ejercicio
forma = input("Buenos días! ¿Cuadrado o círculo?")
if forma == "cuadrado":
    draw_square()
elif forma == "circulo":
    draw_circle()
else:
    say_message("Lo siento, \nno le he entendido :(")

#Tiempo de espera para ver el dibujo
time.sleep(2)