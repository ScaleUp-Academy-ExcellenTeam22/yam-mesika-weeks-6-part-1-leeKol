def words_length(sentence):
    """
        The function receives a sentence and returns its word lengths,
        in the order in which they appear in the sentence (punctuation marks are part of the word lengths).
        :param sentence: The sentence whose word lengths will be measured.
        :return: A list of the word lengths.
    """
    return [len(word) for word in sentence.split(" ")]
