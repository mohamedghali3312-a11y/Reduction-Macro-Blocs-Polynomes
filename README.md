# Réduction et Factorisation Spatiale des Polynômes par Macro-Blocs Combinatoires

**Statut :** `CI : PASSING` | **DOI :** `10.5281/zenodo.24339295` | **Preuves Formelles :** `Lean 4 (Mathlib)` | **Licence :** `MIT (2026)`

**Auteur :** Mohamed Ghali (Novembre 2026)  
**Domaine :** Algèbre polynomiale, factorisation spatiale par macro-blocs combinatoires, dégonflage linéaire et propagation d'ondes en optique complexe.

---

## 1. Vue d'ensemble / Overview

Ce dépôt présente la **Théorie de la Réduction et Factorisation Spatiale des Polynômes par Macro-Blocs Combinatoires** (*Combinatorial Macro-Block Reduction and Spatial Factorization of Polynomials*) :

* **Regroupement par Macro-Blocs Quadratiques :** Factorisation des produits linéaires \(\prod_{i=1}^n (1 + \frac{b_i}{a_i} x)\) en \(k = \lfloor n/2 \rfloor\) macro-blocs \((1 + S_j x + P_j x^2)\) pour le **cas pair (n = 2k)**, avec isolation d'un maillon résiduel \((1 + \frac{b_{2k+1}}{a_{2k+1}} x)\) pour le **cas impair (n = 2k+1)**.
* **Effondrement hiérarchique en cascade :** Réduction récursive d'ordre \(n \to \lceil n/2 \rceil \to \dots \to 1\) conservant exactement la valeur globale du polynôme.
* **Lois géométriques invariantes :** Démonstration des relations de proportionnalité croisée A ⋅ D = B ⋅ C et A ⋅ F = B ⋅ E.
* **Application Optique & Ondes :** Réduction de la complexité des interférences multicouches complexes \(\prod (1 + i r_m)\) de \(2^n\) chemins à un produit de k transferts quadratiques stables.

**Publication principale :** [Télécharger l'article complet (PDF)](article_mbc_annealing_v2_hal_en.pdf)

---

## 2. Citation académique officielle

> Ghali, M. (2026). *Combinatorial Macro-Block Reduction of Polynomials (v1.0.0 — Certified Release)*. Zenodo. `DOI: 10.5281/zenodo.24339295`

---

## 3. Structure du dépôt

```text
Reduction-Macro-Blocs-Polynomes/
├── .github/workflows/ci.yml           # Pipeline CI automatique (Python + Lean 4)
├── article_mbc_annealing_v2_hal_en.pdf # Article scientifique complet (EN)
├── macro_blocks.py                     # Moteur Python (macro-blocs, cascade, optique)
├── test_macro_blocks.py                # Suite de tests unitaires (pytest)
├── proofs_macro_blocks.lean            # Preuves formelles certifiées sous Lean 4
├── lakefile.toml                       # Configuration Lean 4 / Mathlib
├── lake-manifest.json                  # Verrouillage des dépendances Lean 4
├── lean-toolchain                      # Version du compilateur Lean (v4.12.0)
└── LICENSE                             # Licence MIT (Mohamed Ghali, 2026)
```

---

## 4. Vérification et exécution

```bash
# Exécution des tests unitaires et de la démonstration Python
pip install pytest
pytest -v
python macro_blocks.py

# Compilation et vérification formelle sous Lean 4
lake update
lake exe cache get
lake build
```
