# Task 1 — Create Strings
name = "Darshit"
city = 'Kadi'
favorite_language = "Python"
message = 'Python is easy to learn.'

print("Name:", name)
print("City:", city)
print("Favorite Language:", favorite_language)
print("Message:", message)


# Task 2 — Empty String
empty_string = ""

print("String:", empty_string)
print("Length:", len(empty_string))
print("Data Type:", type(empty_string))


# Task 3 — String Information
text = "Python Programming"

print("Complete string:", text)
print("Length:", len(text))
print("First character:", text[0])
print("Last character:", text[-1])
print("Third character:", text[2])
print("Second-last character:", text[-2])


# Task 4 — Positive Indexing
text = "Programming"

print("First character:", text[0])
print("Second character:", text[1])
print("Fifth character:", text[4])
print("Last character:", text[len(text) - 1])


# Task 5 — Negative Indexing
print("Last character:", text[-1])
print("Second-last character:", text[-2])
print("Third-last character:", text[-3])
print("First character:", text[-len(text)])


# Task 6 — Indexing Challenge
full_name = "Darshit Dangar"

print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("First character of last name:", full_name[8])



# Task 7 — Basic Slicing
text = "Python Programming"

print("Python:", text[0:6])
print("Programming:", text[7:18])
print("Complete string:", text[:])
print("First 5 characters:", text[:5])
print("Last 5 characters:", text[-5:])


# Task 8 — Slicing with Step
text = "ABCDEFGHIJKL"

print("Every second character:", text[::2])
print("Every third character:", text[::3])
print("Index 1 to 8 with step 2:", text[1:9:2])
print("Reverse:", text[::-1])


# Task 9 — Slicing with Negative Indexes
text = "Python Programming"

print("Last 5 characters:", text[-5:])
print("Last 10 characters:", text[-10:])
print("Characters from the end using negative step:", text[-1:-11:-1])


# Task 10 — Slicing Challenge
text = "Programming"

print("First 3 characters:", text[:3])
print("Last 3 characters:", text[-3:])
print("Every second character:", text[::2])
print("Reverse:", text[::-1])
print("Without first and last character:", text[1:-1])


# Task 11
word = "Python"
sentence = "Python is easy."
sentence_with_spaces = "Python is very easy to learn."

print("Word length:", len(word))
print("Sentence length:", len(sentence))
print("Sentence with spaces length:", len(sentence_with_spaces))


# Task 12
text = "Python Programming"

last_index = len(text) - 1

print("Last valid positive index:", last_index)
print("Last character:", text[last_index])



# Task 13 — Full Name
first_name = "Darshit"
last_name = "Dangar"

full_name = first_name + " " + last_name

print("Full name:", full_name)


# Task 14 — Sentence Creation
name = "Darshit"
age = 20
city = "Kadi"
programming_language = "Python"

sentence = (
    "My name is " + name +
    ", I am " + str(age) +
    " years old, I live in " + city +
    ", and I am learning " + programming_language + "."
)

print(sentence)


# Task 15 — String and Integer
age = 20
print("Age: " + age)

# Correct version:
age = 20
print("Age: " + str(age))



# Task 16
symbol = "*"

print(symbol * 3)
print(symbol * 5)
print(symbol * 10)


# Task 17 — Pattern
print("*" * 10)



# Task 18
text = "python programming language"

print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())
print("Swapcase:", text.swapcase())


# Task 19 — Case-Insensitive Comparison
text1 = "Python"
text2 = "python"

print("Original comparison:", text1 == text2)
print("Lowercase comparison:", text1.lower() == text2.lower())



# Task 20 — Membership
text = "Python is a programming language"

print("Python:", "Python" in text)
print("programming:", "programming" in text)
print("Java:", "Java" in text)
print("language:", "language" in text)


# Task 21 — find()
print("Python position:", text.find("Python"))
print("programming position:", text.find("programming"))
print("language position:", text.find("language"))
print("Java position:", text.find("Java"))
# find() returns -1 when the searched text is not found.


# Task 22 — index()
print("Python position:", text.index("Python"))
print("programming position:", text.index("programming"))
print("language position:", text.index("language"))

# Correct safe alternative:
java_position = text.find("Java")
print("Java position using find():", java_position)


# Task 23 — Count Characters
text = "banana"

print("Count of a:", text.count("a"))
print("Count of n:", text.count("n"))
print("Count of b:", text.count("b"))


# Task 24 — Starts and Ends
filename = "student_notes.pdf"

print("Starts with student:", filename.startswith("student"))
print("Ends with .pdf:", filename.endswith(".pdf"))
print("Ends with .txt:", filename.endswith(".txt"))



