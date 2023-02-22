def is_palindrome(phrase: str):
    phrase_letters = "".join([c for c in phrase.lower() if c.isalpha()])

    return phrase_letters == phrase_letters[::-1]


if __name__ == "__main__":
    assert is_palindrome("race car")
    assert not is_palindrome("hola")
