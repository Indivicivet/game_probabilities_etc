import itertools
from collections import Counter

sets = "FIVE FOUR HIGHSTRAIGHT FULLHOUSE LOWSTRAIGHT THREE TWOPAIR PAIR NAILS".split()

exec(",".join(reversed(sets))+",*_ = range(999)")

def valuation(ds):
    if sorted(ds) == list(range(10, 15)):
        return HIGHSTRAIGHT
    if sorted(ds) == list(range(9, 14)):
        return LOWSTRAIGHT
    vals = sorted(Counter(ds).values())
    if vals == [5]:
        return FIVE
    if vals == [1, 4]:
        return FOUR
    if vals == [2, 3]:
        return FULLHOUSE
    if vals == [1, 1, 3]:
        return THREE
    if vals == [1, 2, 2]:
        return TWOPAIR
    if vals == [1, 1, 1, 2]:
        return PAIR
    return NAILS


rolls = Counter(valuation(ds) for ds in itertools.product(range(9, 15), repeat=5))
cumulative = {i: sum(v for j, v in rolls.items() if j >= i) for i in rolls}
total_rolls = sum(rolls.values())

print("chance of EXACTLY:")
for s in sets:
    print(f"{s: <13} {100 * rolls[eval(s)] / total_rolls:.2f}%")
print()
print("chance of AT LEAST:")
for s in sets:
    print(f"{s: <13} {100 * cumulative[eval(s)] / total_rolls:.2f}%")
