#Job 3.9
import random

lengths_frequencies = {3: 10, 4: 20, 5: 15}
first_letter_frequencies = {'a': 0.3, 'b': 0.2, 'c': 0.1}
word_frequencies = {'th': 0.2, 'ing': 0.1, 'at': 0.05}

def generate_word():
    # Generate word length 
    word_length = random.choices(list(lengths_frequencies.keys()), list(lengths_frequencies.values()))[0]

    # Generate the first letter 
    first_letter = random.choices(list(first_letter_frequencies.keys()), list(first_letter_frequencies.values()))[0]

    # Generate the rest of the word 
    length_remain = word_length - 1
    word = first_letter

    while length_remain > 0:
        sq = random.choices(list(word_frequencies.keys()), list(word_frequencies.values()))[0]
        word += sq
        length_remain -= len(sq)

    return word

# Generate and print a random word
word = generate_word()
print("Random Word:", word)
