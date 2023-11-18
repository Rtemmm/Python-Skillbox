from collections import Counter

with open('voina-i-mir.txt', 'r', encoding='utf-8') as file:
    text = file.read()

letter_counts = Counter(c for c in text if c.isalpha())
sorted_letters = sorted(letter_counts.items(), key=lambda x: x[1], reverse=True)

for letter, count in sorted_letters:
    print(f"{letter}: {count}")
