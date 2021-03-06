Release History
===============

Releases follow the ``major.minor.micro`` scheme recommended by `PEP440 <https://www.python.org/dev/peps/pep-0440/#final-releases>`_, where

* ``major`` increments denote a change that may break API compatibility with previous ``major`` releases
* ``minor`` increments add features but do not break API compatibility
* ``micro`` increments represent bugfix releases or improvements in documentation


0.3.0 - Rotamers, OPLS2005, SMILES and stability improvements
-------------------------------------------------------------

This is a minor release that includes a refactoring of the classes and methods that involve the rotamer library builder. Besides, now it is possible to combine parameters from OPLS2005 and OFF. This release also contains a new method to define a molecule through a SMILES tag. It is still a preliminary version of the Open Force Field to PELE package which is under development.

New features
""""""""""""
- `PR #28 <https://github.com/martimunicoy/offpele/pull/28>`_: Adds a new method to define a `Molecule` object through a SMILES tag. This molecule can be written as a PDB file later for PELE.
- `PR #31 <https://github.com/martimunicoy/offpele/pull/31>`_: Adds the possibility to combine nonbonding and solvent parameters from OPLS2005 with bonding parameters from OFF.
- `PR #36 <https://github.com/martimunicoy/offpele/pull/36>`_: Minor changes to improve the quality of the code.
- `PR #38 <https://github.com/martimunicoy/offpele/pull/38>`_: Adds a new partial charge calculator that uses OPLS2005 to assign partial charges. Includes new flags in the CLI from main.py to combine bonding and nonbonding parameters and partial charges from OPLS2005.
- `PR #42 <https://github.com/martimunicoy/offpele/pull/42>`_: Improves the documentation, adding a section specific for CLI-usage and API examples.
- `PR #46 <https://github.com/martimunicoy/offpele/pull/46>`_: Adds a tag to Molecule class. Besides, the handling of Molecule names is improved. Both attributes can be set when initiating the molecule.

Bugfixes
""""""""
- `PR #22 <https://github.com/martimunicoy/offpele/pull/22>`_: Fixes many bugs. For example, the default output name of the solvent parameters template is changed to `ligandParams.txt`, which is the name that PELE expects.
- `PR #32 <https://github.com/martimunicoy/offpele/pull/32>`_: Minor fixes in ToolkitWrapper classes.
- `PR #34 <https://github.com/martimunicoy/offpele/pull/34>`_: Improves the translation of dihedrals coming from the Open Force Fielf Toolkit and corrects the lack of exclusions in PELE 1-4 list that result from Impact's dihedral definitions.
- `PR #46 <https://github.com/martimunicoy/offpele/pull/46>`_: Prevents molecule to be untagged when loading it from a SMILES tag.

Tests added
"""""""""""
- `PR #31 <https://github.com/martimunicoy/offpele/pull/31>`_: Adds tests to validate some functions of the new SchrodingerToolkitWrapper.
- `PR #34 <https://github.com/martimunicoy/offpele/pull/34>`_: Adds tests to further validate the assignment of parameters from the Open Force Field Toolkit.
- `PR #38 <https://github.com/martimunicoy/offpele/pull/38>`_: Adds tests to validate the new OPLS charge calculator.
- `PR #46 <https://github.com/martimunicoy/offpele/pull/46>`_: Adds tests to validate the name and tag assignment to Molecule class.


0.2.1
-----

This is a micro release that includes new features and parameters to configurate the behaviour of the program.
It is designed to be employed to run the first benchmarks of the implementation in PELE. 
It also includes many stability improvements and an extended test coverage.

New features
""""""""""""
- `PR #15 <https://github.com/martimunicoy/offpele/pull/15>`_: Adds a new method (Antechamber's gasteiger) to calculate partial charges.
- `PR #19 <https://github.com/martimunicoy/offpele/pull/19>`_: Adds a new option to ignore terminal rotatable bonds of each rotamer's branch.
- `PR #17 <https://github.com/martimunicoy/offpele/pull/17>`_: Adds and updates the documentation. However, it is still not completed.

Bugfixes
""""""""
- `PR #18 <https://github.com/martimunicoy/offpele/pull/18>`_: Fixes some problems with proper and improper constructors.

Tests added
"""""""""""
- `PR #15 <https://github.com/martimunicoy/offpele/pull/15>`_: Adds tests ensuring that the run_offpele call from main and the partial charge calculators work as expected.
- `PR #19 <https://github.com/martimunicoy/offpele/pull/19>`_: Adds tests to validate the construction of the `RotamerLibrary` class and the filtering of terminal rotatable bonds.


0.2.0
-----

This is a preliminary version of the Open Force Field to PELE package.

New features
""""""""""""

A first implementation of the package that allows to:

- Build a rotamer library for a small molecule using RDKit's API
- Build a template with the Molecular Mechanics' parameters for a small molecule using the Open Force Field Toolkit
- Assign the OBC implicit solvent parameters to a small molecule using the Open Force Field Toolkit
