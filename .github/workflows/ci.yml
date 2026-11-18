#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Réduction et Factorisation Spatiale des Polynômes par Macro-Blocs Combinatoires
Auteur : Mohamed Ghali (2026)
"""

import math


def calculer_macro_blocs(couples_ba: list) -> dict:
    n = len(couples_ba)
    k = n // 2
    blocs = list()

    for j in range(k):
        b1, a1 = couples_ba[2 * j]
        b2, a2 = couples_ba[2 * j + 1]
        S_j = (b1 / a1) + (b2 / a2)
        P_j = (b1 * b2) / (a1 * a2)
        blocs.append({"S": S_j, "P": P_j, "valeur_bloc": 1 + S_j + P_j})

    residu = None
    if n % 2 == 1:
        b_last, a_last = couples_ba[-1]
        residu = 1 + (b_last / a_last)

    produit_direct = math.prod(1 + (b / a) for b, a in couples_ba)
    produit_blocs = math.prod(bloc["valeur_bloc"] for bloc in blocs)
    if residu is not None:
        produit_blocs *= residu

    return {
        "degre_n": n,
        "nb_macro_blocs_k": k,
        "blocs": blocs,
        "residu_impair": residu,
        "produit_direct": produit_direct,
        "produit_macro_blocs": produit_blocs,
    }


def degonfler_polynome(coeffs_desc: list, facteur_a_n: complex) -> list:
    n = len(coeffs_desc) - 1
    if n < 1:
        raise ValueError("Le polynôme doit être de degré >= 1.")
    sous_coeffs = list((coeffs_desc[0],))
    for idx in range(1, n):
        val = coeffs_desc[idx] - facteur_a_n * sous_coeffs[-1]
        sous_coeffs.append(val)
    return sous_coeffs


def simuler_cascade_optique(reflexions_r: list) -> dict:
    n = len(reflexions_r)
    k = n // 2
    matrices_blocs = list()

    for j in range(k):
        r1 = reflexions_r[2 * j]
        r2 = reflexions_r[2 * j + 1]
        S_j = 1j * (r1 + r2)
        P_j = -(r1 * r2)
        matrices_blocs.append({"S_j": S_j, "P_j": P_j, "transfert": 1 + S_j + P_j})

    amp_directe = 1.0 + 0.0j
    for r in reflexions_r:
        amp_directe *= (1 + 1j * r)

    amp_blocs = 1.0 + 0.0j
    for bloc in matrices_blocs:
        amp_blocs *= bloc["transfert"]
    if n % 2 == 1:
        amp_blocs *= (1 + 1j * reflexions_r[-1])

    return {
        "nb_couches": n,
        "amplitude_directe": amp_directe,
        "amplitude_macro_blocs": amp_blocs,
        "ecart_numerique": abs(amp_directe - amp_blocs),
    }


if __name__ == "__main__":
    print("=" * 72)
    print("THÉORÈME DE RÉDUCTION PAR MACRO-BLOCS COMBINATOIRES — DÉMONSTRATION")
    print("=" * 72)

    couples_5 = list(((2.0, 1.0), (3.0, 2.0), (5.0, 4.0), (7.0, 3.0), (11.0, 5.0)))
    res_5 = calculer_macro_blocs(couples_5)
    print(f"1. Cas impair (n=5) : Direct = {res_5['produit_direct']:.6f} | "
          f"Macro-Blocs = {res_5['produit_macro_blocs']:.6f}")

    optique_6 = simuler_cascade_optique(list((0.1, 0.2, 0.15, 0.25, 0.1, 0.3)))
    print(f"2. Optique complexe (n=6) : Écart numérique = {optique_6['ecart_numerique']:.2e}")
