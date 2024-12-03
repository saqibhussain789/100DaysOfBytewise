# Anagram Checker
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

if are_anagrams(str1, str2):
    print(f"{str1} and {str2} are anagrams.")
else:
    print(f"{str1} and {str2} are not anagrams.")
