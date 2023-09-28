#Job 3.8

import re
import matplotlib.pyplot as plt

def next_letter_occurrences(text):
    next_letter_counts = {}
    words = re.findall(r'\b\w+\b', text, re.IGNORECASE)  
    
    for word in words:
        word = word.lower()  
        for i in range(len(word) - 1):
            letter1 = word[i]
            letter2 = word[i + 1]
            if letter1.isalpha() and letter2.isalpha():
                if letter1 in next_letter_counts:
                    next_letter_counts[letter1][letter2] = next_letter_counts[letter1].get(letter2, 0) + 1
                else:
                    next_letter_counts[letter1] = {letter2: 1}
    
    return next_letter_counts

file_name= r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"

with open(file_name, "r") as file:
    content = file.read()
    next_letter_counts = next_letter_occurrences(content)

    total_next_letters = sum([sum(counts.values()) for counts in next_letter_counts.values()])

    letters = sorted(set(next_letter_counts.keys()))
    labels = [f'{letter}:' for letter in letters]
    
    # Create superimposed curves for each letter
    plt.figure(figsize=(14, 7))
    for letter in letters:
        percentages = [(count / total_next_letters) * 100 for count in next_letter_counts[letter].values()]
        plt.plot(list(next_letter_counts[letter].keys()), percentages, marker='o', label=f'{letter}:')
    plt.xlabel("The next Letter")
    plt.ylabel("Percentage ")
    plt.title("Percentage of appearance of each  following letter")
    plt.legend(labels)
    plt.grid(True)
    plt.show()
