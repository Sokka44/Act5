from random import *
from turtle import *
from freegames import path

car = path('car.gif')

# Semodifica los caracteres del arreglo, tiene que ser 32
tiles = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z', 'W',
         '@', '#', '$', '%', '&', '*'] * 2
state = {'mark': None}
hide = [True] * 64

# Definimos el contador
touch_count = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    # Actualizar la función tap() para incrementar el contador y mostrar el resultado
    global touch_count
    touch_count += 1

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

    # Modifcar el contador cada vez
    counter_turtle.clear()
    counter_turtle.write("Contador: {}".format(touch_count),
                         align='left', font=('Arial', 12, 'normal'))


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        5
        x, y = xy(mark)
        up()
        goto(x+25, y+4)  # Ajuste de posición para centrar el número
        color('black')
        write(tiles[mark], align='center', font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


# Crear el contador en la pantalla
counter_turtle = Turtle()
counter_turtle.hideturtle()
counter_turtle.up()
# Ajustar la posición del contador en la pantalla
counter_turtle.goto(-190, 200)
counter_turtle.write("Contador: 0", align='left', font=('Arial', 12, 'normal'))

shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
