import MilleniumProblems.Basic
import Lake
open Lake Target

package MilleniumProblems where
  -- Impostazioni del pacchetto

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

@[default_target]
lean_lib MilleniumProblems where
  -- Impostazioni della libreria