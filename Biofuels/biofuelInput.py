# Data sources for kinetics
database(
    thermoLibraries = ['BurkeH2O2','primaryThermoLibrary','DFT_QCI_thermo','CBS_QB3_1dHR'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = 'default',
    #this section lists possible reaction families to find reactioons with
    kineticsFamilies = ['H_Abstraction']
    #kineticsEstimator = 'rate rules'
)

# List all species you want reactions between
species( # 1
        label='OOH',
        reactive=True,
        structure=SMILES("[O]O"),
)

"""species(
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
)"""

# The biofuels of interest

species( # 2
        label='2,2,4-Trimethylpentane', # iso-otane
        reactive=True,
        structure=SMILES("CC(C)CC(C)(C)C"),
)

species( # 3
        label='2,4-Dimethylhexane',
        reactive=True,
        structure=InChI("InChI=1S/C8H18/c1-5-8(4)6-7(2)3/h7-8H,5-6H2,1-4H3"),
)

species( # 4
        label='3-Methylheptane',
        reactive=True,
        structure=SMILES("CCCCC(C)CC"),
)

species( # 5
        label='2-methyl 2-butanol',
        reactive=True,
        structure=SMILES("CCC(C)(C)O"),
)

species( # 6
        label='2-Methyl-1-pentanol',
        reactive=True,
        structure=SMILES("OCC(C)CCC"),
)

species( # 7
        label='2,4-dimethyl-2-heptene',
        reactive=True,
        structure=InChI("InChI=1S/C9H18/c1-5-6-9(4)7-8(2)3/h7,9H,5-6H2,1-4H3"),
)

species( # 8
        label='methylcyclopentane',
        reactive=True,
        structure=InChI("InChI=1S/C6H12/c1-6-4-2-3-5-6/h6H,2-5H2,1H3"),
)

species( # 9
        label='Ocimene',
        reactive=True,
        structure=SMILES("C=C\C(=C\CCC(=C)C)C"),
)

species( # 10
        label='Xylene',
        reactive=True,
        structure=SMILES("CC1=CC=C(C)C=C1"),
)

species( # 11
        label='Diisobutyl ketone',
        reactive=True,
        structure=SMILES("CC(C)CC(=O)CC(C)C"),
)

species( # 12
        label='Methyl 1,3-dimethylbutyl ketone',
        reactive=True,
        structure=SMILES("CC(C)CC(C)C(=O)C"),
)

species( # 13
        label='2,3-di-tert-butoxypropanol',
        reactive=True,
        structure=SMILES("CC(C)(C)OCC(CO)OC(C)(C)C"),
)


species( # 14
        label='2-(1-ethylpropoxy)-propane',
        reactive=True,
        structure=SMILES("CCC(CC)OC(C)C"),
)

species( # 15
        label='alpha-pinene',
        reactive=True,
        structure=SMILES("CC1=CCC2CC1C2(C)C"),
)

species( # 16
        label='isoamyl acetate',
        reactive=True,
        structure=SMILES("CC(C)CCOC(C)=O"),
)
species( # 17
        label='ethyl isobutyrate',
        reactive=True,
        structure=SMILES("CCOC(=O)C(C)C"),
)
species( # 18
        label='2-methylcyclopent-2-en-1-one',
        reactive=True,
        structure=SMILES("CC1=CCCC1=O"),
)
species( # 19
        label='2-methyl-5-pentyl tetrahydrofuran',
        reactive=True,
        structure=SMILES("CCCCCC1CCC(C)O1"),
)

species( # 20
        label='2-methylhept-2-ene',
        reactive=True,
        structure=SMILES("CCCCC=C(C)C"),
)

species( # 21
        label='2-methylhept-3-ene',
        reactive=True,
        structure=SMILES("CCCC=CC(C)C"),
)

species( # 22
        label='2-methylhept-4-ene',
        reactive=True,
        structure=SMILES("CCC=CCC(C)C"),
)

species( # 23
        label='2-methylhept-5-ene',
        reactive=True,
        structure=SMILES("CC=CCCC(C)C"),
)

species( # 24
        label='2-methylhept-6-ene',
        reactive=True,
        structure=SMILES("C=CCCCC(C)C"),
)


# you must list reactor conditions (though this may not effect the output)
simpleReactor(
    temperature=(650,'K'),
    pressure=(10.0,'bar'),
    initialMoleFractions={
        '2,2,4-Trimethylpentane': 1,
    },
    terminationConversion={
        '2,2,4-Trimethylpentane': .99,
    },
#    terminationConversion={
#        '2,4-Dimethylhexane': .99,
#    },
    terminationTime=(120,'s'),
)

#optional module if you want to get pressure dependent kinetics.

#pressureDependence(
#     method='modified strong collision',
#     maximumGrainSize=(0.5,'kcal/mol'),
#     minimumNumberOfGrains=250,
#     temperatures=(300,2200,'K',2),
#     pressures=(0.01,100,'bar',3),
#     interpolation=('Chebyshev', 6, 4),
#     maximumAtoms=15,
#)

#optional module if you want to limit species produced in reactions.

#generatedSpeciesConstraints(
#    allowed=['input species','seed mechanisms','reaction libraries'],
#    maximumCarbonAtoms=4,
#    maximumOxygenAtoms=7,
#    maximumNitrogenAtoms=0,
#    maximumSiliconAtoms=0,
#    maximumSulfurAtoms=0,
#    maximumHeavyAtoms=20,
#    maximumRadicalElectrons=1,
#)
