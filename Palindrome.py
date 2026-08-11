import string

phrase = input('Enter a phrase: ')

clean_phrase = ""

for char in phrase.lower():
    if char not in string.punctuation and char != " ":
        clean_phrase += char

if clean_phrase == clean_phrase[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")