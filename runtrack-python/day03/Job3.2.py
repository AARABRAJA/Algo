#Job 3.2
import re

# The file path:
file_path = r"C:\Users\raara\Documents\DigitalLab\Algo\Data_Projets\domains.xml"

# Initialize a dictionary to store the counts of domain extensions
extension_nbr = {}

# Read the content of the file
with open(file_path, "r") as file:
    content = file.read()

    # Domain extensions
    extensions = re.findall(r'\.\w+\b', content)

    # Count domain extensions
    for extension in extensions:
    # Convertir l'extension en minuscules pour éviter les doublons de casse
        extension = extension.lower()

        # Utiliser la méthode .count() pour compter les occurrences
        count = extensions.count(extension)

        # Stocker le comptage dans le dictionnaire
        extension_nbr[extension] = count

    # Afficher les comptages
    for extension, count in extension_nbr.items():
        print(extension,':',count)

