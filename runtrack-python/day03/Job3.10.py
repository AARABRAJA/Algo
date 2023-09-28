#Job 3.10
file_name= r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\data.txt"
with open(file_name,'r') as file:
    text = file.read()

phrase = text.split('.')  
count= [len(sentence.split()) for sentence in phrase if sentence.strip()]

average= sum(count) / len(count)
min_words = min(count)
max_words= max(count)

print("Words per entence:",average)
print("Maximum Words per Sentence:",max_words)
print("Minimum Words per Sentence:",min_words)

import matplotlib.pyplot as plt

plt.hist(count, bins=18, edgecolor='black')
plt.xlabel('Words per Sentence')
plt.ylabel('Frequency')
plt.title('Word counts')
plt.show()

