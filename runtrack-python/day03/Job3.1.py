#Job 3.1

# Open the "output.txt" file in read mode
with open("output.txt", "r") as file:

# Read the contents of output.txt
    file_to_read = file.read()
    print("'output.txt' contains:")
    print(file_to_read)

