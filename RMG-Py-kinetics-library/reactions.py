#!/usr/bin/env python
# encoding: utf-8

name = "AutoTST-M062X"
shortDesc = u"AutoTST using M062X"
longDesc = u"""
AutoTST calculations using M062X
"""
entry(
    index = 1,
    label = "C5H8(1) + HO2(2) <=> C5H7(3) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.46901e-07, 'cm^3/(mol*s)'),
        n = 5.46227,
        Ea = (16.0409, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.40766, dn = +|- 0.115316, dEa = +|- 0.634353 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8(1) + HO2(2) <=> C5H7(3) + H2O2(4)""",
)

entry(
    index = 2,
    label = "C2H4O2(5) + HO2(2) <=> C2H3O2(6) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000827612, 'cm^3/(mol*s)'),
        n = 4.50294,
        Ea = (56.3444, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.33955, dn = +|- 0.0383657, dEa = +|- 0.21105 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O2(5) + HO2(2) <=> C2H3O2(6) + H2O2(4)""",
)

entry(
    index = 3,
    label = "C4H8O(7) + HO2(2) <=> C4H7O(8) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56079e-07, 'cm^3/(mol*s)'),
        n = 5.22388,
        Ea = (11.9207, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.03086, dn = +|- 0.0929786, dEa = +|- 0.511476 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(7) + HO2(2) <=> C4H7O(8) + H2O2(4)""",
)

entry(
    index = 4,
    label = "C4H8(9) + HO2(2) <=> H2O2(4) + C4H7(10)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.85695e-08, 'cm^3/(mol*s)'),
        n = 5.63825,
        Ea = (24.6184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.61249, dn = +|- 0.126031, dEa = +|- 0.693299 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8(9) + HO2(2) <=> H2O2(4) + C4H7(10)""",
)

entry(
    index = 5,
    label = "C4H8O(11) + HO2(2) <=> C4H7O(12) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.86399e-07, 'cm^3/(mol*s)'),
        n = 5.35115,
        Ea = (20.2957, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.17403, dn = +|- 0.10192, dEa = +|- 0.560659 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(11) + HO2(2) <=> C4H7O(12) + H2O2(4)""",
)

entry(
    index = 6,
    label = "C4H10(13) + HO2(2) <=> H2O2(4) + C4H9(14)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000948686, 'cm^3/(mol*s)'),
        n = 4.38662,
        Ea = (61.9582, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.26505, dn = +|- 0.0308561, dEa = +|- 0.16974 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10(13) + HO2(2) <=> H2O2(4) + C4H9(14)""",
)

entry(
    index = 7,
    label = "C4H8(15) + HO2(2) <=> H2O2(4) + C4H7(16)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000220412, 'cm^3/(mol*s)'),
        n = 4.48417,
        Ea = (61.2327, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.29944, dn = +|- 0.0343761, dEa = +|- 0.189103 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8(15) + HO2(2) <=> H2O2(4) + C4H7(16)""",
)

entry(
    index = 8,
    label = "C4H8O(17) + HO2(2) <=> C4H7O(18) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000583326, 'cm^3/(mol*s)'),
        n = 4.35917,
        Ea = (44.6771, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.23402, dn = +|- 0.0275975, dEa = +|- 0.151814 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(17) + HO2(2) <=> C4H7O(18) + H2O2(4)""",
)

entry(
    index = 9,
    label = "C6H8(19) + HO2(2) <=> C6H7(20) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.56034e-10, 'cm^3/(mol*s)'),
        n = 6.64499,
        Ea = (22.1924, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.61527, dn = +|- 0.126171, dEa = +|- 0.694065 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H8(19) + HO2(2) <=> C6H7(20) + H2O2(4)""",
)

entry(
    index = 10,
    label = "C3H4O(21) + HO2(2) <=> C3H3O(22) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.37519e-05, 'cm^3/(mol*s)'),
        n = 5.0024,
        Ea = (30.7116, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.91102, dn = +|- 0.0849968, dEa = +|- 0.467568 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4O(21) + HO2(2) <=> C3H3O(22) + H2O2(4)""",
)

entry(
    index = 11,
    label = "C4H10(23) + HO2(2) <=> C4H9(24) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00381462, 'cm^3/(mol*s)'),
        n = 4.38434,
        Ea = (39.5154, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.2896, dn = +|- 0.0333792, dEa = +|- 0.183619 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10(23) + HO2(2) <=> C4H9(24) + H2O2(4)""",
)

entry(
    index = 12,
    label = "C3H8(25) + HO2(2) <=> C3H7(26) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000337358, 'cm^3/(mol*s)'),
        n = 4.70263,
        Ea = (46.2109, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.40842, dn = +|- 0.0449463, dEa = +|- 0.24725 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8(25) + HO2(2) <=> C3H7(26) + H2O2(4)""",
)

entry(
    index = 13,
    label = "C3H6O2(27) + HO2(2) <=> C3H5O2(28) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000423229, 'cm^3/(mol*s)'),
        n = 4.33217,
        Ea = (10.9667, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.33794, dn = +|- 0.038208, dEa = +|- 0.210182 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O2(27) + HO2(2) <=> C3H5O2(28) + H2O2(4)""",
)

entry(
    index = 14,
    label = "C2H4O2(29) + HO2(2) <=> C2H3O2(30) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00108079, 'cm^3/(mol*s)'),
        n = 4.22914,
        Ea = (20.9665, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.27527, dn = +|- 0.0319125, dEa = +|- 0.175551 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O2(29) + HO2(2) <=> C2H3O2(30) + H2O2(4)""",
)

entry(
    index = 15,
    label = "C2H4O(31) + HO2(2) <=> C2H3O(32) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000274848, 'cm^3/(mol*s)'),
        n = 4.67067,
        Ea = (21.5744, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.59853, dn = +|- 0.0615635, dEa = +|- 0.338661 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O(31) + HO2(2) <=> C2H3O(32) + H2O2(4)""",
)

entry(
    index = 16,
    label = "C4H10O(33) + HO2(2) <=> C4H9O(34) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000181889, 'cm^3/(mol*s)'),
        n = 4.60161,
        Ea = (54.0961, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.3787, dn = +|- 0.0421467, dEa = +|- 0.231849 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(33) + HO2(2) <=> C4H9O(34) + H2O2(4)""",
)

entry(
    index = 17,
    label = "C4H8O(35) + HO2(2) <=> C4H7O(36) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000281069, 'cm^3/(mol*s)'),
        n = 4.5897,
        Ea = (15.2284, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.50747, dn = +|- 0.0538655, dEa = +|- 0.296314 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(35) + HO2(2) <=> C4H7O(36) + H2O2(4)""",
)

entry(
    index = 18,
    label = "C4H10O(33) + HO2(2) <=> H2O2(4) + C4H9O(37)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00102796, 'cm^3/(mol*s)'),
        n = 4.40852,
        Ea = (62.869, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.25438, dn = +|- 0.0297452, dEa = +|- 0.163628 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(33) + HO2(2) <=> H2O2(4) + C4H9O(37)""",
)

entry(
    index = 19,
    label = "C4H6O(38) + HO2(2) <=> C4H5O(39) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.22601e-05, 'cm^3/(mol*s)'),
        n = 4.98552,
        Ea = (32.7154, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.86223, dn = +|- 0.0816026, dEa = +|- 0.448896 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O(38) + HO2(2) <=> C4H5O(39) + H2O2(4)""",
)

entry(
    index = 20,
    label = "C4H8O(35) + HO2(2) <=> H2O2(4) + C4H7O(40)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000383212, 'cm^3/(mol*s)'),
        n = 4.55507,
        Ea = (60.3052, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.33514, dn = +|- 0.0379336, dEa = +|- 0.208673 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(35) + HO2(2) <=> H2O2(4) + C4H7O(40)""",
)

entry(
    index = 21,
    label = "C4H8(41) + HO2(2) <=> H2O2(4) + C4H7(42)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.05586e-07, 'cm^3/(mol*s)'),
        n = 5.54951,
        Ea = (27.2363, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.32581, dn = +|- 0.110777, dEa = +|- 0.609382 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8(41) + HO2(2) <=> H2O2(4) + C4H7(42)""",
)

entry(
    index = 22,
    label = "C4H10O(43) + HO2(2) <=> H2O2(4) + C4H9O(44)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000740853, 'cm^3/(mol*s)'),
        n = 4.38311,
        Ea = (56.8389, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.2143, dn = +|- 0.0254829, dEa = +|- 0.140181 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(43) + HO2(2) <=> H2O2(4) + C4H9O(44)""",
)

entry(
    index = 23,
    label = "C4H10(13) + HO2(2) <=> C4H9(45) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00210652, 'cm^3/(mol*s)'),
        n = 4.45303,
        Ea = (49.819, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.32839, dn = +|- 0.0372684, dEa = +|- 0.205013 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10(13) + HO2(2) <=> C4H9(45) + H2O2(4)""",
)

entry(
    index = 24,
    label = "C4H8O(46) + HO2(2) <=> H2O2(4) + C4H7O(47)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.05514e-08, 'cm^3/(mol*s)'),
        n = 5.43438,
        Ea = (20.7556, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.21916, dn = +|- 0.104616, dEa = +|- 0.575492 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(46) + HO2(2) <=> H2O2(4) + C4H7O(47)""",
)

entry(
    index = 25,
    label = "C3H6(48) + HO2(2) <=> H2O2(4) + C3H5(49)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.23038e-10, 'cm^3/(mol*s)'),
        n = 6.60553,
        Ea = (19.4098, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.5386, dn = +|- 0.122266, dEa = +|- 0.672585 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6(48) + HO2(2) <=> H2O2(4) + C3H5(49)""",
)

entry(
    index = 26,
    label = "C2H6O(50) + HO2(2) <=> H2O2(4) + C2H5O(51)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000409287, 'cm^3/(mol*s)'),
        n = 4.70424,
        Ea = (67.0893, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.42706, dn = +|- 0.0466716, dEa = +|- 0.256741 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H6O(50) + HO2(2) <=> H2O2(4) + C2H5O(51)""",
)

entry(
    index = 27,
    label = "C4H8O(17) + HO2(2) <=> H2O2(4) + C4H7O(52)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0059468, 'cm^3/(mol*s)'),
        n = 4.14413,
        Ea = (57.888, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.13258, dn = +|- 0.0163398, dEa = +|- 0.0898853 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(17) + HO2(2) <=> H2O2(4) + C4H7O(52)""",
)

entry(
    index = 28,
    label = "C4H8(15) + HO2(2) <=> C4H7(53) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.20615e-08, 'cm^3/(mol*s)'),
        n = 5.62053,
        Ea = (19.7262, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.56265, dn = +|- 0.123503, dEa = +|- 0.679391 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8(15) + HO2(2) <=> C4H7(53) + H2O2(4)""",
)

entry(
    index = 29,
    label = "C6H8(54) + HO2(2) <=> C6H7(55) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.01875e-07, 'cm^3/(mol*s)'),
        n = 5.07549,
        Ea = (10.2176, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.93084, dn = +|- 0.0863504, dEa = +|- 0.475014 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H8(54) + HO2(2) <=> C6H7(55) + H2O2(4)""",
)

entry(
    index = 30,
    label = "C4H10O(56) + HO2(2) <=> H2O2(4) + C4H9O(57)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0142764, 'cm^3/(mol*s)'),
        n = 4.09233,
        Ea = (66.0716, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.12286, dn = +|- 0.015208, dEa = +|- 0.0836592 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(56) + HO2(2) <=> H2O2(4) + C4H9O(57)""",
)

entry(
    index = 31,
    label = "C6H8(58) + HO2(2) <=> H2O2(4) + C6H7(59)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.81635e-06, 'cm^3/(mol*s)'),
        n = 5.07119,
        Ea = (13.2806, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.95305, dn = +|- 0.0878515, dEa = +|- 0.483272 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H8(58) + HO2(2) <=> H2O2(4) + C6H7(59)""",
)

entry(
    index = 32,
    label = "C2H6O(50) + HO2(2) <=> C2H5O(60) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000564314, 'cm^3/(mol*s)'),
        n = 4.34123,
        Ea = (31.9151, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.28242, dn = +|- 0.0326461, dEa = +|- 0.179587 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H6O(50) + HO2(2) <=> C2H5O(60) + H2O2(4)""",
)

entry(
    index = 33,
    label = "C3H8(25) + HO2(2) <=> H2O2(4) + C3H7(61)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000510827, 'cm^3/(mol*s)'),
        n = 4.59277,
        Ea = (58.4923, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.32453, dn = +|- 0.0368865, dEa = +|- 0.202913 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8(25) + HO2(2) <=> H2O2(4) + C3H7(61)""",
)

entry(
    index = 34,
    label = "C4H10O(43) + HO2(2) <=> C4H9O(62) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000166121, 'cm^3/(mol*s)'),
        n = 4.53539,
        Ea = (32.6901, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.36841, dn = +|- 0.0411636, dEa = +|- 0.226441 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(43) + HO2(2) <=> C4H9O(62) + H2O2(4)""",
)

entry(
    index = 35,
    label = "C4H8O(17) + HO2(2) <=> C4H7O(63) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.91164e-05, 'cm^3/(mol*s)'),
        n = 4.59616,
        Ea = (16.6055, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.52125, dn = +|- 0.0550603, dEa = +|- 0.302887 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(17) + HO2(2) <=> C4H7O(63) + H2O2(4)""",
)

entry(
    index = 36,
    label = "C3H6O(64) + HO2(2) <=> H2O2(4) + C3H5O(65)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.89078e-06, 'cm^3/(mol*s)'),
        n = 4.90542,
        Ea = (44.584, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.61705, dn = +|- 0.0630746, dEa = +|- 0.346973 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O(64) + HO2(2) <=> H2O2(4) + C3H5O(65)""",
)

entry(
    index = 37,
    label = "C2H6O(66) + HO2(2) <=> H2O2(4) + C2H5O(67)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00107875, 'cm^3/(mol*s)'),
        n = 4.37156,
        Ea = (38.6209, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.26938, dn = +|- 0.0313052, dEa = +|- 0.17221 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H6O(66) + HO2(2) <=> H2O2(4) + C2H5O(67)""",
)

entry(
    index = 38,
    label = "C4H8O(68) + HO2(2) <=> C4H7O(69) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.10146e-06, 'cm^3/(mol*s)'),
        n = 5.12066,
        Ea = (31.0702, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.82321, dn = +|- 0.0788229, dEa = +|- 0.433605 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(68) + HO2(2) <=> C4H7O(69) + H2O2(4)""",
)

entry(
    index = 39,
    label = "C2H4O(70) + HO2(2) <=> H2O2(4) + C2H3O(71)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.102149, 'cm^3/(mol*s)'),
        n = 3.87668,
        Ea = (70.1773, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.07587, dn = +|- 0.00959792, dEa = +|- 0.0527982 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O(70) + HO2(2) <=> H2O2(4) + C2H3O(71)""",
)

entry(
    index = 40,
    label = "C5H6(72) + HO2(2) <=> H2O2(4) + C5H5(73)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.75415e-08, 'cm^3/(mol*s)'),
        n = 5.57639,
        Ea = (16.934, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.51401, dn = +|- 0.120988, dEa = +|- 0.665557 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H6(72) + HO2(2) <=> H2O2(4) + C5H5(73)""",
)

entry(
    index = 41,
    label = "C4H8O(17) + HO2(2) <=> C4H7O(74) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.70895e-08, 'cm^3/(mol*s)'),
        n = 5.53146,
        Ea = (26.0936, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.42086, dn = +|- 0.116033, dEa = +|- 0.638298 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(17) + HO2(2) <=> C4H7O(74) + H2O2(4)""",
)

entry(
    index = 42,
    label = "C2H6(75) + HO2(2) <=> C2H5(76) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00107611, 'cm^3/(mol*s)'),
        n = 4.64503,
        Ea = (58.9259, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.37643, dn = +|- 0.0419307, dEa = +|- 0.230661 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H6(75) + HO2(2) <=> C2H5(76) + H2O2(4)""",
)

entry(
    index = 43,
    label = "C2H4O2(5) + HO2(2) <=> H2O2(4) + C2H3O2(77)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000104186, 'cm^3/(mol*s)'),
        n = 4.50983,
        Ea = (53.7734, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.315, dn = +|- 0.0359384, dEa = +|- 0.197697 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O2(5) + HO2(2) <=> H2O2(4) + C2H3O2(77)""",
)

entry(
    index = 44,
    label = "C4H10O(33) + HO2(2) <=> H2O2(4) + C4H9O(78)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.523e-05, 'cm^3/(mol*s)'),
        n = 4.57604,
        Ea = (61.4648, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.37128, dn = +|- 0.0414389, dEa = +|- 0.227956 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(33) + HO2(2) <=> H2O2(4) + C4H9O(78)""",
)

entry(
    index = 45,
    label = "C4H6O(79) + HO2(2) <=> C4H5O(80) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.63673e-05, 'cm^3/(mol*s)'),
        n = 4.91506,
        Ea = (23.471, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.76652, dn = +|- 0.0746773, dEa = +|- 0.4108 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O(79) + HO2(2) <=> C4H5O(80) + H2O2(4)""",
)

entry(
    index = 46,
    label = "C6H8(19) + HO2(2) <=> C6H7(81) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.96701e-10, 'cm^3/(mol*s)'),
        n = 6.4638,
        Ea = (13.0827, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.31164, dn = +|- 0.109974, dEa = +|- 0.604968 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H8(19) + HO2(2) <=> C6H7(81) + H2O2(4)""",
)

entry(
    index = 47,
    label = "C4H8O(68) + HO2(2) <=> H2O2(4) + C4H7O(82)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.05561e-07, 'cm^3/(mol*s)'),
        n = 5.00571,
        Ea = (50.7329, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.73253, dn = +|- 0.0721277, dEa = +|- 0.396774 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(68) + HO2(2) <=> H2O2(4) + C4H7O(82)""",
)

entry(
    index = 48,
    label = "C3H6O(83) + HO2(2) <=> C3H5O(84) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000293965, 'cm^3/(mol*s)'),
        n = 4.67279,
        Ea = (13.2914, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.50013, dn = +|- 0.0532249, dEa = +|- 0.29279 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O(83) + HO2(2) <=> C3H5O(84) + H2O2(4)""",
)

entry(
    index = 49,
    label = "C4H10(23) + HO2(2) <=> H2O2(4) + C4H9(85)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000832921, 'cm^3/(mol*s)'),
        n = 4.41042,
        Ea = (60.4783, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.25863, dn = +|- 0.0301881, dEa = +|- 0.166065 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10(23) + HO2(2) <=> H2O2(4) + C4H9(85)""",
)

entry(
    index = 50,
    label = "C4H10O(86) + HO2(2) <=> H2O2(4) + C4H9O(87)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.001262, 'cm^3/(mol*s)'),
        n = 4.35918,
        Ea = (59.5366, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.22938, dn = +|- 0.0271023, dEa = +|- 0.14909 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(86) + HO2(2) <=> H2O2(4) + C4H9O(87)""",
)

entry(
    index = 51,
    label = "CH4O(88) + HO2(2) <=> H2O2(4) + CH3O(89)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.64717e-05, 'cm^3/(mol*s)'),
        n = 4.75283,
        Ea = (41.0765, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.49505, dn = +|- 0.0527799, dEa = +|- 0.290342 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for CH4O(88) + HO2(2) <=> H2O2(4) + CH3O(89)""",
)

entry(
    index = 52,
    label = "C4H10O(43) + HO2(2) <=> C4H9O(90) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000375686, 'cm^3/(mol*s)'),
        n = 4.61727,
        Ea = (47.4469, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.3677, dn = +|- 0.0410955, dEa = +|- 0.226066 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(43) + HO2(2) <=> C4H9O(90) + H2O2(4)""",
)

entry(
    index = 53,
    label = "C4H10O(86) + HO2(2) <=> C4H9O(91) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000391488, 'cm^3/(mol*s)'),
        n = 4.50526,
        Ea = (36.07, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.36394, dn = +|- 0.0407347, dEa = +|- 0.224082 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(86) + HO2(2) <=> C4H9O(91) + H2O2(4)""",
)

entry(
    index = 54,
    label = "C4H8O(68) + HO2(2) <=> H2O2(4) + C4H7O(92)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000631728, 'cm^3/(mol*s)'),
        n = 4.64055,
        Ea = (66.8149, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.40113, dn = +|- 0.0442652, dEa = +|- 0.243503 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(68) + HO2(2) <=> H2O2(4) + C4H7O(92)""",
)

entry(
    index = 55,
    label = "C5H8(93) + HO2(2) <=> H2O2(4) + C5H7(94)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.0144e-10, 'cm^3/(mol*s)'),
        n = 6.30656,
        Ea = (24.2759, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 3.91317, dn = +|- 0.179058, dEa = +|- 0.985 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8(93) + HO2(2) <=> H2O2(4) + C5H7(94)""",
)

entry(
    index = 56,
    label = "CH2O(95) + HO2(2) <=> H2O2(4) + CHO(96)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.23547e-06, 'cm^3/(mol*s)'),
        n = 5.20393,
        Ea = (21.3195, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.04626, dn = +|- 0.0939706, dEa = +|- 0.516933 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for CH2O(95) + HO2(2) <=> H2O2(4) + CHO(96)""",
)

entry(
    index = 57,
    label = "C4H10O(43) + HO2(2) <=> C4H9O(97) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0157366, 'cm^3/(mol*s)'),
        n = 3.87722,
        Ea = (45.4966, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.06497, dn = +|- 0.00826126, dEa = +|- 0.0454452 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(43) + HO2(2) <=> C4H9O(97) + H2O2(4)""",
)

