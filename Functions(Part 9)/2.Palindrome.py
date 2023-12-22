def palindrome(word):
    reversed_word = word[::-1]
    return reversed_word.lower() == word.lower()


print("казак -", palindrome("казак"))
print("холод -", palindrome("холод"))
print("level -", palindrome("level"))
print("zoo -", palindrome("zoo"))
