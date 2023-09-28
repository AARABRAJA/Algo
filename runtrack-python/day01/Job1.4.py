#Job 1.4
def final_word(word):
    list_user = sorted(list(word))
    
    new_word = ''.join(list_user)
    
    return new_word

def word():
    input_user = input("Enter a word without spaces or special characters:").lower()
    
    # Vérifier que l'entrée est constituée uniquement de lettres de l'alphabet
    if not input_user.isalpha():
        print("The word must contain only letters of the alphabet.")
    else:
        new_word = final_word(input_user)
        print("The reorganized word is:", new_word)
if __name__ == "__main__":
    word()
