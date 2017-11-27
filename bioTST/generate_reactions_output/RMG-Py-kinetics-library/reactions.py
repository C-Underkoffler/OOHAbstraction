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
    duplicate = True,
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
    duplicate = True,
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

entry(
    index = 58,
    label = "C5H6O(98) + HO2(2) <=> H2O2(4) + C5H5O(99)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.12783e-05, 'cm^3/(mol*s)'),
        n = 4.72352,
        Ea = (7.13709, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.59015, dn = +|- 0.0608733, dEa = +|- 0.334864 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H6O(98) + HO2(2) <=> H2O2(4) + C5H5O(99)""",
)

entry(
    index = 59,
    label = "C5H6O(100) + HO2(2) <=> H2O2(4) + C5H5O(101)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000170319, 'cm^3/(mol*s)'),
        n = 4.61962,
        Ea = (12.6354, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.60068, dn = +|- 0.0617396, dEa = +|- 0.33963 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H6O(100) + HO2(2) <=> H2O2(4) + C5H5O(101)""",
)

entry(
    index = 60,
    label = "C6H10O(102) + HO2(2) <=> H2O2(4) + C6H9O(103)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.55372e-07, 'cm^3/(mol*s)'),
        n = 5.11729,
        Ea = (14.3227, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.78771, dn = +|- 0.0762425, dEa = +|- 0.41941 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H10O(102) + HO2(2) <=> H2O2(4) + C6H9O(103)""",
)

entry(
    index = 61,
    label = "C5H10(104) + HO2(2) <=> C5H9(105) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.82936e-08, 'cm^3/(mol*s)'),
        n = 5.57639,
        Ea = (21.9866, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.59144, dn = +|- 0.12497, dEa = +|- 0.687458 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10(104) + HO2(2) <=> C5H9(105) + H2O2(4)""",
)

entry(
    index = 62,
    label = "C6H10O(106) + HO2(2) <=> H2O2(4) + C6H9O(107)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0114732, 'cm^3/(mol*s)'),
        n = 3.89426,
        Ea = (57.6883, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.07028, dn = +|- 0.00891434, dEa = +|- 0.0490378 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H10O(106) + HO2(2) <=> H2O2(4) + C6H9O(107)""",
)

entry(
    index = 63,
    label = "C3H4O3(108) + HO2(2) <=> C3H3O3(109) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.46381e-10, 'cm^3/(mol*s)'),
        n = 6.0746,
        Ea = (20.7976, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 3.18244, dn = +|- 0.151931, dEa = +|- 0.835772 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4O3(108) + HO2(2) <=> C3H3O3(109) + H2O2(4)""",
)

entry(
    index = 64,
    label = "C5H10O(110) + HO2(2) <=> H2O2(4) + C5H9O(111)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000361794, 'cm^3/(mol*s)'),
        n = 4.67589,
        Ea = (51.9521, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.43309, dn = +|- 0.047225, dEa = +|- 0.259785 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(110) + HO2(2) <=> H2O2(4) + C5H9O(111)""",
)

entry(
    index = 65,
    label = "C4H6O(112) + HO2(2) <=> C4H5O(113) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.26288e-05, 'cm^3/(mol*s)'),
        n = 4.75547,
        Ea = (17.2215, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.6202, dn = +|- 0.0633302, dEa = +|- 0.34838 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O(112) + HO2(2) <=> C4H5O(113) + H2O2(4)""",
)

entry(
    index = 66,
    label = "C7H8(114) + HO2(2) <=> C7H7(115) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.55735e-05, 'cm^3/(mol*s)'),
        n = 5.09377,
        Ea = (-2.60251, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.15687, dn = +|- 0.0191237, dEa = +|- 0.1052 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H8(114) + HO2(2) <=> C7H7(115) + H2O2(4)""",
)

entry(
    index = 67,
    label = "C5H8O(116) + HO2(2) <=> H2O2(4) + C5H7O(117)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00802742, 'cm^3/(mol*s)'),
        n = 3.97344,
        Ea = (51.4742, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.08142, dn = +|- 0.010273, dEa = +|- 0.056512 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(116) + HO2(2) <=> H2O2(4) + C5H7O(117)""",
)

entry(
    index = 68,
    label = "C4H6O2(118) + HO2(2) <=> H2O2(4) + C4H5O2(119)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.228563, 'cm^3/(mol*s)'),
        n = 3.85957,
        Ea = (100.481, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.06853, dn = +|- 0.00869905, dEa = +|- 0.0478535 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O2(118) + HO2(2) <=> H2O2(4) + C4H5O2(119)""",
)

entry(
    index = 69,
    label = "CH2O2(120) + HO2(2) <=> H2O2(4) + CHO2(121)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.16738, 'cm^3/(mol*s)'),
        n = 3.6382,
        Ea = (96.8331, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.02165, dn = +|- 0.00281125, dEa = +|- 0.0154647 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for CH2O2(120) + HO2(2) <=> H2O2(4) + CHO2(121)""",
)

entry(
    index = 70,
    label = "C6H12(122) + HO2(2) <=> C6H11(123) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00126402, 'cm^3/(mol*s)'),
        n = 4.35832,
        Ea = (49.4485, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.26192, dn = +|- 0.0305317, dEa = +|- 0.167955 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12(122) + HO2(2) <=> C6H11(123) + H2O2(4)""",
)

entry(
    index = 71,
    label = "C5H12(124) + HO2(2) <=> C5H11(125) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00483184, 'cm^3/(mol*s)'),
        n = 4.25851,
        Ea = (39.4875, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.22068, dn = +|- 0.0261707, dEa = +|- 0.143965 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(124) + HO2(2) <=> C5H11(125) + H2O2(4)""",
)

entry(
    index = 72,
    label = "C3H8O(126) + HO2(2) <=> H2O2(4) + C3H7O(127)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000461344, 'cm^3/(mol*s)'),
        n = 4.49371,
        Ea = (61.8638, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.31972, dn = +|- 0.0364087, dEa = +|- 0.200284 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8O(126) + HO2(2) <=> H2O2(4) + C3H7O(127)""",
)

entry(
    index = 73,
    label = "C5H8O2(128) + HO2(2) <=> H2O2(4) + C5H7O2(129)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.96075e-09, 'cm^3/(mol*s)'),
        n = 5.81809,
        Ea = (24.2053, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.9056, dn = +|- 0.139987, dEa = +|- 0.770069 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O2(128) + HO2(2) <=> H2O2(4) + C5H7O2(129)""",
)

entry(
    index = 74,
    label = "C3H8O(130) + HO2(2) <=> H2O2(4) + C3H7O(131)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000348513, 'cm^3/(mol*s)'),
        n = 4.53302,
        Ea = (66.5864, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.32675, dn = +|- 0.0371059, dEa = +|- 0.20412 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8O(130) + HO2(2) <=> H2O2(4) + C3H7O(131)""",
)

entry(
    index = 75,
    label = "C5H10O(132) + HO2(2) <=> H2O2(4) + C5H9O(133)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0145262, 'cm^3/(mol*s)'),
        n = 3.80511,
        Ea = (57.7743, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.05418, dn = +|- 0.00692463, dEa = +|- 0.0380924 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(132) + HO2(2) <=> H2O2(4) + C5H9O(133)""",
)

entry(
    index = 76,
    label = "C3H4O3(134) + HO2(2) <=> C3H3O3(135) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.87971e-07, 'cm^3/(mol*s)'),
        n = 5.45116,
        Ea = (21.2124, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.11512, dn = +|- 0.0983145, dEa = +|- 0.540828 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4O3(134) + HO2(2) <=> C3H3O3(135) + H2O2(4)""",
)

entry(
    index = 77,
    label = "C5H8O(136) + HO2(2) <=> C5H7O(137) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000219287, 'cm^3/(mol*s)'),
        n = 4.66965,
        Ea = (18.4724, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.58821, dn = +|- 0.060713, dEa = +|- 0.333982 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(136) + HO2(2) <=> C5H7O(137) + H2O2(4)""",
)

entry(
    index = 78,
    label = "C7H12(138) + HO2(2) <=> H2O2(4) + C7H11(139)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.24649e-08, 'cm^3/(mol*s)'),
        n = 5.60943,
        Ea = (27.1191, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.49933, dn = +|- 0.12022, dEa = +|- 0.661328 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H12(138) + HO2(2) <=> H2O2(4) + C7H11(139)""",
)

entry(
    index = 79,
    label = "C7H8(140) + HO2(2) <=> C7H7(141) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.68621e-05, 'cm^3/(mol*s)'),
        n = 4.6047,
        Ea = (3.1184, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.45361, dn = +|- 0.049091, dEa = +|- 0.27005 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H8(140) + HO2(2) <=> C7H7(141) + H2O2(4)""",
)

entry(
    index = 80,
    label = "C4H6O(112) + HO2(2) <=> C4H5O(142) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.06564e-08, 'cm^3/(mol*s)'),
        n = 5.3915,
        Ea = (12.0237, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.24336, dn = +|- 0.10604, dEa = +|- 0.583324 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O(112) + HO2(2) <=> C4H5O(142) + H2O2(4)""",
)

entry(
    index = 81,
    label = "C5H10O(143) + HO2(2) <=> C5H9O(144) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000465233, 'cm^3/(mol*s)'),
        n = 4.45855,
        Ea = (47.2106, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.2802, dn = +|- 0.0324186, dEa = +|- 0.178335 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(143) + HO2(2) <=> C5H9O(144) + H2O2(4)""",
)

entry(
    index = 82,
    label = "C5H8O(145) + HO2(2) <=> H2O2(4) + C5H7O(146)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.87713e-08, 'cm^3/(mol*s)'),
        n = 5.75789,
        Ea = (26.0319, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.96685, dn = +|- 0.142725, dEa = +|- 0.785129 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(145) + HO2(2) <=> H2O2(4) + C5H7O(146)""",
)

entry(
    index = 83,
    label = "C3H8O(126) + HO2(2) <=> C3H7O(147) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000358264, 'cm^3/(mol*s)'),
        n = 4.40545,
        Ea = (36.0846, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.34315, dn = +|- 0.0387185, dEa = +|- 0.21299 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8O(126) + HO2(2) <=> C3H7O(147) + H2O2(4)""",
)

entry(
    index = 84,
    label = "CH2O2(120) + HO2(2) <=> CHO2(148) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00509617, 'cm^3/(mol*s)'),
        n = 4.05194,
        Ea = (31.2032, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.1489, dn = +|- 0.0182168, dEa = +|- 0.100211 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for CH2O2(120) + HO2(2) <=> CHO2(148) + H2O2(4)""",
)

entry(
    index = 85,
    label = "C5H10(149) + HO2(2) <=> C5H9(150) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.28196e-07, 'cm^3/(mol*s)'),
        n = 5.39686,
        Ea = (20.0928, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.32117, dn = +|- 0.110514, dEa = +|- 0.60794 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10(149) + HO2(2) <=> C5H9(150) + H2O2(4)""",
)

entry(
    index = 86,
    label = "C7H14(151) + HO2(2) <=> H2O2(4) + C7H13(152)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.21402e-09, 'cm^3/(mol*s)'),
        n = 5.66517,
        Ea = (24.7896, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.7249, dn = +|- 0.13156, dEa = +|- 0.723714 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(151) + HO2(2) <=> H2O2(4) + C7H13(152)""",
)

entry(
    index = 87,
    label = "C7H14(153) + HO2(2) <=> C7H13(154) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000120537, 'cm^3/(mol*s)'),
        n = 4.66555,
        Ea = (52.379, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.46815, dn = +|- 0.0503972, dEa = +|- 0.277235 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(153) + HO2(2) <=> C7H13(154) + H2O2(4)""",
)

entry(
    index = 88,
    label = "C7H14(153) + HO2(2) <=> H2O2(4) + C7H13(155)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.60398e-05, 'cm^3/(mol*s)'),
        n = 4.74358,
        Ea = (63.8521, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.49211, dn = +|- 0.0525215, dEa = +|- 0.288921 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(153) + HO2(2) <=> H2O2(4) + C7H13(155)""",
)

entry(
    index = 89,
    label = "C3H4O3(108) + HO2(2) <=> C3H3O3(156) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00062496, 'cm^3/(mol*s)'),
        n = 4.16015,
        Ea = (10.4933, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.17726, dn = +|- 0.0214174, dEa = +|- 0.117817 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4O3(108) + HO2(2) <=> C3H3O3(156) + H2O2(4)""",
)

entry(
    index = 90,
    label = "C6H12(122) + HO2(2) <=> C6H11(157) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00100139, 'cm^3/(mol*s)'),
        n = 4.46378,
        Ea = (48.8841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.31767, dn = +|- 0.0362051, dEa = +|- 0.199165 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12(122) + HO2(2) <=> C6H11(157) + H2O2(4)""",
)

entry(
    index = 91,
    label = "C7H14(153) + HO2(2) <=> C7H13(158) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00136098, 'cm^3/(mol*s)'),
        n = 4.39776,
        Ea = (50.8253, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.28772, dn = +|- 0.0331873, dEa = +|- 0.182563 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(153) + HO2(2) <=> C7H13(158) + H2O2(4)""",
)

entry(
    index = 92,
    label = "C6H12O(159) + HO2(2) <=> H2O2(4) + C6H11O(160)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000435069, 'cm^3/(mol*s)'),
        n = 4.40483,
        Ea = (57.9043, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.22723, dn = +|- 0.0268733, dEa = +|- 0.14783 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(159) + HO2(2) <=> H2O2(4) + C6H11O(160)""",
)

entry(
    index = 93,
    label = "C3H8O(130) + HO2(2) <=> C3H7O(161) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00161843, 'cm^3/(mol*s)'),
        n = 4.41608,
        Ea = (31.2187, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.34896, dn = +|- 0.0392853, dEa = +|- 0.216109 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8O(130) + HO2(2) <=> C3H7O(161) + H2O2(4)""",
)

entry(
    index = 94,
    label = "C7H10(162) + HO2(2) <=> H2O2(4) + C7H9(163)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.50381e-08, 'cm^3/(mol*s)'),
        n = 5.67296,
        Ea = (15.8252, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.65616, dn = +|- 0.128207, dEa = +|- 0.705266 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H10(162) + HO2(2) <=> H2O2(4) + C7H9(163)""",
)

entry(
    index = 95,
    label = "C6H10O(102) + HO2(2) <=> H2O2(4) + C6H9O(164)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0221951, 'cm^3/(mol*s)'),
        n = 3.87815,
        Ea = (52.5291, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.06472, dn = +|- 0.00823067, dEa = +|- 0.0452769 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H10O(102) + HO2(2) <=> H2O2(4) + C6H9O(164)""",
)

entry(
    index = 96,
    label = "C3H2O3(165) + HO2(2) <=> C3HO3(166) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00288574, 'cm^3/(mol*s)'),
        n = 4.41263,
        Ea = (60.7819, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.29956, dn = +|- 0.0343888, dEa = +|- 0.189173 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H2O3(165) + HO2(2) <=> C3HO3(166) + H2O2(4)""",
)

entry(
    index = 97,
    label = "C7H14(167) + HO2(2) <=> C7H13(168) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.72086e-08, 'cm^3/(mol*s)'),
        n = 5.32048,
        Ea = (18.5576, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.29457, dn = +|- 0.109002, dEa = +|- 0.599619 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(167) + HO2(2) <=> C7H13(168) + H2O2(4)""",
)

entry(
    index = 98,
    label = "C6H12O(159) + HO2(2) <=> C6H11O(169) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.02307e-09, 'cm^3/(mol*s)'),
        n = 5.71222,
        Ea = (30.2333, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.53715, dn = +|- 0.122191, dEa = +|- 0.672172 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(159) + HO2(2) <=> C6H11O(169) + H2O2(4)""",
)

entry(
    index = 99,
    label = "C5H6(170) + HO2(2) <=> H2O2(4) + C5H5(73)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (2.7355e-08, 'cm^3/(mol*s)'),
        n = 5.5772,
        Ea = (16.9238, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.51468, dn = +|- 0.121024, dEa = +|- 0.665751 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H6(170) + HO2(2) <=> H2O2(4) + C5H5(73)""",
)

entry(
    index = 100,
    label = "C5H10O(143) + HO2(2) <=> C5H9O(171) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00142415, 'cm^3/(mol*s)'),
        n = 4.5134,
        Ea = (18.0511, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.47877, dn = +|- 0.0513431, dEa = +|- 0.282439 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(143) + HO2(2) <=> C5H9O(171) + H2O2(4)""",
)

entry(
    index = 101,
    label = "C6H12O(172) + HO2(2) <=> C6H11O(173) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00019002, 'cm^3/(mol*s)'),
        n = 4.26476,
        Ea = (46.4659, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.20984, dn = +|- 0.0249995, dEa = +|- 0.137522 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(172) + HO2(2) <=> C6H11O(173) + H2O2(4)""",
)

entry(
    index = 102,
    label = "C2H2O3(174) + HO2(2) <=> C2HO3(175) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000488607, 'cm^3/(mol*s)'),
        n = 4.60737,
        Ea = (49.748, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.39381, dn = +|- 0.0435772, dEa = +|- 0.239718 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H2O3(174) + HO2(2) <=> C2HO3(175) + H2O2(4)""",
)

entry(
    index = 103,
    label = "C2H4(176) + HO2(2) <=> H2O2(4) + C2H3(177)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.265705, 'cm^3/(mol*s)'),
        n = 3.96021,
        Ea = (92.4156, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.08257, dn = +|- 0.0104122, dEa = +|- 0.0572774 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4(176) + HO2(2) <=> H2O2(4) + C2H3(177)""",
)

entry(
    index = 104,
    label = "C4H10O(178) + HO2(2) <=> C4H9O(179) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000282731, 'cm^3/(mol*s)'),
        n = 4.50922,
        Ea = (35.0027, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.37477, dn = +|- 0.0417724, dEa = +|- 0.22979 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(178) + HO2(2) <=> C4H9O(179) + H2O2(4)""",
)

entry(
    index = 105,
    label = "C5H10O(180) + HO2(2) <=> H2O2(4) + C5H9O(181)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.01782e-06, 'cm^3/(mol*s)'),
        n = 4.93933,
        Ea = (43.7026, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.65342, dn = +|- 0.0659939, dEa = +|- 0.363032 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(180) + HO2(2) <=> H2O2(4) + C5H9O(181)""",
)

entry(
    index = 106,
    label = "C5H12(182) + HO2(2) <=> C5H11(183) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000190466, 'cm^3/(mol*s)'),
        n = 4.63624,
        Ea = (44.7453, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.36159, dn = +|- 0.040508, dEa = +|- 0.222835 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(182) + HO2(2) <=> C5H11(183) + H2O2(4)""",
)

entry(
    index = 107,
    label = "C5H10O(110) + HO2(2) <=> H2O2(4) + C5H9O(184)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.25905e-05, 'cm^3/(mol*s)'),
        n = 4.94049,
        Ea = (43.3724, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.65111, dn = +|- 0.0658102, dEa = +|- 0.362022 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(110) + HO2(2) <=> H2O2(4) + C5H9O(184)""",
)

entry(
    index = 108,
    label = "C5H12(124) + HO2(2) <=> H2O2(4) + C5H11(185)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.21803e-05, 'cm^3/(mol*s)'),
        n = 4.5993,
        Ea = (57.5134, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.36763, dn = +|- 0.0410888, dEa = +|- 0.226029 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(124) + HO2(2) <=> H2O2(4) + C5H11(185)""",
)

entry(
    index = 109,
    label = "C5H10O(110) + HO2(2) <=> H2O2(4) + C5H9O(186)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.84535e-05, 'cm^3/(mol*s)'),
        n = 4.81555,
        Ea = (58.9839, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.57087, dn = +|- 0.0592724, dEa = +|- 0.326057 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(110) + HO2(2) <=> H2O2(4) + C5H9O(186)""",
)

entry(
    index = 110,
    label = "C5H10(104) + HO2(2) <=> C5H9(187) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000315487, 'cm^3/(mol*s)'),
        n = 4.50876,
        Ea = (47.5193, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.30674, dn = +|- 0.0351114, dEa = +|- 0.193148 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10(104) + HO2(2) <=> C5H9(187) + H2O2(4)""",
)

entry(
    index = 111,
    label = "C6H10O(102) + HO2(2) <=> C6H9O(188) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.14443e-06, 'cm^3/(mol*s)'),
        n = 4.81706,
        Ea = (28.1356, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.54114, dn = +|- 0.0567649, dEa = +|- 0.312264 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H10O(102) + HO2(2) <=> C6H9O(188) + H2O2(4)""",
)

entry(
    index = 112,
    label = "C4H8O(189) + HO2(2) <=> C4H7O(190) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.04843e-06, 'cm^3/(mol*s)'),
        n = 4.79274,
        Ea = (14.1732, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.74322, dn = +|- 0.0729353, dEa = +|- 0.401217 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(189) + HO2(2) <=> C4H7O(190) + H2O2(4)""",
)

entry(
    index = 113,
    label = "C5H12(182) + HO2(2) <=> C5H11(191) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000375325, 'cm^3/(mol*s)'),
        n = 4.55086,
        Ea = (46.0816, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.30718, dn = +|- 0.0351554, dEa = +|- 0.19339 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(182) + HO2(2) <=> C5H11(191) + H2O2(4)""",
)

entry(
    index = 114,
    label = "C3H2O4(192) + HO2(2) <=> C3HO4(193) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.64583e-06, 'cm^3/(mol*s)'),
        n = 5.84699,
        Ea = (55.5868, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.55717, dn = +|- 0.0581227, dEa = +|- 0.319733 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H2O4(192) + HO2(2) <=> C3HO4(193) + H2O2(4)""",
)

entry(
    index = 115,
    label = "C5H12(124) + HO2(2) <=> H2O2(4) + C5H11(194)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000678368, 'cm^3/(mol*s)'),
        n = 4.47401,
        Ea = (58.974, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.27439, dn = +|- 0.0318216, dEa = +|- 0.175051 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(124) + HO2(2) <=> H2O2(4) + C5H11(194)""",
)

entry(
    index = 116,
    label = "C5H8O(195) + HO2(2) <=> C5H7O(196) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (4.6226e-05, 'cm^3/(mol*s)'),
        n = 4.86568,
        Ea = (22.7711, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.78423, dn = +|- 0.0759867, dEa = +|- 0.418003 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(195) + HO2(2) <=> C5H7O(196) + H2O2(4)""",
)

entry(
    index = 117,
    label = "C6H14(197) + HO2(2) <=> C6H13(198) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000468774, 'cm^3/(mol*s)'),
        n = 4.53367,
        Ea = (47.5335, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.35032, dn = +|- 0.039417, dEa = +|- 0.216833 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H14(197) + HO2(2) <=> C6H13(198) + H2O2(4)""",
)

entry(
    index = 118,
    label = "C5H12(124) + HO2(2) <=> C5H11(199) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0024808, 'cm^3/(mol*s)'),
        n = 4.37053,
        Ea = (46.7402, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.24471, dn = +|- 0.0287286, dEa = +|- 0.158036 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(124) + HO2(2) <=> C5H11(199) + H2O2(4)""",
)

entry(
    index = 119,
    label = "C2H4O(31) + HO2(2) <=> H2O2(4) + C2H3O(200)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.13215e-07, 'cm^3/(mol*s)'),
        n = 5.33323,
        Ea = (45.1551, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.08967, dn = +|- 0.0967257, dEa = +|- 0.532088 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O(31) + HO2(2) <=> H2O2(4) + C2H3O(200)""",
)

entry(
    index = 120,
    label = "C3H4O3(108) + HO2(2) <=> C3H3O3(201) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000507, 'cm^3/(mol*s)'),
        n = 4.593,
        Ea = (53.7226, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.36444, dn = +|- 0.040782, dEa = +|- 0.224342 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4O3(108) + HO2(2) <=> C3H3O3(201) + H2O2(4)""",
)

entry(
    index = 121,
    label = "C5H10(104) + HO2(2) <=> H2O2(4) + C5H9(202)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000863445, 'cm^3/(mol*s)'),
        n = 4.46539,
        Ea = (58.4953, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.25872, dn = +|- 0.0301979, dEa = +|- 0.166119 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10(104) + HO2(2) <=> H2O2(4) + C5H9(202)""",
)

entry(
    index = 122,
    label = "C4H10O(178) + HO2(2) <=> H2O2(4) + C4H9O(203)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.65424e-06, 'cm^3/(mol*s)'),
        n = 5.31449,
        Ea = (71.5509, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.89613, dn = +|- 0.0839702, dEa = +|- 0.46192 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H10O(178) + HO2(2) <=> H2O2(4) + C4H9O(203)""",
)

entry(
    index = 123,
    label = "C3H6O3(204) + HO2(2) <=> H2O2(4) + C3H5O3(205)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0194118, 'cm^3/(mol*s)'),
        n = 3.83268,
        Ea = (38.5247, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.06373, dn = +|- 0.00810811, dEa = +|- 0.0446027 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O3(204) + HO2(2) <=> H2O2(4) + C3H5O3(205)""",
)

entry(
    index = 124,
    label = "C3H8O(126) + HO2(2) <=> C3H7O(206) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.0139973, 'cm^3/(mol*s)'),
        n = 3.94442,
        Ea = (47.9109, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.09009, dn = +|- 0.0113214, dEa = +|- 0.0622791 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8O(126) + HO2(2) <=> C3H7O(206) + H2O2(4)""",
)

entry(
    index = 125,
    label = "C5H8O(207) + HO2(2) <=> C5H7O(208) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.47687e-05, 'cm^3/(mol*s)'),
        n = 4.92848,
        Ea = (29.9282, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.79755, dn = +|- 0.0769631, dEa = +|- 0.423374 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(207) + HO2(2) <=> C5H7O(208) + H2O2(4)""",
)

entry(
    index = 126,
    label = "C5H8O(195) + HO2(2) <=> H2O2(4) + C5H7O(209)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.87226e-09, 'cm^3/(mol*s)'),
        n = 5.75392,
        Ea = (27.3486, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.79556, dn = +|- 0.13492, dEa = +|- 0.742194 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(195) + HO2(2) <=> H2O2(4) + C5H7O(209)""",
)

entry(
    index = 127,
    label = "C6H14(197) + HO2(2) <=> C6H13(210) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00015669, 'cm^3/(mol*s)'),
        n = 4.4528,
        Ea = (46.7795, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.29246, dn = +|- 0.0336692, dEa = +|- 0.185214 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H14(197) + HO2(2) <=> C6H13(210) + H2O2(4)""",
)

entry(
    index = 128,
    label = "C5H10O(211) + HO2(2) <=> H2O2(4) + C5H9O(212)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.08521e-08, 'cm^3/(mol*s)'),
        n = 5.84966,
        Ea = (39.8384, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.55771, dn = +|- 0.0581684, dEa = +|- 0.319985 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(211) + HO2(2) <=> H2O2(4) + C5H9O(212)""",
)

entry(
    index = 129,
    label = "C6H8(213) + HO2(2) <=> H2O2(4) + C6H7(59)",
    degeneracy = 1,
    duplicate = True,
    kinetics = Arrhenius(
        A = (5.60285e-06, 'cm^3/(mol*s)'),
        n = 5.03863,
        Ea = (17.4408, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.97032, dn = +|- 0.0890069, dEa = +|- 0.489627 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H8(213) + HO2(2) <=> H2O2(4) + C6H7(59)""",
)

entry(
    index = 130,
    label = "C3H4(214) + HO2(2) <=> C3H3(215) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.02065e-08, 'cm^3/(mol*s)'),
        n = 5.56952,
        Ea = (34.8886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.33181, dn = +|- 0.111115, dEa = +|- 0.611241 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4(214) + HO2(2) <=> C3H3(215) + H2O2(4)""",
)

entry(
    index = 131,
    label = "C5H8O(216) + HO2(2) <=> H2O2(4) + C5H7O(217)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.70994e-08, 'cm^3/(mol*s)'),
        n = 5.48408,
        Ea = (47.9008, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.19788, dn = +|- 0.103351, dEa = +|- 0.568535 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(216) + HO2(2) <=> H2O2(4) + C5H7O(217)""",
)

entry(
    index = 132,
    label = "C4H6O(38) + HO2(2) <=> H2O2(4) + C4H5O(218)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.08079e-08, 'cm^3/(mol*s)'),
        n = 5.53033,
        Ea = (29.3721, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.27191, dn = +|- 0.107699, dEa = +|- 0.592453 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O(38) + HO2(2) <=> H2O2(4) + C4H5O(218)""",
)

entry(
    index = 133,
    label = "C7H12(219) + HO2(2) <=> H2O2(4) + C7H11(220)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.96589e-09, 'cm^3/(mol*s)'),
        n = 5.61724,
        Ea = (24.0478, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.57726, dn = +|- 0.12425, dEa = +|- 0.683497 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H12(219) + HO2(2) <=> H2O2(4) + C7H11(220)""",
)

entry(
    index = 134,
    label = "C5H10O(211) + HO2(2) <=> C5H9O(221) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.17611e-09, 'cm^3/(mol*s)'),
        n = 6.37963,
        Ea = (17.6927, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.23777, dn = +|- 0.105712, dEa = +|- 0.581523 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(211) + HO2(2) <=> C5H9O(221) + H2O2(4)""",
)

entry(
    index = 135,
    label = "C5H10O(143) + HO2(2) <=> H2O2(4) + C5H9O(222)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000451636, 'cm^3/(mol*s)'),
        n = 4.31888,
        Ea = (58.1426, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.20659, dn = +|- 0.0246474, dEa = +|- 0.135585 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(143) + HO2(2) <=> H2O2(4) + C5H9O(222)""",
)

entry(
    index = 136,
    label = "C3H6O3(204) + HO2(2) <=> C3H5O3(223) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00484826, 'cm^3/(mol*s)'),
        n = 4.11104,
        Ea = (51.3067, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.06146, dn = +|- 0.00782834, dEa = +|- 0.0430637 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O3(204) + HO2(2) <=> C3H5O3(223) + H2O2(4)""",
)

entry(
    index = 137,
    label = "C3H8O2(224) + HO2(2) <=> C3H7O2(225) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000405537, 'cm^3/(mol*s)'),
        n = 4.37835,
        Ea = (23.7318, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.28241, dn = +|- 0.0326449, dEa = +|- 0.17958 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H8O2(224) + HO2(2) <=> C3H7O2(225) + H2O2(4)""",
)

entry(
    index = 138,
    label = "C4H6O2(118) + HO2(2) <=> H2O2(4) + C4H5O2(226)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000408181, 'cm^3/(mol*s)'),
        n = 4.20427,
        Ea = (48.1227, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.16662, dn = +|- 0.0202255, dEa = +|- 0.111261 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O2(118) + HO2(2) <=> H2O2(4) + C4H5O2(226)""",
)

entry(
    index = 139,
    label = "C5H8O(116) + HO2(2) <=> C5H7O(227) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.55467e-07, 'cm^3/(mol*s)'),
        n = 5.27471,
        Ea = (26.5385, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.01526, dn = +|- 0.0919671, dEa = +|- 0.505911 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(116) + HO2(2) <=> C5H7O(227) + H2O2(4)""",
)

entry(
    index = 140,
    label = "C6H12O(172) + HO2(2) <=> C6H11O(228) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.56887e-10, 'cm^3/(mol*s)'),
        n = 5.8952,
        Ea = (27.996, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.99859, dn = +|- 0.144121, dEa = +|- 0.792811 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(172) + HO2(2) <=> C6H11O(228) + H2O2(4)""",
)

entry(
    index = 141,
    label = "CH4O2(229) + HO2(2) <=> CH3O2(230) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.25347e-05, 'cm^3/(mol*s)'),
        n = 4.61955,
        Ea = (0.462874, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.41572, dn = +|- 0.045624, dEa = +|- 0.250978 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for CH4O2(229) + HO2(2) <=> CH3O2(230) + H2O2(4)""",
)

entry(
    index = 142,
    label = "C3H6O(83) + HO2(2) <=> C3H5O(231) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.5612e-08, 'cm^3/(mol*s)'),
        n = 5.63323,
        Ea = (25.7729, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.52069, dn = +|- 0.121336, dEa = +|- 0.667472 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O(83) + HO2(2) <=> C3H5O(231) + H2O2(4)""",
)

entry(
    index = 143,
    label = "C3H6O2(232) + HO2(2) <=> C3H5O2(233) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.61147e-07, 'cm^3/(mol*s)'),
        n = 5.39794,
        Ea = (53.3084, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.06096, dn = +|- 0.09491, dEa = +|- 0.5221 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O2(232) + HO2(2) <=> C3H5O2(233) + H2O2(4)""",
)

entry(
    index = 144,
    label = "C6H10O(106) + HO2(2) <=> C6H9O(234) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.93324e-08, 'cm^3/(mol*s)'),
        n = 5.57703,
        Ea = (24.3886, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.57598, dn = +|- 0.124184, dEa = +|- 0.683136 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H10O(106) + HO2(2) <=> C6H9O(234) + H2O2(4)""",
)

entry(
    index = 145,
    label = "C6H12O(172) + HO2(2) <=> C6H11O(235) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.38992e-05, 'cm^3/(mol*s)'),
        n = 4.59948,
        Ea = (17.9284, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.55725, dn = +|- 0.0581294, dEa = +|- 0.31977 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(172) + HO2(2) <=> C6H11O(235) + H2O2(4)""",
)

entry(
    index = 146,
    label = "C5H8O2(236) + HO2(2) <=> C5H7O2(237) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (5.29618e-10, 'cm^3/(mol*s)'),
        n = 5.83949,
        Ea = (12.045, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.76227, dn = +|- 0.133348, dEa = +|- 0.733546 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O2(236) + HO2(2) <=> C5H7O2(237) + H2O2(4)""",
)

entry(
    index = 147,
    label = "C2H4O(238) + HO2(2) <=> C2H3O(239) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.131477, 'cm^3/(mol*s)'),
        n = 3.83204,
        Ea = (82.1128, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.05819, dn = +|- 0.00742338, dEa = +|- 0.040836 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C2H4O(238) + HO2(2) <=> C2H3O(239) + H2O2(4)""",
)

entry(
    index = 148,
    label = "C3H4O2(240) + HO2(2) <=> C3H3O2(241) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.03096e-05, 'cm^3/(mol*s)'),
        n = 4.7819,
        Ea = (1.76206, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.52563, dn = +|- 0.0554372, dEa = +|- 0.30496 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H4O2(240) + HO2(2) <=> C3H3O2(241) + H2O2(4)""",
)

entry(
    index = 149,
    label = "C6H14(197) + HO2(2) <=> H2O2(4) + C6H13(242)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000218317, 'cm^3/(mol*s)'),
        n = 4.46437,
        Ea = (58.8852, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.28909, dn = +|- 0.033327, dEa = +|- 0.183332 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H14(197) + HO2(2) <=> H2O2(4) + C6H13(242)""",
)

entry(
    index = 150,
    label = "C7H14(153) + HO2(2) <=> C7H13(243) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.26892e-07, 'cm^3/(mol*s)'),
        n = 5.28799,
        Ea = (63.0482, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.14314, dn = +|- 0.100041, dEa = +|- 0.550328 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(153) + HO2(2) <=> C7H13(243) + H2O2(4)""",
)

entry(
    index = 151,
    label = "C4H8O(244) + HO2(2) <=> C4H7O(245) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (7.57284e-06, 'cm^3/(mol*s)'),
        n = 4.76828,
        Ea = (36.2339, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.50424, dn = +|- 0.0535844, dEa = +|- 0.294768 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(244) + HO2(2) <=> C4H7O(245) + H2O2(4)""",
)

entry(
    index = 152,
    label = "C5H12(182) + HO2(2) <=> H2O2(4) + C5H11(246)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000307602, 'cm^3/(mol*s)'),
        n = 4.59424,
        Ea = (57.841, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.32304, dn = +|- 0.0367389, dEa = +|- 0.202101 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H12(182) + HO2(2) <=> H2O2(4) + C5H11(246)""",
)

entry(
    index = 153,
    label = "C7H12(247) + HO2(2) <=> H2O2(4) + C7H11(248)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.16788e-07, 'cm^3/(mol*s)'),
        n = 5.27195,
        Ea = (24.6276, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.09691, dn = +|- 0.0971796, dEa = +|- 0.534585 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H12(247) + HO2(2) <=> H2O2(4) + C7H11(248)""",
)

entry(
    index = 154,
    label = "C5H8O(249) + HO2(2) <=> H2O2(4) + C5H7O(250)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.393e-08, 'cm^3/(mol*s)'),
        n = 5.74753,
        Ea = (28.6265, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.91819, dn = +|- 0.140554, dEa = +|- 0.773191 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(249) + HO2(2) <=> H2O2(4) + C5H7O(250)""",
)

entry(
    index = 155,
    label = "C7H8(251) + HO2(2) <=> H2O2(4) + C7H7(252)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.6588e-09, 'cm^3/(mol*s)'),
        n = 6.18418,
        Ea = (28.6153, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.97747, dn = +|- 0.0894823, dEa = +|- 0.492243 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H8(251) + HO2(2) <=> H2O2(4) + C7H7(252)""",
)

entry(
    index = 156,
    label = "C5H10(149) + HO2(2) <=> H2O2(4) + C5H9(253)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000834696, 'cm^3/(mol*s)'),
        n = 4.27525,
        Ea = (57.49, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.18499, dn = +|- 0.0222764, dEa = +|- 0.122542 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10(149) + HO2(2) <=> H2O2(4) + C5H9(253)""",
)

entry(
    index = 157,
    label = "C4H6O(79) + HO2(2) <=> H2O2(4) + C4H5O(254)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.07977e-10, 'cm^3/(mol*s)'),
        n = 6.18894,
        Ea = (24.1903, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 3.55647, dn = +|- 0.166515, dEa = +|- 0.915997 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H6O(79) + HO2(2) <=> H2O2(4) + C4H5O(254)""",
)

entry(
    index = 158,
    label = "C6H12O(172) + HO2(2) <=> C6H11O(255) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.95109e-05, 'cm^3/(mol*s)'),
        n = 4.49369,
        Ea = (51.038, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.33762, dn = +|- 0.0381765, dEa = +|- 0.210009 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(172) + HO2(2) <=> C6H11O(255) + H2O2(4)""",
)

entry(
    index = 159,
    label = "C6H12(122) + HO2(2) <=> H2O2(4) + C6H11(256)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000430665, 'cm^3/(mol*s)'),
        n = 4.42366,
        Ea = (60.3346, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.27693, dn = +|- 0.032083, dEa = +|- 0.176488 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12(122) + HO2(2) <=> H2O2(4) + C6H11(256)""",
)

entry(
    index = 160,
    label = "C5H10O(211) + HO2(2) <=> H2O2(4) + C5H9O(257)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000228484, 'cm^3/(mol*s)'),
        n = 4.88886,
        Ea = (56.047, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.06954, dn = +|- 0.00882341, dEa = +|- 0.0485376 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(211) + HO2(2) <=> H2O2(4) + C5H9O(257)""",
)

entry(
    index = 161,
    label = "C6H12O(159) + HO2(2) <=> H2O2(4) + C6H11O(258)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000547843, 'cm^3/(mol*s)'),
        n = 4.54687,
        Ea = (60.3244, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.31524, dn = +|- 0.0359628, dEa = +|- 0.197832 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12O(159) + HO2(2) <=> H2O2(4) + C6H11O(258)""",
)

entry(
    index = 162,
    label = "C4H8O(189) + HO2(2) <=> H2O2(4) + C4H7O(259)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.37166e-09, 'cm^3/(mol*s)'),
        n = 5.75426,
        Ea = (31.1394, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.74682, dn = +|- 0.132612, dEa = +|- 0.729496 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C4H8O(189) + HO2(2) <=> H2O2(4) + C4H7O(259)""",
)

entry(
    index = 163,
    label = "C6H12(122) + HO2(2) <=> C6H11(260) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (6.89092e-08, 'cm^3/(mol*s)'),
        n = 5.51764,
        Ea = (22.004, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.53103, dn = +|- 0.121874, dEa = +|- 0.670428 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12(122) + HO2(2) <=> C6H11(260) + H2O2(4)""",
)

entry(
    index = 164,
    label = "C6H10O(261) + HO2(2) <=> H2O2(4) + C6H9O(262)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (2.8487e-06, 'cm^3/(mol*s)'),
        n = 4.92965,
        Ea = (44.8359, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.63671, dn = +|- 0.0646606, dEa = +|- 0.355698 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H10O(261) + HO2(2) <=> H2O2(4) + C6H9O(262)""",
)

entry(
    index = 165,
    label = "C5H10O(180) + HO2(2) <=> C5H9O(263) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000794784, 'cm^3/(mol*s)'),
        n = 4.26562,
        Ea = (43.7449, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.19017, dn = +|- 0.0228487, dEa = +|- 0.125691 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(180) + HO2(2) <=> C5H9O(263) + H2O2(4)""",
)

entry(
    index = 166,
    label = "C5H10(149) + HO2(2) <=> H2O2(4) + C5H9(264)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.39024e-08, 'cm^3/(mol*s)'),
        n = 5.5877,
        Ea = (23.9257, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.51546, dn = +|- 0.121064, dEa = +|- 0.665975 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10(149) + HO2(2) <=> H2O2(4) + C5H9(264)""",
)

entry(
    index = 167,
    label = "C5H8O(136) + HO2(2) <=> C5H7O(265) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (9.00839e-09, 'cm^3/(mol*s)'),
        n = 5.77243,
        Ea = (22.7581, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.87101, dn = +|- 0.138415, dEa = +|- 0.761423 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H8O(136) + HO2(2) <=> C5H7O(265) + H2O2(4)""",
)

entry(
    index = 168,
    label = "C3H2O4(192) + HO2(2) <=> C3HO4(266) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (1.08431e-09, 'cm^3/(mol*s)'),
        n = 6.34606,
        Ea = (22.493, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 2.07454, dn = +|- 0.0957718, dEa = +|- 0.526841 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H2O4(192) + HO2(2) <=> C3HO4(266) + H2O2(4)""",
)

entry(
    index = 169,
    label = "C7H14(153) + HO2(2) <=> C7H13(267) + H2O2(4)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.000756205, 'cm^3/(mol*s)'),
        n = 4.41946,
        Ea = (43.3456, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.34256, dn = +|- 0.0386605, dEa = +|- 0.212672 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C7H14(153) + HO2(2) <=> C7H13(267) + H2O2(4)""",
)

entry(
    index = 170,
    label = "C5H10O(180) + HO2(2) <=> H2O2(4) + C5H9O(268)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (0.00162435, 'cm^3/(mol*s)'),
        n = 4.22072,
        Ea = (52.4572, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.15855, dn = +|- 0.0193142, dEa = +|- 0.106247 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C5H10O(180) + HO2(2) <=> H2O2(4) + C5H9O(268)""",
)

entry(
    index = 171,
    label = "C6H12(269) + HO2(2) <=> H2O2(4) + C6H11(270)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (3.91043e-06, 'cm^3/(mol*s)'),
        n = 5.21824,
        Ea = (61.0254, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.96367, dn = +|- 0.0885635, dEa = +|- 0.487188 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C6H12(269) + HO2(2) <=> H2O2(4) + C6H11(270)""",
)

entry(
    index = 172,
    label = "C3H6O2(271) + HO2(2) <=> H2O2(4) + C3H5O2(272)",
    degeneracy = 1,
    kinetics = Arrhenius(
        A = (8.3672e-09, 'cm^3/(mol*s)'),
        n = 6.07812,
        Ea = (55.5281, 'kJ/mol'),
        T0 = (1, 'K'),
        Tmin = (303.03, 'K'),
        Tmax = (2500, 'K'),
        comment = 'Fitted to 59 data points; dA = *|/ 1.78093, dn = +|- 0.0757438, dEa = +|- 0.416667 kJ/mol',
    ),
    shortDesc = u"""AutoTST M062X for C3H6O2(271) + HO2(2) <=> H2O2(4) + C3H5O2(272)""",
)

