def average(*args):
    return sum(args, 0.0) / len(args)


def factorial(num):
    # check the number is non negative integer
    if not ((num >= 0) & (num % 1 == 0)):
        raise Execption(f"Number({num}) can't be floating point or negative")
    return 1 if num == 0 else num * factorial(num - 1)


from functools import reduce


def spread(arg):
    ret = []
    for i in arg:
        # check the instance of value
        if isinstance(i, list):
            # concat the list at the end
            ret.extend(list)
        else:
            # push the value to the end of the list
            ret.append(i)
    return ret


def gcd(*args):
    numbers = []
    # type of args is tuple
    print(type(args))
    # create list from tuple using list()
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else _gcd(y, x % y)

    return reduce((lambda x, y: _gcd(x, y)), numbers)


def lcm(*args):
    numbers = []
    numbers.extend(spread(list(args)))

    def _gcd(x, y):
        return x if not y else _gcd(y, x % y)

    def _lcm(x, y):
        return x * y / _gcd(x, y)

    return reduce((lambda x, y: _lcm(x, y)), numbers)


def max_n(lst, n=1, reverse=True):
    return sorted(lst, reverse=reverse)[:n]


from copy import deepcopy


def min_n(lst, n=1):
    numbers = deepcopy(lst)
    numbers.sort()
    return numbers[:n]
