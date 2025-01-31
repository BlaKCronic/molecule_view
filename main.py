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

    # Molécula de etanol (C₂H₅OH)
    ethanol = Molecule("Etanol (C₂H₅OH)")
    ethanol.add_atom('C', [0.0, 0.0, 0.0])
    ethanol.add_atom('C', [1.54, 0.0, 0.0])
    ethanol.add_atom('O', [2.31, 0.89, 0.0])
    ethanol.add_atom('H', [-0.51, 0.89, 0.0])
    ethanol.add_atom('H', [-0.51, -0.89, 0.0])
    ethanol.add_atom('H', [0.51, 0.0, 0.89])
    ethanol.add_atom('H', [1.54, -0.89, -0.89])
    ethanol.add_atom('H', [1.54, 0.89, -0.89])
    ethanol.add_atom('H', [2.31, 0.89, 1.0])
    ethanol.add_bond(0, 1)  # C-C
    ethanol.add_bond(1, 2)  # C-O
    ethanol.add_bond(0, 3)  # C-H
    ethanol.add_bond(0, 4)  # C-H
    ethanol.add_bond(0, 5)  # C-H
    ethanol.add_bond(1, 6)  # C-H
    ethanol.add_bond(1, 7)  # C-H
    ethanol.add_bond(2, 8)  # O-H
    molecules.append(ethanol)

    # Molécula de ácido acético (CH₃COOH)
    acetic_acid = Molecule("Ácido Acético (CH₃COOH)")
    acetic_acid.add_atom('C', [0.0, 0.0, 0.0])
    acetic_acid.add_atom('C', [1.54, 0.0, 0.0])
    acetic_acid.add_atom('O', [2.31, 0.89, 0.0])
    acetic_acid.add_atom('O', [2.31, -0.89, 0.0])
    acetic_acid.add_atom('H', [-0.51, 0.89, 0.0])
    acetic_acid.add_atom('H', [-0.51, -0.89, 0.0])
    acetic_acid.add_atom('H', [0.51, 0.0, 0.89])
    acetic_acid.add_atom('H', [1.54, 0.0, 1.0])
    acetic_acid.add_bond(0, 1)  # C-C
    acetic_acid.add_bond(1, 2)  # C-O
    acetic_acid.add_bond(1, 3)  # C-O
    acetic_acid.add_bond(0, 4)  # C-H
    acetic_acid.add_bond(0, 5)  # C-H
    acetic_acid.add_bond(0, 6)  # C-H
    acetic_acid.add_bond(3, 7)  # O-H
    molecules.append(acetic_acid)

    # Molécula de benceno (C₆H₆)
    benzene = Molecule("Benceno (C₆H₆)")
    benzene.add_atom('C', [0.0, 0.0, 0.0])
    benzene.add_atom('C', [1.39, 0.0, 0.0])
    benzene.add_atom('C', [2.08, 1.2, 0.0])
    benzene.add_atom('C', [1.39, 2.4, 0.0])
    benzene.add_atom('C', [0.0, 2.4, 0.0])
    benzene.add_atom('C', [-0.69, 1.2, 0.0])
    benzene.add_atom('H', [-0.69, -1.2, 0.0])
    benzene.add_atom('H', [2.08, -1.2, 0.0])
    benzene.add_atom('H', [3.17, 1.2, 0.0])
    benzene.add_atom('H', [1.39, 3.6, 0.0])
    benzene.add_atom('H', [0.0, 3.6, 0.0])
    benzene.add_atom('H', [-1.78, 1.2, 0.0])
    benzene.add_bond(0, 1)  # C-C
    benzene.add_bond(1, 2)  # C-C
    benzene.add_bond(2, 3)  # C-C
    benzene.add_bond(3, 4)  # C-C
    benzene.add_bond(4, 5)  # C-C
    benzene.add_bond(5, 0)  # C-C
    benzene.add_bond(0, 6)  # C-H
    benzene.add_bond(1, 7)  # C-H
    benzene.add_bond(2, 8)  # C-H
    benzene.add_bond(3, 9)  # C-H
    benzene.add_bond(4, 10)  # C-H
    benzene.add_bond(5, 11)  # C-H
    molecules.append(benzene)

    # Molécula de eteno (C₂H₄)
    ethene = Molecule("Eteno (C₂H₄)")
    ethene.add_atom('C', [0.0, 0.0, 0.0])
    ethene.add_atom('C', [1.33, 0.0, 0.0])
    ethene.add_atom('H', [-0.67, 0.93, 0.0])
    ethene.add_atom('H', [-0.67, -0.93, 0.0])
    ethene.add_atom('H', [2.0, 0.93, 0.0])
    ethene.add_atom('H', [2.0, -0.93, 0.0])
    ethene.add_bond(0, 1)  # C=C
    ethene.add_bond(0, 2)  # C-H
    ethene.add_bond(0, 3)  # C-H
    ethene.add_bond(1, 4)  # C-H
    ethene.add_bond(1, 5)  # C-H
    molecules.append(ethene)

    # Molécula de ácido sulfúrico (H₂SO₄)
    sulfuric_acid = Molecule("Ácido Sulfúrico (H₂SO₄)")
    sulfuric_acid.add_atom('S', [0.0, 0.0, 0.0])
    sulfuric_acid.add_atom('O', [1.43, 0.0, 0.0])
    sulfuric_acid.add_atom('O', [-1.43, 0.0, 0.0])
    sulfuric_acid.add_atom('O', [0.0, 1.43, 0.0])
    sulfuric_acid.add_atom('O', [0.0, -1.43, 0.0])
    sulfuric_acid.add_atom('H', [0.0, 1.43, 1.0])
    sulfuric_acid.add_atom('H', [0.0, -1.43, 1.0])
    sulfuric_acid.add_bond(0, 1)  # S-O
    sulfuric_acid.add_bond(0, 2)  # S-O
    sulfuric_acid.add_bond(0, 3)  # S-O
    sulfuric_acid.add_bond(0, 4)  # S-O
    sulfuric_acid.add_bond(3, 5)  # O-H
    sulfuric_acid.add_bond(4, 6)  # O-H
    molecules.append(sulfuric_acid)

    glucose = Molecule("Glucosa (C₆H₁₂O₆)")
    glucose.add_atom('C', [0.0, 0.0, 0.0])
    glucose.add_atom('C', [1.54, 0.0, 0.0])
    glucose.add_atom('C', [2.31, 0.89, 0.0])
    glucose.add_atom('C', [1.54, 1.78, 0.0])
    glucose.add_atom('C', [0.0, 1.78, 0.0])
    glucose.add_atom('C', [-0.77, 0.89, 0.0])
    glucose.add_atom('O', [2.31, -0.89, 0.0])
    glucose.add_atom('O', [0.0, -0.89, 0.0])
    glucose.add_atom('O', [-0.77, 1.78, 0.0])
    glucose.add_atom('O', [1.54, 2.67, 0.0])
    glucose.add_atom('H', [-0.51, 0.89, 0.89])
    glucose.add_atom('H', [-0.51, 0.89, -0.89])
    glucose.add_atom('H', [0.51, 0.0, 0.89])
    glucose.add_atom('H', [0.51, 0.0, -0.89])
    glucose.add_atom('H', [1.54, -0.89, 0.89])
    glucose.add_atom('H', [1.54, -0.89, -0.89])
    glucose.add_atom('H', [2.31, 0.89, 0.89])
    glucose.add_atom('H', [2.31, 0.89, -0.89])
    glucose.add_atom('H', [1.54, 1.78, 0.89])
    glucose.add_atom('H', [1.54, 1.78, -0.89])
    glucose.add_atom('H', [0.0, 1.78, 0.89])
    glucose.add_atom('H', [0.0, 1.78, -0.89])
    glucose.add_atom('H', [-0.77, 0.89, 0.89])
    glucose.add_atom('H', [-0.77, 0.89, -0.89])
    glucose.add_bond(0, 1)  # C-C
    glucose.add_bond(1, 2)  # C-C
    glucose.add_bond(2, 3)  # C-C
    glucose.add_bond(3, 4)  # C-C
    glucose.add_bond(4, 5)  # C-C
    glucose.add_bond(5, 0)  # C-C
    glucose.add_bond(1, 6)  # C-O
    glucose.add_bond(0, 7)  # C-O
    glucose.add_bond(5, 8)  # C-O
    glucose.add_bond(3, 9)  # C-O
    molecules.append(glucose)

    nacl = Molecule("Cloruro de Sodio (NaCl)")
    nacl.add_atom('Na', [0.0, 0.0, 0.0])
    nacl.add_atom('Cl', [2.82, 0.0, 0.0])
    nacl.add_bond(0, 1)  # Na-Cl
    molecules.append(nacl)

    butane = Molecule("Butano (C₄H₁₀)")
    butane.add_atom('C', [0.0, 0.0, 0.0])
    butane.add_atom('C', [1.54, 0.0, 0.0])
    butane.add_atom('C', [3.08, 0.0, 0.0])
    butane.add_atom('C', [4.62, 0.0, 0.0])
    butane.add_atom('H', [-0.51, 0.89, 0.0])
    butane.add_atom('H', [-0.51, -0.89, 0.0])
    butane.add_atom('H', [0.51, 0.0, 0.89])
    butane.add_atom('H', [1.54, 0.89, 0.0])
    butane.add_atom('H', [1.54, -0.89, 0.0])
    butane.add_atom('H', [3.08, 0.89, 0.0])
    butane.add_atom('H', [3.08, -0.89, 0.0])
    butane.add_atom('H', [4.62, 0.89, 0.0])
    butane.add_atom('H', [4.62, -0.89, 0.0])
    butane.add_bond(0, 1)  # C-C
    butane.add_bond(1, 2)  # C-C
    butane.add_bond(2, 3)  # C-C
    butane.add_bond(0, 4)  # C-H
    butane.add_bond(0, 5)  # C-H
    butane.add_bond(0, 6)  # C-H
    butane.add_bond(1, 7)  # C-H
    butane.add_bond(1, 8)  # C-H
    butane.add_bond(2, 9)  # C-H
    butane.add_bond(2, 10)  # C-H
    butane.add_bond(3, 11)  # C-H
    butane.add_bond(3, 12)  # C-H
    molecules.append(butane)

    hcl = Molecule("Ácido Clorhídrico (HCl)")
    hcl.add_atom('H', [0.0, 0.0, 0.0])
    hcl.add_atom('Cl', [1.27, 0.0, 0.0])
    hcl.add_bond(0, 1)  # H-Cl
    molecules.append(hcl)

    ozone = Molecule("Ozono (O₃)")
    ozone.add_atom('O', [0.0, 0.0, 0.0])
    ozone.add_atom('O', [1.28, 0.0, 0.0])
    ozone.add_atom('O', [0.64, 1.11, 0.0])
    ozone.add_bond(0, 1)  # O-O
    ozone.add_bond(1, 2)  # O-O
    molecules.append(ozone)

    phenol = Molecule("Fenol (C₆H₅OH)")
    phenol.add_atom('C', [0.0, 0.0, 0.0])
    phenol.add_atom('C', [1.39, 0.0, 0.0])
    phenol.add_atom('C', [2.08, 1.2, 0.0])
    phenol.add_atom('C', [1.39, 2.4, 0.0])
    phenol.add_atom('C', [0.0, 2.4, 0.0])
    phenol.add_atom('C', [-0.69, 1.2, 0.0])
    phenol.add_atom('O', [0.0, -1.2, 0.0])
    phenol.add_atom('H', [-0.69, -1.2, 0.0])
    phenol.add_atom('H', [2.08, -1.2, 0.0])
    phenol.add_atom('H', [3.17, 1.2, 0.0])
    phenol.add_atom('H', [1.39, 3.6, 0.0])
    phenol.add_atom('H', [0.0, 3.6, 0.0])
    phenol.add_atom('H', [-1.78, 1.2, 0.0])
    phenol.add_bond(0, 1)  # C-C
    phenol.add_bond(1, 2)  # C-C
    phenol.add_bond(2, 3)  # C-C
    phenol.add_bond(3, 4)  # C-C
    phenol.add_bond(4, 5)  # C-C
    phenol.add_bond(5, 0)  # C-C
    phenol.add_bond(0, 6)  # C-O
    phenol.add_bond(6, 7)  # O-H
    phenol.add_bond(1, 8)  # C-H
    phenol.add_bond(2, 9)  # C-H
    phenol.add_bond(3, 10)  # C-H
    phenol.add_bond(4, 11)  # C-H
    phenol.add_bond(5, 12)  # C-H
    molecules.append(phenol)

    formaldehyde = Molecule("Formaldehído (CH₂O)")
    formaldehyde.add_atom('C', [0.0, 0.0, 0.0])
    formaldehyde.add_atom('O', [1.21, 0.0, 0.0])
    formaldehyde.add_atom('H', [-0.51, 0.89, 0.0])
    formaldehyde.add_atom('H', [-0.51, -0.89, 0.0])
    formaldehyde.add_bond(0, 1)  # C=O
    formaldehyde.add_bond(0, 2)  # C-H
    formaldehyde.add_bond(0, 3)  # C-H
    molecules.append(formaldehyde)

    nitric_acid = Molecule("Ácido Nítrico (HNO₃)")
    nitric_acid.add_atom('N', [0.0, 0.0, 0.0])
    nitric_acid.add_atom('O', [1.21, 0.0, 0.0])
    nitric_acid.add_atom('O', [0.0, 1.21, 0.0])
    nitric_acid.add_atom('O', [0.0, -1.21, 0.0])
    nitric_acid.add_atom('H', [0.0, 1.21, 1.0])
    nitric_acid.add_bond(0, 1)  # N=O
    nitric_acid.add_bond(0, 2)  # N-O
    nitric_acid.add_bond(0, 3)  # N-O
    nitric_acid.add_bond(2, 4)  # O-H
    molecules.append(nitric_acid)

    acetone = Molecule("Acetona (C₃H₆O)")
    acetone.add_atom('C', [0.0, 0.0, 0.0])
    acetone.add_atom('C', [1.54, 0.0, 0.0])
    acetone.add_atom('C', [3.08, 0.0, 0.0])
    acetone.add_atom('O', [1.54, 1.21, 0.0])
    acetone.add_atom('H', [-0.51, 0.89, 0.0])
    acetone.add_atom('H', [-0.51, -0.89, 0.0])
    acetone.add_atom('H', [0.51, 0.0, 0.89])
    acetone.add_atom('H', [3.08, 0.89, 0.0])
    acetone.add_atom('H', [3.08, -0.89, 0.0])
    acetone.add_bond(0, 1)  # C-C
    acetone.add_bond(1, 2)  # C-C
    acetone.add_bond(1, 3)  # C=O
    acetone.add_bond(0, 4)  # C-H
    acetone.add_bond(0, 5)  # C-H
    acetone.add_bond(0, 6)  # C-H
    acetone.add_bond(2, 7)  # C-H
    acetone.add_bond(2, 8)  # C-H
    molecules.append(acetone)

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