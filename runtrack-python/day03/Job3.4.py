#Job 3.4
import re

# Function to count words of a specific length
def count_words(text, length):
    words = re.findall(r'\b\w+\b', text)
    count = sum(1 for word in words if len(word) == length)
    return count

# Name of the file to read
file_path= r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"

with open(file_path, "r") as file:
        content = file.read()

word_length = int(input("Enter a whole number to count words of that length of the size entered: "))
if word_length >= 0:
    word_count = count_words(content, word_length)
    print("There are", word_count,"words of length",word_length,"in the file data.txt.")
