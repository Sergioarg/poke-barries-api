""" Main math operations to calculate the data """

class MathOperations:
    """ Some math operations """

    def calculate_mean(self, numbers: list) -> float:
        """Caculate the media """
        result = sum(numbers) / len(numbers)

        return result


    def calculate_median(self, numbers: list) -> float:
        """ Calculate median """
        numbers.sort()
        lenght = len(numbers)

        if lenght % 2 == 0:
            median = (numbers[lenght // 2 - 1] + numbers[lenght // 2]) / 2
        else:
            median = numbers[lenght // 2]

        return median


    def calculate_variance(self, numbers: list) -> float:
        """ Calculate variance in base of numbers data """
        mean = self.calculate_mean(numbers)
        variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)

        return variance

    def calculate_frequency_growth_times(self, numbers: list) -> dict:
        """ Calculate the frequency of growth times """

        frequency = {}

        for time in numbers:
            if time in frequency:
                frequency[time] += 1
            else:
                frequency[time] = 1

        return frequency
