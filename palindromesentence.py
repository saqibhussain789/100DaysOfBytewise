# Palindrome Sentences
import re

sentence = input("Enter a sentence: ")

def is_palindrome_sentence(s):
    s = re.sub(r'[^A-Za-z]', '', s).lower()
    return s == s[::-1]

if is_palindrome_sentence(sentence):
    print(sentence, "is a palindrome.")
else:
    print(sentence, "is not a palindrome.")
