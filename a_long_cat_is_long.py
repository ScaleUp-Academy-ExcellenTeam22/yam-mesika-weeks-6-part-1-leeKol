import re
from typing import Text


def count_words(text: Text) -> dict:
    """
        The function receives text, and returns a dictionary of the word lengths in it.
        :param text: The text whose word lengths will be measured.
        :return: A dictionary of the word lengths in the text.
    """
    word_list = text.split()
    word_list_only_letters = [re.sub('[^a-zA-Z]+', '', word) for word in word_list]
    return {word: len(word) for word in word_list_only_letters}


if __name__ == '__main__':
    print(count_words("""
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """))
