#Job 3.6
import re
import matplotlib.pyplot as plt

# Function to count words of each size in text
def count_words_by_size(text):
    word_sizes = {}
    words = re.findall(r'\b\w+\b', text)
    
    for word in words:
        size = len(word)
        if size in word_sizes:
            word_sizes[size] += 1
        else:
            word_sizes[size] = 1
    
    return word_sizes

# Name of the file to read
file_name= r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"


with open(file_name, "r") as file:
    content = file.read()
    word_sizes = count_words_by_size(content)
    total_words = sum(word_sizes.values())
    word_size_percentages = {size: (count / total_words) * 100 for size, count in word_sizes.items()}
    sizes = sorted(word_size_percentages.keys())
    size_percentages = [word_size_percentages[size] for size in sizes]
    
    # Create a bar chart using Matplotlib
    plt.figure(figsize=(12, 6))
    plt.bar(sizes, size_percentages)
    plt.xlabel("Word Size")
    plt.ylabel("Percentage of Appearance")
    plt.title("Percentage of Appearance of Each Word Size")
    plt.show()

