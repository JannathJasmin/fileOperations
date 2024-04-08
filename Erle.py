# 8.Write a program to prompt for a file name, and then read through the file line-by-line.
# Prompt for a file name
file_name = input("Enter the file name: ")

try:
    # Open the file
    with open(file_name, 'r') as file:
        # Read through the file line-by-line
        for line in file:
            # Print each line
            print(line.strip())
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("An error occurred:", e)

# 9.Write a Python program that displays the longest word found in a text file
filename = 'Erle.txt'
with open(filename, 'r') as file:
    words = file.read().split()
    longest_word = max(words, key=len)

print("The longest word in the file is:", longest_word)
