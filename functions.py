from operator import itemgetter


def count_divisible(number1, number2, number3):
    """
    A function that takes as a parameters number1(int), number2(int) and number3.
    Function need to return the count of integers that are divisible by number3 in range [number1, number2]
    """

    return sum(1 for i in range(number1, number2 + 1) if i % number3 == 0)


def count_letters_digits(value):
    """
    A function that takes sentense as a parameter and count number of letters and digits
    """

    digits = letters = 0

    for c in value:

        if c.isdigit():
            digits += 1
        elif c.isalpha():
            letters += 1
        else:
            pass

    return {"letters": letters, "digits": digits}


def sort_persons(input_list):
    """
    A function that takes list of tuples and sort it based on the next rules:
    name / age / height / weight
    """

    return sorted(input_list, key=lambda obj: (obj[0], -int(obj[1]), -int(obj[2]), -int(obj[3])))
