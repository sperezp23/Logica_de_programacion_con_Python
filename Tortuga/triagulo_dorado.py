# %% Librerías
import turtle

# Triangulo dorado
t = turtle.Turtle()
t.shape('turtle')
t.color('gold')

lados = 10
largo = 100
angle = -360/lados

for i in range(lados):
    t.forward(largo)
    t.left(angle)

# %% Ensayo
    
# Python program to draw 
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x//100 + 1)
	t.forward(x)
	t.left(59)
