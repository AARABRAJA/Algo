#Job 3.5
import matplotlib.pyplot as plt

# Function to count occurrences in text
def count_occurences(text):
    text = text.lower()  
    letter_counts = {}
    for letter in text:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

# Name of the file to read
file_name= r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"


with open(file_name, "r") as file:
    content = file.read()
    letter_counts = count_occurences(content)

    # Nbr total des lettres
    total_letters = sum(letter_counts.values()) # Afin d'afficher tt les valeurs

    # Calculate the percentage of appearance for each letter
    letter_percentages = {letter: (count / total_letters) * 100 for letter, count in letter_counts.items()}
    
    # Create an ordered list of letters for plotting
    letters = sorted(letter_percentages.keys()) #.keys: pour acceder aux lettres
    #sorted:pour mettre en ordre les clèfs: les lettres dans ce cas

    # Extract corresponding percentages in the same order
    percentages = [letter_percentages[letter] for letter in letters]

    # Create a bar chart using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.bar(letters, percentages)
    plt.xlabel("Letter")
    plt.ylabel("Percentage of Appearance")
    plt.title("Percentage of Appearance of Each Letter")
    plt.show()
