def is_palindrome(text):
    clean_text = ''.join(text.lower().split())
    return clean_text == clean_text[::-1]


word = input("Enter a word: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")