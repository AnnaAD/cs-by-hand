#!/usr/bin/env python3
"""
Reads q1-template.tex, randomly fills in the D column of the truth table,
builds the correct SOP expression from that table, generates 4 incorrect SOPs,
shuffles them, and writes q1.tex.
"""

import random
import re
import itertools

TEMPLATE_FILE = "lec2/q1-template.tex"
OUTPUT_FILE = "outputs/lec2/q1.tex"

INPUTS = [
    (0,0,0),
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1),
]

def minterm(a, b, c):
    """Return LaTeX string for a single minterm."""
    def lit(var, val):
        return var if val == 1 else f"\\bar{{{var}}}"

    return lit("A", a) + lit("B", b) + lit("C", c)

def sop_from_truth(truth):
    """
    Given a dict {(a,b,c): d}, return SOP LaTeX string.
    """
    terms = []
    for (a,b,c), d in truth.items():
        if d == 1:
            terms.append(minterm(a,b,c))
    if not terms:
        return "0"
    return " + ".join(terms)

def random_wrong_sop(correct_terms, all_terms):
    """
    Generate a wrong SOP by randomly selecting a different subset of minterms.
    """
    while True:
        k = random.randint(1, len(all_terms))
        chosen = set(random.sample(all_terms, k))
        if chosen != correct_terms:
            return " + ".join(chosen)

def main():
    with open(TEMPLATE_FILE, "r") as f:
        template = f.read()

    truth = {}
    for abc in INPUTS:
        truth[abc] = random.randint(0, 1)

    correct_sop = sop_from_truth(truth)

    if correct_sop == "0":
        correct_terms = set()
    else:
        correct_terms = set(correct_sop.split(" + "))

    all_terms = [minterm(a,b,c) for (a,b,c) in INPUTS]

    wrong_sops = []
    for _ in range(4):
        wrong_sops.append(random_wrong_sop(correct_terms, all_terms))

    choices = wrong_sops + [correct_sop]
    random.shuffle(choices)

    def replace_d_column(tex):
        lines = tex.splitlines()
        out = []
        i = 0
        for line in lines:
            if re.search(r"\$\d\$\s*&\s*\$\d\$\s*&\s*\$\d\$\s*&", line):
                a,b,c = INPUTS[i]
                d = truth[(a,b,c)]
                new_line = re.sub(r"&\s*\\\\", f"& ${d}$ \\\\\\\\", line)
                print(new_line)
                out.append(new_line)
                i += 1
            else:
                out.append(line)
        return "\n".join(out)

    tex = replace_d_column(template)
    print(tex)

    new_block = ["\\begin{checkboxes}"]

    for sop in choices:
        if sop == correct_sop:
            new_block.append(f"\\CorrectChoice ${sop}$")
        else:
            new_block.append(f"\\choice ${sop}$")

    new_block.append("\\choice None of the above")
    new_block.append("\\end{checkboxes}")

    print("\n".join(new_block))
    tex += ("\n".join(new_block))

    with open(OUTPUT_FILE, "w") as f:
        f.write(tex)

if __name__ == "__main__":
    main()
