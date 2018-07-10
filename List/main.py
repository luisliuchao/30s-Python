from math import ceil


def chunk(lst, size):
    return list(map(lambda x: lst[x * size: x * size + size], list(range(0, ceil(len(lst) / size)))))


def compact(lst):
    return list(filter(bool, lst))


def count_occurences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])


def deep_flatten(lst):
    def spread(arg):
        ret = []
        for i in arg:
            if isinstance(i, list):
                ret.extend(i)
            else:
                ret.append(i)
        return ret

    result = []
    result.extend(
        spread(list(map(lambda x: deep_flatten(x) if type(x) == list else x, lst)))
    )
    return result


def difference(a, b):
    return [item for item in a if item not in b]


from copy import deepcopy
from random import randint


def shuffle(lst):
    tmp_list = deepcopy(lst)
    m = len(tmp_list)
    while m:
        m -= 1
        i = randint(0, m)
        # exchange two values
        tmp_list[m], tmp_list[i] = tmp_list[i], tmp_list[m]
    return tmp_list


def spread(arg):
    ret = []
    for i in arg:
        if isinstance(i, list):
            ret.extend(i)
        else:
            ret.append(i)
    return ret


def zip(*args, fill_value=None):
    max_length = max([len(lst) for lst in args])
    result = []
    for i in range(max_length):
        result.append([
            args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))
        ])
    return result


def count_by(lst, fn=lambda x: x):
    ret = {}
    for el in map(fn, lst):
        # 'el not in ret' check the existance of key in dictionary
        ret[el] = 0 if el not in ret else ret[el]
        ret[el] += 1
    return ret


def difference_by(a, b, fn=lambda x: x):
    # create a set with unique value inside
    b = set(map(fn, b))
    return [item for item in a if fn(item) not in b]


def bubble_sort(lst):
    for i in range(1, len(lst)):
        j = i - 1
        while j >= 0 and lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            j -= 1


def has_duplicate(lst):
    return len(lst) != len(set(lst))
