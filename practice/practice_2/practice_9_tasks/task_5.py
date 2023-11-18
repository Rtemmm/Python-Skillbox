from collections import Counter

with open('text.txt', 'r') as f:
    text = f.read().lower()

letter_freq = Counter(c for c in text if c.isalpha())

total_letters = sum(letter_freq.values())

letter_freq = {k: v / total_letters for k, v in letter_freq.items()}

sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))

with open('analysis.txt', 'w') as f:
    for letter, freq in sorted_letters:
        f.write(f'{letter} {freq:.3f}\n')
