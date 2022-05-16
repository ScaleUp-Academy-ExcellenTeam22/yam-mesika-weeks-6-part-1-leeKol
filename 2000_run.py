from typing import Callable
import time


def timer(function: Callable, *args: tuple, **kwargs: dict) -> float:
    """
        The function receives a function and other parameters.
        It measures how long the received function ran when the received parameters were passed to it.
        :param function: The function to be executed.
        :param args: The arguments to be passed to the function.
        :param kwargs: The arguments to be passed to the function (if there are keywords).
        :return: The time it took to run the function.
    """
    start = time.time()
    function(*args, **kwargs)
    end = time.time()
    return end - start
