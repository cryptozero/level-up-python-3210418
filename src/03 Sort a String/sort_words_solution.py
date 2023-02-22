def sort_words(word_string: str):
    words_list = word_string.split(" ")

    words_list.sort(key=str.lower)

    return " ".join(words_list)


if __name__ == "__main__":
    assert sort_words('banana ORANGE apple') == 'apple banana ORANGE'
    assert sort_words('B a C D') == 'a B C D'
