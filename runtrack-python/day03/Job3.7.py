#Job 3.7
import re
import matplotlib.pyplot as plt


def count_occurrences(text):
    counts = {}
    words = re.findall(r'\b\w+\b', text, re.IGNORECASE)  
    
    for word in words:
        first_letter = word[0].lower()  
        if first_letter.isalpha():
            if first_letter in counts:
                counts[first_letter] += 1
            else:
                counts[first_letter] = 1
    
    return counts  

file_name = r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"

with open(file_name, "r") as file:
    content = file.read()
    counts = count_occurrences(content)

    total_words = sum(counts.values())

    char_percentages = {letter: (count / total_words) * 100 for letter, count in counts.items()}
    
    letters = sorted(char_percentages.keys())
    
    percentages = [char_percentages[letter] for letter in letters]

    plt.figure(figsize=(12, 6))
    plt.bar(letters, percentages)
    plt.xlabel("Letter")
    plt.ylabel("Percentage of presence")
    plt.title("Percentage of each letter")
    plt.show()
