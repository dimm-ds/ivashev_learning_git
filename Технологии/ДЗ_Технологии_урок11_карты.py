import itertools

suits = ["♠", "♥", "♦", "♣"]
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [e[0] + e[1] for e in itertools.product(ranks, suits)]
variants = {}
for r in range(2, 7):
    for var in itertools.combinations(deck, r):
        variants.setdefault(r, set()).add(var)


