from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    # A cannot be both Knight and knave. It is either one or the other.
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    # If A is knight, he is true
    Implication(AKnight,And(AKnight,AKnave)),
    # If A is knave, he is false
    Implication(AKnave,Not(And(AKnight,AKnave)))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    # A cannot be both Knight and knave. It is either one or the other.
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    # B cannot be both Knight and knave. It is either one or the other.
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    # A says both are A and B are knaves
        # it is true if A is knight
    Implication(AKnight,And(AKnave,BKnave)),
        # it is false if A is knave
    Implication(AKnave,Not(And(AKnave,BKnave)))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    # A cannot be both Knight and knave. It is either one or the other.
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    # B cannot be both Knight and knave. It is either one or the other.
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    # A says both are of same kinds
        # True if A is knight
    Implication(AKnight,Or(And(AKnight,BKnight),And(AKnave,BKnave))),
        # False if A is knave
    Implication(AKnave,Not(Or(And(AKnight,BKnight),And(AKnave,BKnave)))),
    # B says they are of different kinds
        # True if B is knight
    Implication(BKnight,Or(And(AKnight,BKnave),And(AKnave,BKnight))),
        # False if B is knave
    Implication(BKnave,Not(Or(And(AKnight,BKnave),And(AKnave,BKnave))))
    
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # A cannot be both Knight and knave. It is either one or the other.
    And(Or(AKnight,AKnave),Not(And(AKnight,AKnave))),
    # B cannot be both Knight and knave. It is either one or the other.
    And(Or(BKnight,BKnave),Not(And(BKnight,BKnave))),
    # C cannot be both Knight and knave. It is either one or the other.
    And(Or(CKnight,CKnave),Not(And(CKnight,CKnave))),

    # For B if is knight
    # B says "C is a knave."
    Implication(BKnight,CKnave),
    # B says "A said 'I am a knave'."
    Implication(BKnight,And(
                Implication(AKnight,AKnave),
                Implication(AKnave,Not(AKnave))
                )),

    # For If B is knave
    # B says "C is a knave."
    Implication(BKnave,Not(CKnave)),
    # B says "A said 'I am a knave'."
    Implication(BKnave,Not(And(
        Implication(AKnight,AKnave),
        Implication(AKnave,Not(AKnave))
    ))),

    # For C says "A is a knight."
    Implication(CKnight,AKnight),
    Implication(CKnave,Not(AKnight))

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
