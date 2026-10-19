#!/usr/bin/env python3
"""Print review-file questions for a redo session with the option letters SHUFFLED,
so remembering the old letter doesn't help. Saves the answer key for grading.

Usage:
  python3 aws-sap/redo_shuffle.py <review.md> <q1,q2,...> <seed> [--key /tmp/redo_key.json]
  python3 aws-sap/redo_shuffle.py --grade "1:B 2:AC ..." [--key /tmp/redo_key.json]
"""
import json
import random
import re
import sys

KEY_DEFAULT = "/tmp/redo_key.json"


def show(review, qs, seed, key_path):
    random.seed(seed)
    text = open(review, encoding="utf-8").read()
    key = {}
    for n, q in enumerate(qs, 1):
        m = re.search(rf"^## Q{q}\n(.*?)<details>(.*?)</details>", text, re.S | re.M)
        if not m:
            sys.exit(f"Q{q} not found in {review}")
        body, ans = m.group(1), m.group(2)
        opts = re.findall(r"^- \*\*([A-G])\.\*\* (.*)$", body, re.M)
        stem = body[:body.index("- **A.**")].strip()
        # "**Correct:** A, C · …" (wrong mode) or "**Correct:** A (you answered correctly)" (right mode)
        cm = re.search(r"\*\*Correct:\*\*([^·(]*)", ans)
        if not cm:
            sys.exit(f"Q{q}: no '**Correct:**' line in {review}")
        correct = set(re.findall(r"[A-G]", cm.group(1)))
        order = opts[:]
        random.shuffle(order)
        letters = "ABCDEFG"
        key[str(n)] = {"q": q, "correct": "".join(sorted(letters[i] for i, (o, _) in enumerate(order) if o in correct))}
        print(f"**R{n}.** {stem}")
        for i, (_, txt) in enumerate(order):
            print(f"- **{letters[i]}.** {txt}")
        print()
    json.dump(key, open(key_path, "w"))


def grade(answers, key_path):
    """answers: '1:B 2:AC' → prints per-question result and the score."""
    key = json.load(open(key_path))
    given = dict(a.split(":") for a in answers.split())
    ok = 0
    for n, v in key.items():
        mine = "".join(sorted(given.get(n, "").upper()))
        hit = mine == v["correct"]
        ok += hit
        print(f"R{n} Q{v['q']}: you {mine or '-'} · correct {v['correct']} · {'OK' if hit else 'MISS'}")
    print(f"score {ok}/{len(key)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    key_path = args[args.index("--key") + 1] if "--key" in args else KEY_DEFAULT
    if args[0] == "--grade":
        grade(args[1], key_path)
    else:
        show(args[0], args[1].split(","), int(args[2]), key_path)
