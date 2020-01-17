import turtle

#Define the functino squal
#Crate n squares increasing the angle

def draw_square(form):
    i = 1
    while i < 5:
            form.forward(100)
            form.right(90)
            i = i +1


def draw_art():
    window = turtle.Screen()
    window.bgcolor("navy")

    angie = turtle.Turtle()
    angie.shape("turtle")
    angie.color("white")
    angie.speed(1000)

    for i in range(380):
        draw_square(angie)
        angie.right(13)




draw_art()


