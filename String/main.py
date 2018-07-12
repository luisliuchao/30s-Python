# import reg exp library
import re


def count_vowels(str):
    return len(re.findall(r'[aeiou]', str, re.IGNORECASE))


def byte_size(str):
    return len(str.encode('utf-8'))


def capitalize(str, lower_rest=False):
    return str[:1].upper() + str[1:].lower() if lower_rest else string[:1]


def capitalize_every_world(str):
    return str.title()


def decapitalize(str, upper_rest=True):
    return str[:1].lower() + str[1:].upper() if upper_rest else str[:1]


def palindrome(str):
    from re import sub
    # replace the space with empty string
    s = sub('[\W]', '', str.lower())
    return s == s[::-1]


def is_upper_case(str):
    return str == str.upper()


def is_lower_case(str):
    return str == str.lower()
