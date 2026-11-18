import Mathlib.Tactic.Ring
import Mathlib.Data.Real.Basic

theorem macro_block_pair_identity (a1 b1 a2 b2 x : Real) (ha1 : a1 ≠ 0) (ha2 : a2 ≠ 0) :
    let S := b1 / a1 + b2 / a2
    let P := (b1 * b2) / (a1 * a2)
    (1 + (b1 / a1) * x) * (1 + (b2 / a2) * x) = 1 + S * x + P * x ^ 2 := by
  intro S P
  dsimp only [S, P]
  field_simp
  ring

theorem proportionality_law_AD_BC (A r5 M : Real) :
    let B := r5 * A
    let C := M * A
    let D := r5 * M * A
    A * D = B * C := by
  intro B C D
  dsimp only [B, C, D]
  ring

theorem proportionality_law_AF_BE (A r5 M1 M2 : Real) :
    let B := r5 * A
    let E := M1 * M2 * A
    let F := M1 * M2 * r5 * A
    A * F = B * E := by
  intro B E F
  dsimp only [B, E, F]
  ring
