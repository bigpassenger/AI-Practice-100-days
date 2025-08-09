# first = "Hello"
# second = "World"
# result = first + " " + second
# print(result)

########################## Spliting #############################

# text = "Python Programming"
# print(text[0:6])
# print(text[-11:])

########################## Formating #############################
# name = "Alice"
# age = 25
# print(f"my name is {name} and i am {age} years old")

########################## split()&join()&replace&strip() #############################
# split()

# sentence = "Python is fun"
# words = sentence.split()
# print(words)

# # join()
# sentence = " ".join(words)
# print(sentence)

# sentence = sentence.replace("is","IS")
# print(sentence)

# messy = "    Hello,world     "
# cleaned_text = messy.strip()
# print(cleaned_text)
########################## Regular Expressions #############################
# import re

"""
This code demonstrates the use of Python's `re` module for working with regular expressions.

1. `re.findall(r"\d+", text)`:
   - `\d` matches any digit (0–9).
   - `+` means "one or more" of the preceding token.
   - So `\d+` matches complete sequences of digits (e.g., "123", "456", "7890").
   - `findall()` returns all matches as a list of strings.

2. `re.sub(r"\d", "X", text)`:
   - `\d` again matches a single digit (0–9).
   - No `+` here, so it replaces each digit individually.
   - `sub(pattern, replacement, string)` replaces all matches with the given replacement string ("X").

Summary:
- `\d` → matches exactly one digit.
- `\d+` → matches a whole number (one or more digits in a row).
- `findall()` → finds all matches and returns them as a list.
- `sub()` → replaces all matches with the specified replacement text.
"""

# text = "Contact me at 123-456-7890"
# digits = re.findall(r"\d+", text)
# print(digits)  # ['123', '456', '7890']

# updated_text = re.sub(r"\d", "X", text)
# print(updated_text)  # Contact me at XXX-XXX-XXXX
########################## EXERCISE 1 #############################
# import re

# text = str(input()).lower()
# text = re.sub(r"[^\w\s]", "",text)
# print(text)
# text = " ".join(text.split())
# print(text)
# text = text.strip()
# print(text)
########################## EXERCISE 2 palindromes#############################
# import re
# text = str(input()).lower()

# text2 = re.sub(r"[^\w\s]", "",text)

# text2 = "".join(text2.split())

# if text2[::-1] == text2:
#     print("Palindrome")
########################## EXERCISE 3 count vowels#############################
# import re

# text = "Beautiful day in the neighborhood"
# vowels = re.findall(r"[aeiou]", text, flags=re.IGNORECASE)
# print(vowels)          # ['e', 'a', 'u', 'i', 'u', 'a', 'i', 'e', 'i', 'o', 'o']
# print(len(vowels))     # Count of vowel letters
