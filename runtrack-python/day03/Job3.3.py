#Job 3.3
import re

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

file_path= r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"
with open(file_path, "r") as file:
    text_file = file.read()
    word_count = count_words(text_file)
    print("Le fichier 'data' contient",word_count,"mots.")



