def add(values: list) -> float:
    '''
    Function to add the positive numbers of a list
    :param values: the list of values to be added
    :return: sum of the positive numbers of the given list
    '''
    total = 0.0
    for value in values:
        if value > 0:
            total += value
    return total

def subtract(values: list) -> float:
    '''
    Function to add the negative numbers in a list
    :param values: the list of values to be added
    :return: sum of the negative numbers of the given list
    '''
    total = 0
    for value in values:
        if value < 0:
            total += value
    return total

def multiply(values: list) -> float:
    '''
    FUnction to multiply the non-zero numbers of a list
    :param values: the list of values to be multiplied
    :return: the result of multiplying the non-zero numbers of the given list
    '''
    total = 0
    for value in values:
        if value != 0:
            if total == 0:
                total = value
            else:
                total *= value
    return total

def divide(values: list) -> float:
    '''
    Function to divide an initial value at index 0 of the list by the remaining numbers of that list
    :param values: a list containing the inital value at index 0, and the numbers that value is divided by
    :return: a float after the inital values has been divided by the rest of the list, None if there is divide by zero error
    '''
    total = values[0]
    for i in range(1, len(values)):
        if values[i] == 0:
            return None
        else:
            total /= values[i]
    return total

def exponentiate(values: list) -> float:
    '''
    Function to raise an inital value in a list by the next value, then the result to power of the next element thoughout the whole list
    :param values: a list of elements to raised to the power of the next element
    :return: a float resulting from taking an inital value in a list to the power of the next elements of the list
    '''
    total = values[0]
    for i in range(1, len(values)):
        total **= values[i]
    return total

def mean(values: list) -> float:
    '''
    Function to find the average value of a given list
    :param values: a list conatining the values to be averaged
    :return: a float resulting from taking the average of a list
    '''
    return sum(values) / len(values)

def min(values: list) -> any:
    '''
    Function to find the minimum value of a list
    :param values: a list containing a minimum value
    :return: the smallest value of a given list
    '''
    minimum = values[0]
    for item in values:
        if item < minimum:
            minimum = item
    return minimum

def max(values: list) -> any:
    '''
    Function to find the maximum value of a list
    :param values: a list containing a maximum value
    :return: the largest value of a given list
    '''
    maximum = values[0]
    for item in values:
        if item > maximum:
            maximum = item
    return maximum

def totalDistance(values: list[list]) -> float:
    '''
    Function to sum the distance from a point to another point, then from that point to another through a list of points
    (ex. a->b, b->c, c->n) in any single dimention (ex. point(1, 1, 1, 1) -> (2, 2, 2, 2) vs point (1, 1, 1) -> (2, 2, 2))
    :param values: a list of points given as a list to be summed
    :return: a float that is the sum of distance of given points
    '''
    total = 0
    for i in range(len(values) - 1):
        temp = 0
        for j in range(len(values[0])):
            temp += (values[i + 1][j] - values[i][j]) ** 2
        total += temp ** 0.5 
    return total

def gcd(values: list[int]) -> int:
    '''
    Function to find the greatest common divisior of a given list
    :param values: a list of integers to find the greatest common divisor
    :return: an integer that is the greatest common divisor of the given list
    '''
    currentDivisor = values[0]
    for i in range(1, len(values)):
        if currentDivisor == 0:
            currentDivisor = values[i]
        elif currentDivisor == 1:
            return 1
        else:
            currentDivisor = gcd([values[i] % currentDivisor, currentDivisor])
    return abs(currentDivisor)