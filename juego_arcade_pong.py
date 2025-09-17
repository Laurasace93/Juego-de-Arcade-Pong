
#Importamos librerias necesarias
import turtle
import threading
import time

#Configuramos la ventana del juego
ventana = turtle.Screen()
ventana.title("Pong")
ventana.bgcolor("black")
ventana.setup(width=800, height=600)
ventana.tracer(0)   #Desactiva la actualización automática de la ventana

#Marcador
marcador_izquierda = 0
marcador_derecha = 0

#Paleta izquierda
paleta_izquierda = turtle.Turtle()
paleta_izquierda.speed(0)
paleta_izquierda.shape("square")
paleta_izquierda.color("white")
paleta_izquierda.shapesize(stretch_wid=5, stretch_len=1)
paleta_izquierda.penup()
paleta_izquierda.goto(-350, 0)

#Paleta derecha
paleta_derecha = turtle.Turtle()
paleta_derecha.speed(0)
paleta_derecha.shape("square")
paleta_derecha.color("white")
paleta_derecha.shapesize(stretch_wid=5, stretch_len=1)
paleta_derecha.penup()
paleta_derecha.goto(350, 0)

#Linea central
linea_central = turtle.Turtle()
linea_central.speed(0)
linea_central.shape("square")
linea_central.color("gray")
linea_central.shapesize(stretch_wid=30, stretch_len=0.1)
linea_central.penup()
linea_central.goto(0, 0)

#Pelota
pelota = turtle.Turtle()        
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.5
pelota.dy = 0.5
static = True

#Marcador en pantalla
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.penup()
marcador.hideturtle()
marcador.goto(-2.5, 220)
marcador.write("Izquierda: 0  Derecha: 0", align="center", font=("Fixedsys", 24, "normal"))

#Funcion para actualizar el marcador
def actualizar_marcador():
    marcador.clear()
    marcador.write("Izquierda: {}  Derecha: {}".format(marcador_izquierda, marcador_derecha), align="center", font=("Fixedsys", 24, "normal"))

#Funciones para mover las paletas

#mover pala izquierda hacia arriba y abajo
def paleta_izquierda_arriba():
    y = paleta_izquierda.ycor()
    if y < 250:
        y += 20
    paleta_izquierda.sety(y)

def paleta_izquierda_abajo():
    y = paleta_izquierda.ycor()
    if y > -240:
        y -= 20
    paleta_izquierda.sety(y)

#mover pala derecha hacia arriba y abajo
def paleta_derecha_arriba():
    y = paleta_derecha.ycor()
    if y < 250:
        y += 20
    paleta_derecha.sety(y)

def paleta_derecha_abajo():
    y = paleta_derecha.ycor()
    if y > -240:
        y -= 20
    paleta_derecha.sety(y)


#Inicializamos el juego
def iniciar_juego():
    global static
    static = False
    paleta_derecha.clear()

def reiniciar_juego():
    global marcador_izquierda, marcador_derecha, static
    static = True
    marcador_izquierda = 0
    marcador_derecha = 0
    actualizar_marcador()
    pelota.goto(0, 0)
    pelota.dx = 0.5
    pelota.dy = 0.5
    paleta_izquierda.goto(-350, 0)
    paleta_derecha.goto(350, 0)
    paleta_derecha.write("Presiona 'Enter' para iniciar", align="center", font=("Fixedsys", 24, "normal"))

#Teclado
ventana.listen()
ventana.onkeypress(paleta_izquierda_arriba, "w")
ventana.onkeypress(paleta_izquierda_abajo, "s")
ventana.onkeypress(paleta_derecha_arriba, "Up")
ventana.onkeypress(paleta_derecha_abajo, "Down")
ventana.onkeypress(iniciar_juego, "Return")
ventana.onkeypress(reiniciar_juego, "Escape")

#Hilo para mover la pelota
while True:
    try:
        ventana.update()
        if not static:
            #Mover la pelota
            pelota.setx(pelota.xcor() + pelota.dx)
            pelota.sety(pelota.ycor() + pelota.dy)

            #Colisiones con los bordes
            if pelota.ycor() > 290:
                pelota.sety(290)
                pelota.dy *= -1

            if pelota.ycor() < -290:
                pelota.sety(-290)
                pelota.dy *= -1

            if pelota.xcor() > 390:
                pelota.goto(0, 0)
                pelota.dx *= -1
                marcador_izquierda += 1
                actualizar_marcador()

            if pelota.xcor() < -390:
                pelota.goto(0, 0)
                pelota.dx *= -1
                marcador_derecha += 1
                actualizar_marcador()

            #Colisiones con las paletas
            if (pelota.xcor() > 340 and pelota.xcor() < 350) and (pelota.ycor() < paleta_derecha.ycor() + 50 and pelota.ycor() > paleta_derecha.ycor() - 50):
                pelota.setx(340)
                pelota.dx *= -1

            if (pelota.xcor() < -340 and pelota.xcor() > -350) and (pelota.ycor() < paleta_izquierda.ycor() + 50 and pelota.ycor() > paleta_izquierda.ycor() - 50):
                pelota.setx(-340)
                pelota.dx *= -1

        time.sleep(0.01)
    except turtle.Terminator:
        break