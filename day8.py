# 2.Read the content of that file**
with open('day8.txt', 'r') as file:
    content = file.read()
print(content)

# 3.Write a Python program to read a file line by line and store it into a list
with open('day8.txt', 'r') as file:
    # lines = file.readlines()
    lines = [line.strip() for line in file.readlines()]
print(lines)

# 4.Write a Python program to count the number of lines in a text file.
with open('day8.txt', 'r') as file:
    num_lines = 0
    for line in file:
        num_lines += 1
print("Number of lines in the file:", num_lines)

# 5.Write a Python program to read a random line from a file.
import random
def read_random_line(filename):
    with open(filename, 'r') as file:
        return random.choice(file.readlines()).strip()
filename = "day8.txt" 
random_line = read_random_line(filename)
print("Random line from the file:", random_line)
# 6.Write a Python program that takes a text file as input and returns the number of words of a given text file.**
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        word_count = len(text.split())
        return word_count

file_path = input("Enter the path to the text file: ")  
word_count = count_words(file_path)
print("Number of words in the file:", word_count)

# 7.Write a program in Python which allows you to insert at the 3rd position of an existing file called myFile.txt, the line "This line was inserted via Python code! " without changing the existing content file*
file_path = "day8.txt"
line_to_insert = "This line was inserted via Python code!"
with open(file_path, 'r+') as file:
    lines = file.readlines()
    lines.insert(2, line_to_insert + '\n')  # 2 corresponds to the 3rd position (0-indexed)
    file.seek(0)
    file.writelines(lines)
