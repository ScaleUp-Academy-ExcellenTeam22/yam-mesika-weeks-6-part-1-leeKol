def get_positive_numbers() -> list:
    """
        The function receives from the user a series of numbers separated by a comma.
        It returns all the positive numbers that the user entered, as a list of integers.
        :return: A list of integers.
    """
    return list(filter(lambda number: number > 0,
                       map(int, input("Please enter a series of numbers separated by a comma: ").split(','))))
