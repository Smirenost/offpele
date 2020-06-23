import pytest

from simtk import unit
import numpy as np

from offPELE.utils import get_data_file_path
from .utils import (SET_OF_LIGAND_PATHS, apply_PELE_dihedral_equation,
                    apply_OFF_dihedral_equation)
from offPELE.topology import Molecule


class TestDihedrals(object):
    def test_OFF_to_PELE_conversion(self):
        MAX_THRESHOLD = 1e-10
        FORCEFIELD_NAME = 'openff_unconstrained-1.1.1.offxml'

        for ligand_path in SET_OF_LIGAND_PATHS:
            ligand_path = get_data_file_path(ligand_path)
            molecule = Molecule(ligand_path)
            molecule.parameterize(FORCEFIELD_NAME)

            x = unit.Quantity(np.arange(0, np.pi, 0.1), unit=unit.radians)

            for PELE_proper, OFF_proper in zip(molecule.propers,
                                               molecule._OFF_propers):
                PELE_y = apply_PELE_dihedral_equation(PELE_proper, x)
                OFF_y = apply_OFF_dihedral_equation(OFF_proper, x)

                y_diff = PELE_y - OFF_y

                assert np.linalg.norm(y_diff) < MAX_THRESHOLD
