# # write a program to find the length of your name
name = input("Enter your name:")
print("length of your name is:", len(name))

# find the ocurrence of a character in your name
char = input("Enter a character to find its occurrence in your name:")
print(str.count("s", char))

# find the index of a character in your name
name = input("Enter your name:")
char = input("Enter a character to find its index in your name:")
print("Index of", char, "in your name is:", name.index(char))

# replace an item in the list
str = input("Enter a string:")
old_char = input("Enter the character you want to replace:")
new_char = input("Enter the new character:")
print("New string after replacement:", str.replace(old_char, new_char))