from typing import Generator, Callable
from collections.abc import Iterable


def my_filter(function: Callable, iterable: Iterable) -> Generator[object, None, None]:
    """
        The function is a generator that receives a function as the first parameter,
        and iterable as the second parameter.
        The function executes on each of the iterable items the function obtained as a parameter,
        and returns the member if and only if the value returned from the function is equal to True.
        In this way the function performs a filter on the iterable.
        :param function: The function that will be executed on each of the iterable items.
        :param iterable: The iterable to be filtered.
        :return: A generator iterator that holds the filtered iterable.
    """
    for item in iterable:
        if function(item):
            yield item
