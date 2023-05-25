import turtle
import math
import random

# Configuración inicial de la ventana
window = turtle.Screen()
window.title("Sistema Solar")
window.bgcolor("black")

# Creación del sol
sol = turtle.Turtle()
sol.shape("circle")
sol.color("yellow")
sol.penup()
sol.goto(0, 0)
sol.pendown()

# Lista de planetas
planetas = []

# Colores disponibles para los planetas
colores = ["blue", "green"]

# Función para crear un planeta con color y sentido de giro aleatorios
def crearPlanetas(distancia):
    planet = turtle.Turtle()
    planet.shape("circle")
    color = random.choice(colores)
    colores.remove(color)  # Remover el color seleccionado para evitar repeticiones
    planet.color(color)
    planet.penup()
    planet.goto(distancia, 0)
    planet.pendown()
    planet.radius = random.randint(50, 150)
    planet.angle = 0
    planet.speed = random.randint(1, 5) / 100  # Velocidad de giro
    planet.clockwise = random.choice([True, False])  # Sentido de giro aleatorio
    planetas.append(planet)

# Creación de planetas
distance = 100  # Distancia entre los planetas
for _ in range(2):
    crearPlanetas(distance)
    distance += 100

# Bucle principal
while True:
    for planeta in planetas:
        # Movimiento circular
        x = planeta.radius * math.cos(planeta.angle)
        y = planeta.radius * math.sin(planeta.angle)
        planeta.goto(x, y)

        # Actualización del ángulo según la dirección y velocidad de giro
        if planeta.clockwise:
            planeta.angle -= planeta.speed
        else:
            planeta.angle += planeta.speed

# Finalización del programa
turtle.done()


