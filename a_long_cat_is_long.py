import string
from typing import Text


def count_words(text: Text) -> dict:
    """
        The function receives text, and returns a dictionary of the word lengths in it.
        :param text: The text whose word lengths will be measured.
        :return: A dictionary of the word lengths in the text.
    """
    text = [row.split(" ") for row in text.translate(str.maketrans('', '', string.punctuation)).splitlines()]
    text = [item for sublist in text for item in sublist if item != ""]
    return {word: len(word) for word in text}
