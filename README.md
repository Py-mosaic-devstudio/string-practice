# 🔤 Python String Practice – Basics of String Functions

## 📌 Purpose
This simple Python program helps beginners practice **basic string operations** such as:
- Finding the **length** of a string
- Counting the **occurrence** of a character
- Finding the **index** of a character
- **Replacing** characters in a string

The exercises aim to strengthen understanding of string methods through real-time user input.

---

## 🧠 What You'll Learn

- How to use `input()` for user interaction
- How to apply string methods like:
  - `len()` – to get length
  - `count()` – to find how many times a character appears
  - `index()` – to find the position of a character
  - `replace()` – to modify a string by replacing characters
- How to handle and transform user input dynamically

---

## ✅ Program Code (Well-Formatted)

```python
# 🔢 Find the length of your name
name = input("Enter your name: ")
print("Length of your name is:", len(name))

# 🔁 Find the occurrence of a character in your name
char = input("Enter a character to find its occurrence in your name: ")
print("Occurrence of", char, "is:", name.count(char))

# 📍 Find the index of a character in your name
char = input("Enter a character to find its index in your name: ")
print("Index of", char, "in your name is:", name.find(char))

# 🔄 Replace a character in a string
user_str = input("Enter a string: ")
old_char = input("Enter the character you want to replace: ")
new_char = input("Enter the new character: ")
print("New string after replacement:", user_str.replace(old_char, new_char))
💡 Helping Note
Always check if a character exists before using methods like .index() to avoid errors. Use .find() instead — it returns -1 if the character is not found.

Try entering different names and characters to understand how string methods behave with different inputs.

These basic operations are foundation-level skills needed for data cleaning, text analysis, and real-world automation tasks.

Happy Coding! 👩‍💻👨‍💻
