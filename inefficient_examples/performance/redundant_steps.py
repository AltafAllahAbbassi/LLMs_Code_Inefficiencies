# HumanEval/4 by CodeLlama-7B
# the instruc-tion mean(numbers) is recalculated in each iteration. Instead, calling it once and storing the result in a variable would be sufficient.

from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    return sum(abs(x - mean(numbers)) for x in numbers) / len(numbers)