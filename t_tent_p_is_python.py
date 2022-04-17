def get_letters() -> list:
    """
        The function returns the list of all characters between a and z and between A and Z.
        :return: A list of all characters between a and z and between A and Z.
    """
    return [chr(lower_case_letter) for lower_case_letter in range(ord('a'), ord('z') + 1)] + \
           [chr(upper_case_letter) for upper_case_letter in range(ord('A'), ord('Z') + 1)]
