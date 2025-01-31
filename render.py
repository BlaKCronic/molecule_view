from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import glutSolidSphere, glutBitmapCharacter, GLUT_BITMAP_HELVETICA_18
import numpy as np

def draw_sphere(position, radius, color):
    glColor3f(*color)
    glPushMatrix()
    glTranslatef(*position)
    glutSolidSphere(radius, 20, 20)
    glPopMatrix()

def draw_cylinder(start, end, radius, color):
    glColor3f(*color)
    glPushMatrix()
    glTranslatef(*start)
    direction = np.array(end) - np.array(start)
    length = np.linalg.norm(direction)
    if length > 0:
        direction /= length
        rot_axis = np.cross([0, 0, 1], direction)
        rot_angle = np.arccos(np.dot([0, 0, 1], direction)) * 180 / np.pi
        glRotatef(rot_angle, *rot_axis)
    gluCylinder(gluNewQuadric(), radius, radius, length, 20, 20)
    glPopMatrix()

def render_molecule(molecule):
    # Colores para los átomos
    colors = {'O': (1.0, 0.0, 0.0), 'H': (0.0, 0.0, 1.0), 'C': (0.5, 0.5, 0.5), 'N': (0.0, 1.0, 0.0)}

    # Dibujar átomos
    for atom in molecule.atoms:
        element = atom['element']
        position = atom['position']
        radius = 0.3 if element in ['O', 'N'] else 0.2
        draw_sphere(position, radius, colors.get(element, (1.0, 1.0, 1.0)))

    # Dibujar enlaces
    for bond in molecule.bonds:
        start = molecule.atoms[bond[0]]['position']
        end = molecule.atoms[bond[1]]['position']
        draw_cylinder(start, end, 0.05, (0.5, 0.5, 0.5))

def draw_text(x, y, text):
    glColor3f(1.0, 1.0, 1.0)  # Color blanco
    glWindowPos2f(x, y)  # Establecer la posición del texto
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(character))  # Renderizar cada carácter