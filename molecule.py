class Molecule:
    def __init__(self, name):
        self.name = name
        self.atoms = []
        self.bonds = []

    def add_atom(self, element, position):
        self.atoms.append({'element': element, 'position': position})

    def add_bond(self, atom1_idx, atom2_idx):
        self.bonds.append((atom1_idx, atom2_idx))