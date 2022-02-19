#Para mayor informacion sobre la libreria turtle, ir a la documentación
#https://docs.python.org/es/3.9/library/turtle.html#overview-of-available-turtle-and-screen-methods

                             #####CODIGO#####
import turtle
t = turtle.Turtle() #cursor dinámico, por defecto es un triangulo pero si colocamos entre parentesis (shape: "circle"), el cursor se transformara en un circulo.
s = turtle.Screen() #muestra el dibujo en una pantalla aparte
s.bgcolor("white") #establece el color de fondo de la pantalla
t.pencolor("black") #color del lapiz
t.speed(100) #velocidad de la tortuga (cursor). speed= 0o significa que no hará ninguna animacion. 1 es lento y 10 es rapido.
col = ("red", "blue", "cyan", "purple")
for n in range (5):
    for x in range (8):
        t.speed(x+8)
        for i in range(2):
            t.pensize(2) #grosor de la linea
            t.circle(80+n*20,90) #dibuja un circulo  (radio, angulo, steps: pasos a usar. En caso de no colocar, es calculado automaticamente)
            t.lt(90) # angulo de giro del cursor (hacia la izquierda). Por defecto está en grados (°) 
        t.lt(45)
    t.pencolor(col[n%4])
s.exitonclick() #cierra la ventana del grafico con un click

