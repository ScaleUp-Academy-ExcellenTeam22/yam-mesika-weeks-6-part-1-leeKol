def full_names(first_names: list, last_names: list, *min_length: int) -> list:
    """
        The function receives a list of first names and a list of last names, and makes up full names from them.
        For each first name, the function will attach all the family names received.
        The function also receives an optional parameter of minimum length- if the parameter has been passed,
        full names whose number of characters is less than the minimum length will not be returned from the function.
        :param first_names: A list of the first names.
        :param last_names: A list of the last names.
        :param min_length: minimum length for full name (optional).
        :return: A list of the full names.
    """
    return [first_name.capitalize() + " " + last_name.capitalize()
            for first_name in first_names for last_name in last_names
            if (len(first_name) + len(last_name) + 1) >= int(*min_length)]
