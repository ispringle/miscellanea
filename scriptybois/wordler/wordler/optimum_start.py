from collections import Counter


wp = "words.txt"
letter_count = Counter([char for x in
                        [x.strip().lower() for x in [*open(wp)]
                         if len(x.strip()) == 5]
                        for char in x])
print(letter_count.most_common(5))