# Task 25 — Replace a Word
text = "I am learning Java"

new_text = text.replace("Java", "Python")

print(new_text)


# Task 26 — Multiple Replacements
text = "apple apple apple"

new_text = text.replace("apple", "mango")

print(new_text)


# Task 27 — Limited Replacement
new_text = text.replace("apple", "mango", 1)

print(new_text)


# Task 28 — Check Immutability
text = "Python"

text.upper()
print("Original string:", text)

text = text.upper()
print("After storing result:", text)



# Task 29
text = "   Python Programming   "

print("Original:", repr(text))
print("strip():", repr(text.strip()))
print("lstrip():", repr(text.lstrip()))
print("rstrip():", repr(text.rstrip()))


# Task 30 — User Input
name = input("Enter your name: ")
cleaned_name = name.strip()

print("Cleaned name:", cleaned_name)



# Task 31 — Split
text = "Python is easy to learn"

words = text.split()

print(words)


# Task 32 — Split with Separator
text = "apple,banana,mango,orange"

fruits = text.split(",")

print(fruits)


# Task 33 — Join
words = ["Python", "is", "easy"]

sentence = " ".join(words)

print(sentence)


# Task 34 — Join with Different Separators
words = ["Python", "is", "easy"]

print("-".join(words))
print("/".join(words))



# Task 35 — F-String
name = "Darshit"
age = 20
city = "Kadi"

sentence = f"My name is {name}, I am {age} years old, and I live in {city}."

print(sentence)


# Task 36 — Arithmetic Inside F-String
a = 10
b = 20

print(f"The sum is {a + b}")



# Task 37

# A
# text = "Python"
# print(text[20])
# Error: IndexError
# Reason: Index 20 is outside the valid range of the string.

# Correct version:
text = "Python"
print("A corrected:", text[0])


# B
# text = "Python"
# text[0] = "J"
# Error: TypeError
# Reason: Strings are immutable and individual characters cannot be changed directly.

# Correct version:
text = "Python"
text = "J" + text[1:]
print("B corrected:", text)


# C
# age = 20
# print("Age: " + age)
# Error: TypeError
# Reason: String and integer cannot be concatenated using + directly.

# Correct version:
age = 20
print("C corrected:", "Age: " + str(age))


# D
# text = "Python"
# print(text.index("Java"))
# Error: ValueError
# Reason: index() raises ValueError when the searched text is not found.

# Correct version:
text = "Python"
print("D corrected:", text.find("Java"))



# Task 38 — Name Processor
full_name = input("Enter your full name: ")

print("Original input:", full_name)

cleaned_name = full_name.strip()

print("Cleaned name:", cleaned_name)
print("Uppercase:", cleaned_name.upper())
print("Lowercase:", cleaned_name.lower())
print("Title case:", cleaned_name.title())
print("Length:", len(cleaned_name))
print("First character:", cleaned_name[0])
print("Last character:", cleaned_name[-1])

chosen_character = input("Enter a character to search for: ")
print(
    f"Contains '{chosen_character}':",
    chosen_character in cleaned_name
)



# Task 39 — Sentence Analyzer
sentence = input("Enter a sentence: ")

print("Original sentence:", sentence)
print("Number of characters:", len(sentence))

words = sentence.split()
print("Number of words:", len(words))

if sentence:
    print("First character:", sentence[0])
    print("Last character:", sentence[-1])
else:
    print("First character: No character")
    print("Last character: No character")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Title case:", sentence.title())
print("Contains Python:", "Python" in sentence)

chosen_character = input("Enter a character to count: ")
print(
    f"Number of times '{chosen_character}' occurs:",
    sentence.count(chosen_character)
)



# Task 40 — Student Information
first_name = input("Enter first name: ").strip()
last_name = input("Enter last name: ").strip()
city = input("Enter city: ").strip()
course = input("Enter course: ").strip()
age = int(input("Enter age: "))

full_name = first_name + " " + last_name

print("Full name:", full_name)
print("Title case:", full_name.title())
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
print("Length of full name:", len(full_name))
print("First character:", full_name[0])
print("Last character:", full_name[-1])
print("City:", city)
print("Course:", course)
print(f"Age: {age}")
print("Course contains Python:", "Python" in course)

word_to_replace = input("Enter a word from the course to replace: ")
replacement_word = input("Enter the replacement word: ")

updated_course = course.replace(word_to_replace, replacement_word, 1)

print("Updated course:", updated_course)
print("Number of words in course:", len(course.split()))
