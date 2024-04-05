""" Main math operations to calculate the data """
from functools import wraps

def validate_not_empty_and_numeric(func):
    """ Decorator to validate list of numbers """
    @wraps(func)
    def wrapper(self, numbers: list):
        if not numbers:
            raise ValueError("The list of numbers cannot be empty.")
        if not all(isinstance(num, (int, float)) for num in numbers):
            raise ValueError("All items in the list must be numbers.")
        return func(self, numbers)
    return wrapper


class MathOperations:
    """ Some math operations """
    @validate_not_empty_and_numeric
    def calculate_mean(self, numbers: list) -> float:
        """Caculate the media """
        result = sum(numbers) / len(numbers)

        return result

    @validate_not_empty_and_numeric
    def calculate_median(self, numbers: list) -> float:
        """ Calculate median """
        numbers.sort()
        lenght = len(numbers)

        if lenght % 2 == 0:
            median = (numbers[lenght // 2 - 1] + numbers[lenght // 2]) / 2
        else:
            median = numbers[lenght // 2]

        return median

    @validate_not_empty_and_numeric
    def calculate_variance(self, numbers: list) -> float:
        """ Calculate variance in base of numbers data """
        mean = self.calculate_mean(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

        return variance

    @validate_not_empty_and_numeric
    def calculate_frequency(self, numbers: list) -> dict:
        """ Calculate the numbers frequency """

        frequency = {}

        for time in numbers:
            if time in frequency:
                frequency[time] += 1
            else:
                frequency[time] = 1

        return frequency
