import math
from macro_blocks import (
    calculer_macro_blocs,
    reduction_hierarchique_cascade,
    degonfler_polynome,
    simuler_cascade_optique,
)


def test_cas_pair_et_impair():
    couples_4 = list(((1.0, 2.0), (3.0, 4.0), (5.0, 6.0), (7.0, 8.0)))
    res_4 = calculer_macro_blocs(couples_4)
    assert res_4["residu_impair"] is None
    assert math.isclose(res_4["produit_direct"], res_4["produit_macro_blocs"], rel_tol=1e-12)

    couples_5 = list(((1.0, 2.0), (3.0, 4.0), (5.0, 6.0), (7.0, 8.0), (9.0, 10.0)))
    res_5 = calculer_macro_blocs(couples_5)
    assert res_5["residu_impair"] is not None
    assert math.isclose(res_5["produit_direct"], res_5["produit_macro_blocs"], rel_tol=1e-12)


def test_reduction_hierarchique_manuscrit():
    couples_5 = list(((2.0, 1.0), (3.0, 2.0), (5.0, 4.0), (7.0, 3.0), (11.0, 5.0)))
    res_direct = calculer_macro_blocs(couples_5)["produit_direct"]
    cascade = reduction_hierarchique_cascade(couples_5)
    assert cascade["nb_etapes_reduction"] == 3
    assert math.isclose(res_direct, cascade["valeur_finale"], rel_tol=1e-12)


def test_lois_proportionnalite_degre_5():
    S1, P1 = 1.5, 0.5
    S2, P2 = 2.2, 1.1
    ratio_5 = 0.75
    A = 1.0
    B = ratio_5 * A
    C = (S1 + P1) * A
    D = ratio_5 * (S1 + P1) * A
    E = (S1 + P1) * (S2 + P2) * A
    F = (S1 + P1) * (S2 + P2) * ratio_5 * A

    assert math.isclose(A * D, B * C, rel_tol=1e-12)
    assert math.isclose(A * F, B * E, rel_tol=1e-12)


def test_degonflage_et_optique():
    sous = degonfler_polynome(list((2, 7, 10, 8)), 2)
    assert sous == list((2, 3, 4))

    res_opt = simuler_cascade_optique(list((0.12, 0.08, 0.15, 0.05, 0.1, 0.2)))
    assert res_opt["ecart_numerique"] < 1e-14
