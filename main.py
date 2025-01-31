from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from molecule import Molecule
from render import render_molecule

# Configuración de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Variables globales para la rotación y zoom
rot_x, rot_y = 0, 0
zoom = -5

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glEnable(GL_DEPTH_TEST)  # Habilitar prueba de profundidad

def display():
    global rot_x, rot_y, zoom
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, zoom)
    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)

    # Renderizar la molécula
    render_molecule(molecule)

    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (width / height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

def keyboard(key, x, y):
    global rot_x, rot_y, zoom
    if key == b'w':
        rot_x += 5
    elif key == b's':
        rot_x -= 5
    elif key == b'a':
        rot_y += 5
    elif key == b'd':
        rot_y -= 5
    elif key == b'q':
        zoom += 0.5
    elif key == b'e':
        zoom -= 0.5
    glutPostRedisplay()

# Crear una molécula de agua (H₂O)
molecule = Molecule()
molecule.add_atom('O', [0.0, 0.0, 0.0])
molecule.add_atom('H', [0.0, 0.75, -0.5])
molecule.add_atom('H', [0.0, -0.75, -0.5])
molecule.add_bond(0, 1)  # O-H
molecule.add_bond(0, 2)  # O-H

# Inicializar GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow(b"Visualizacion 3D de una Molecula")
init()
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMainLoop()