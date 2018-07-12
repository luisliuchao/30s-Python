def keys_only(flat_dict):
    lst = []
    for k, v in flat_dict.items():
        lst.append(k)
    return lst


def values_only(flat_dict):
    lst = []
    for k, v in flat_dict.items():
        lst.append(v)
    return lst


def all_unique(lst):
    return len(lst) == len(set(lst))
