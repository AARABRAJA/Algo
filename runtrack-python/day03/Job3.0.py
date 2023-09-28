#Job 3.0

# Ask the user to input
input_user = input("Write a sentence of your choice: ")

# Open a file named "output.txt" in write mode
with open("output.txt", "w") as file:
    # Write the user's input 
    file.write(input_user)

print("The string has been successfully written to 'output.txt'.")

