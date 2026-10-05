import pgzrun, random

WIDTH = 300
HEIGHT = 300
TITLE = "Basic Game"


def draw():
    screen.fill("black")
    
    # rectangles width and height
    width = WIDTH
    height = HEIGHT - 200
    r = random.randint(1, 255)
    g = 0
    b = 255

    for i in range(20):
        myRect = Rect((0,0),(width, height))
        myRect.center = 150, 150
        screen.draw.rect(myRect,(r,g,b))
        width = width - 10
        height = height + 10
        g = g + 10
        b = b - 10

    screen.draw.circle((200, 200), 50, (255, 0, 0))
    screen.draw.line((50, 50), (350, 300), (0, 250, 50))







pgzrun.go()