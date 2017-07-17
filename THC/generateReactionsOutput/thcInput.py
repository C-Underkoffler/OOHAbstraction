# Data sources for kinetics
database(
    thermoLibraries = ['BurkeH2O2','primaryThermoLibrary','DFT_QCI_thermo','CBS_QB3_1dHR'],
    reactionLibraries = [],
    seedMechanisms = [],
    kineticsDepositories = 'default',
    #this section lists possible reaction families to find reactions with
    kineticsFamilies = ['H_Abstraction']
    #kineticsEstimator = 'rate rules'
)

# List all species you want reactions between
species( # 1
        label='OOH',
        reactive=True,
        structure=SMILES("[O]O"),
)

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

# THC lol

species( # 2
        label='THC', # iso-otane
        reactive=True,
        structure=SMILES("CCCCCc1cc(c2c(c1)OC([C@H]3[C@H]2C=C(CC3)C)(C)C)O"),
)

# you must list reactor conditions (though this may not effect the output)
simpleReactor(
    temperature=(650,'K'),
    pressure=(10.0,'bar'),
    initialMoleFractions={
        'THC': 1,
    },
    terminationConversion={
        'THC': .99,
    },
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
