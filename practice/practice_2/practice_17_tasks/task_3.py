from collections import Counter


def can_be_poly(s: str) -> bool:
    counter = Counter(s)
    odd_counts = sum(1 for count in counter.values() if count % 2 == 1)
    return odd_counts <= 1


print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
