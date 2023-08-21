def is_palindrome(s):
    return s.replace(" ", "") == s[::-1].replace(" ", "")