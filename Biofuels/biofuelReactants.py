from rmgpy import species

species(
        label='OH',
        reactive=True,
        structure=SMILES("[OH]"),
)

species(
        label='H',
        reactive=True,
        structure=SMILES("[H]"),
)

species(
        label='OOH',
        reactive=True,
        structure=SMILES("[O]O"),
)

species(
        label='O',
        reactive=True,
        structure=SMILES("[O]"),
)

species(
        label='CH3',
        reactive=True,
        structure=SMILES("[CH3]"),
)

species(
        label='O2',
        reactive=True,
        structure=SMILES("OO"),
)

# The biofuels of interest

species(
        label='2,4-Dimethylhexane',
        reactive=True,
        structure=InChI("InChI=1S/C8H18/c1-5-8(4)6-7(2)3/h7-8H,5-6H2,1-4H3"),
)

species(
        label='2,2,4-Trimethylpentane',
        reactive=True,
        structure=SMILES("CC(C)CC(C)(C)C"),
)

species(
        label='3-Methylheptane',
        reactive=True,
        structure=SMILES("CCCCC(C)CC),
)
