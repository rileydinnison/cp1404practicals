"""
Word Occurrences
Estimate: 40 minutes
Actual:    minutes
"""


text = input('Text: ')
word_to_count = {}
words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

sorted_words = sorted(word_to_count.keys())

max_length = max(len(word) for word in sorted_words)

for word in sorted_words:
    print(f"{word:{max_length}} : {word_to_count[word]}")
