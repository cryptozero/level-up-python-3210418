def is_palindrome(phrase: str):
    phrase_letters = "".join([c for c in phrase.lower() if c.isalpha()])

    if phrase_letters == reversed(phrase_letters):
        return True
    else:
        return False


if __name__ == "main":
    assert is_palindrome("racecar")
    assert not is_palindrome("hola")
