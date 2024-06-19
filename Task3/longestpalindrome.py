def longest_palindromic_substring(s):
    if not s:
        return ""

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    start, end = 0, 0
    for i in range(len(s)):
        len1 = len(expand_around_center(s, i, i))
        len2 = len(expand_around_center(s, i, i + 1))
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

# Take input from user and test the function
s = input("Enter a string to find the longest palindromic substring: ")
print("The longest palindromic substring is:", longest_palindromic_substring(s))
