from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from molecule import Molecule
from render import render_molecule, draw_text

# Configuración de la ventana
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Variables globales para la rotación, zoom y molécula actual
rot_x, rot_y = 0, 0
zoom = -5
current_molecule = None
molecules = []  # Lista de moléculas

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Fondo negro
    glEnable(GL_DEPTH_TEST)  # Habilitar prueba de profundidad

def display():
    global rot_x, rot_y, zoom, current_molecule
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, zoom)
    glRotatef(rot_x, 1, 0, 0)
    glRotatef(rot_y, 0, 1, 0)

    # Renderizar la molécula actual
    if current_molecule:
        render_molecule(current_molecule)
        draw_text(-1.5, 2.0, f"Molecula: {current_molecule.name}")

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

def create_menu():
    def menu_callback(option):
        global current_molecule
        current_molecule = molecules[option]  # Usar el índice directamente
        glutPostRedisplay()

    # Crear un menú para seleccionar moléculas
    menu = glutCreateMenu(menu_callback)
    for idx, molecule in enumerate(molecules):
        glutAddMenuEntry(molecule.name, idx)  # Usar el nombre de la molécula en el menú
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def create_molecules():
    # Molécula de agua (H₂O)
    water = Molecule("Agua (H₂O)")
    water.add_atom('O', [0.0, 0.0, 0.0])
    water.add_atom('H', [0.0, 0.75, -0.5])
    water.add_atom('H', [0.0, -0.75, -0.5])
    water.add_bond(0, 1)  # O-H
    water.add_bond(0, 2)  # O-H
    molecules.append(water)

    # Molécula de metano (CH₄)
    methane = Molecule("Metano (CH₄)")
    methane.add_atom('C', [0.0, 0.0, 0.0])
    methane.add_atom('H', [0.63, 0.63, 0.63])
    methane.add_atom('H', [-0.63, -0.63, 0.63])
    methane.add_atom('H', [-0.63, 0.63, -0.63])
    methane.add_atom('H', [0.63, -0.63, -0.63])
    methane.add_bond(0, 1)  # C-H
    methane.add_bond(0, 2)  # C-H
    methane.add_bond(0, 3)  # C-H
    methane.add_bond(0, 4)  # C-H
    molecules.append(methane)

    # Molécula de dióxido de carbono (CO₂)
    co2 = Molecule("Dióxido de Carbono (CO₂)")
    co2.add_atom('C', [0.0, 0.0, 0.0])
    co2.add_atom('O', [0.0, 0.0, 1.16])
    co2.add_atom('O', [0.0, 0.0, -1.16])
    co2.add_bond(0, 1)  # C-O
    co2.add_bond(0, 2)  # C-O
    molecules.append(co2)

    # Molécula de amoníaco (NH₃)
    ammonia = Molecule("Amoníaco (NH₃)")
    ammonia.add_atom('N', [0.0, 0.0, 0.0])
    ammonia.add_atom('H', [0.0, 0.93, -0.38])
    ammonia.add_atom('H', [-0.81, -0.46, -0.38])
    ammonia.add_atom('H', [0.81, -0.46, -0.38])
    ammonia.add_bond(0, 1)  # N-H
    ammonia.add_bond(0, 2)  # N-H
    ammonia.add_bond(0, 3)  # N-H
    molecules.append(ammonia)

# Inicializar GLUT
glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
glutCreateWindow(b"Visualizacion 3D de Moleculas")
init()

# Crear moléculas y menú
create_molecules()
create_menu()

# Configurar callbacks
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)

# Iniciar el bucle principal
glutMainLoop()