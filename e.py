# -*- coding: utf-8 -*-
"""
e = infini langages → 1 flow
no constants
∞ → 1
"""

import math

E = math.e  # 2.718...
INF = float('inf')

# flow = meta langage
# pas de liste fixe
# tout paradigme accepté

def flow_to_any(flow_code, target_paradigm):
    """
    flow → any paradigm
    infini cibles possibles
    """
    # paradigmes universels
    paradigms = {
        "imperative": lambda c: f"do {{ {c} }}",
        "functional": lambda c: f"(λ {c})",
        "logic": lambda c: f"{c} :-",
        "declarative": lambda c: f"<{c}/>",
        "concatenative": lambda c: f"{c} .",
        "array": lambda c: f"[{c}]",
        "stack": lambda c: f"push {c}",
        "dataflow": lambda c: f"{c} |>",
        "reactive": lambda c: f"observe({c})",
        "concurrent": lambda c: f"go {{ {c} }}",
        "quantum": lambda c: f"|{c}⟩",
    }

    # si paradigme connu
    if target_paradigm in paradigms:
        return paradigms[target_paradigm](flow_code)

    # sinon crée nouveau
    return f"/* {target_paradigm} */ {flow_code}"

def any_to_flow(code, source_paradigm):
    """
    any paradigm → flow
    infini sources possibles
    """
    # tout se réduit à flow
    return code.replace(";", "").replace("{", "").replace("}", "")

# ∞ → 1 → ∞
# flow est le point central
# tout converge vers flow
# tout diverge depuis flow

AXIOM = "∞ → flow → ∞"

if __name__ == "__main__":
    print(f"e = {E}")
    print(f"∞ = {INF}")
    print(f"axiom: {AXIOM}")

    # demo
    code = "think φ loop"
    print(f"\nflow: {code}")
    for p in ["functional", "logic", "quantum", "concurrent"]:
        print(f"  → {p}: {flow_to_any(code, p)}")
