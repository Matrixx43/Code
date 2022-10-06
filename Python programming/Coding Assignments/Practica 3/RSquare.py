import turtle

def inicializa_tortuga():
    turtle.setup(width=800,height=800)  # Crea ventana de 800 x 800
    turtle.speed(0)                     # Velocidad maxima
    turtle.pencolor("#101010")          # Color del lapiz
    turtle.fillcolor("#2c95b5")         # Color del fondo
    turtle.width(2)                     # Ancho del trazo

def finaliza_tortuga():
    turtle.hideturtle()         # Ocultar tortuga
    turtle.done()               # Desbloquear la ventana grafica
    try:
        turtle.bye()
    except turtle.Terminator:
        pass    
    
def dibuja_cuadrado(lado, x, y):
    # Posicionar la tortuga.
    # El centro de la pantalla es (0,0), por tanto para que el cuadrado este
    # centrado, la esquina sup. izqda.  debe situarse en (-lado//2, -lado//2)
    # x, y son las coordenadas del CENTRO del cuadrado
    turtle.up()
    pos_turtle_x = x - lado//2
    pos_turtle_y = y - lado//2
    turtle.setpos(pos_turtle_x, pos_turtle_y)
    turtle.down()

    # Dibujar y rellenar cuadrado
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(lado)
        turtle.left(90)
    turtle.end_fill()

def rSquareA(n, x, y, l):
    if n > 1:
        rSquareA(n-1, x - l//2, y - l//2, l//2)
        rSquareA(n-1, x - l//2, y + l//2, l//2)
        rSquareA(n-1, x + l//2, y + l//2, l//2)
        rSquareA(n-1, x + l//2, y - l//2, l//2)
    # Cuando n ya sea 1 o se hayan dibujado los cuadrados anteriores
    dibuja_cuadrado(l, x, y)

def rSquareB(n, x, y, l):
    # Mismo que A pero superpone los cuadrados pequenos
    # Dibuja primero el cuadrado central
    dibuja_cuadrado(l, x, y)
    # Despues, si todavia hacen falta, dibuja los cuadrados mas pequenos
    if n > 1:
        rSquareB(n-1, x - l//2, y - l//2, l//2)
        rSquareB(n-1, x - l//2, y + l//2, l//2)
        rSquareB(n-1, x + l//2, y + l//2, l//2)
        rSquareB(n-1, x + l//2, y - l//2, l//2)

if __name__ == '__main__':
    # Conseguir tipo
    tipo = input("Tipo figura A o B:").lower()
    # Conseguir orden
    n = int(input("Orden de la figura: "))
    inicializa_tortuga()
    if tipo == 'a':
        rSquareA(n, 0, 0, 400)
    elif tipo =='b':
        rSquareB(n, 0, 0, 400)
    finaliza_tortuga()
    