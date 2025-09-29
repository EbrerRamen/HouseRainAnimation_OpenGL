from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

W_Width, W_Height = 1000, 1000

red, green, blue = 1.0, 1.0, 1.0
bg_red, bg_green, bg_blue = 0.0, 0.0, 0.0

rain_intensity = 200
dir = 0

class Raindrop:
    def __init__(self):
        self.x = random.uniform(0, W_Width)
        self.y = random.uniform(W_Height, W_Height + 1000)
        self.y_speed = 12
        self.x_speed = 4

# Generating raindrops
raindrops = []
for i in range(rain_intensity):
    raindrops.append(Raindrop())

def iterate():
    glViewport(0, 0, W_Width, W_Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, W_Width, 0.0, W_Height, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def draw_raindrop(raindrop):
    glBegin(GL_LINES)
    glVertex2f(raindrop.x, raindrop.y)
    glVertex2f(raindrop.x + dir * raindrop.x_speed * 10, raindrop.y - 20)
    glEnd()

def draw_house():

    # Quadrangles

    # Walls

    glLineWidth(4)
    glBegin(GL_LINES)

    glVertex2f(250, 1)
    glVertex2f(750, 1)
    glVertex2f(250, 1)
    glVertex2f(250, 400)
    glVertex2f(750, 1)
    glVertex2f(750, 400)

    glEnd()

    # Window

    glLineWidth(2)
    glBegin(GL_LINES)

    glVertex2f(550, 150)
    glVertex2f(700, 150)
    glVertex2f(550, 150)
    glVertex2f(550, 300)
    glVertex2f(700, 150)
    glVertex2f(700, 300)
    glVertex2f(550, 300)
    glVertex2f(700, 300)

    # Door

    glVertex2f(350, 1)
    glVertex2f(350, 200)
    glVertex2f(450, 1)
    glVertex2f(450, 200)
    glVertex2f(350, 200)
    glVertex2f(450, 200)

    glEnd()

    # Details

    glPointSize(5)
    glBegin(GL_POINTS)

    glVertex2f(435, 100)

    glEnd()

    glLineWidth(1)
    glBegin(GL_LINES)

    glVertex2f(625, 150)
    glVertex2f(625, 300)
    glVertex2f(550, 225)
    glVertex2f(700, 225)

    glEnd()

    # Triangle

    glBegin(GL_TRIANGLES)

    glVertex2d(500, 500)
    glVertex2d(240, 400)
    glVertex2d(760, 400)

    glEnd()

def specialKeyListener(key, x, y):
    global dir
    if key == GLUT_KEY_LEFT and dir>-1:
        dir -= 0.2
    elif key == GLUT_KEY_RIGHT and dir<1:
        dir += 0.2
    glutPostRedisplay()

def keyboardListener(key, x, y):

    global red, green, blue, bg_red, bg_green, bg_blue

    if key==b'n' and (bg_red > 0 and bg_green > 0 and bg_blue > 0):
        red, green, blue = red + 0.2, green + 0.2, blue + 0.2
        bg_red, bg_green, bg_blue = bg_red - 0.2, bg_green - 0.2, bg_blue - 0.2
        print(bg_red, bg_green, bg_blue)
    if key==b'd' and (bg_red < 1 and bg_green < 1 and bg_blue < 1):
        red, green, blue = red - 0.2, green - 0.2, blue - 0.2
        bg_red, bg_green, bg_blue = bg_red + 0.2, bg_green + 0.2, bg_blue + 0.2
    glutPostRedisplay()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(red, green, blue)
    glClearColor(bg_red, bg_green, bg_blue, 1)
    draw_house()
    for raindrop in raindrops:
        draw_raindrop(raindrop)
    glutSwapBuffers()

def animate():
    for raindrop in raindrops:
        raindrop.y -= raindrop.y_speed
        raindrop.x += dir * raindrop.y_speed
        if raindrop.y < 0:
            raindrop.x = random.uniform(0, W_Width)
            raindrop.y = random.uniform(W_Height, W_Height + 1000)
        if raindrop.x < 0:
            raindrop.x = W_Width
            raindrop.y = random.uniform(0, W_Height)
        if raindrop.x > W_Width:
            raindrop.x = 0
            raindrop.y = random.uniform(0, W_Height)
    glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutCreateWindow(b"Heavy Rain")
glutDisplayFunc(showScreen)
glutIdleFunc(animate)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMainLoop()
