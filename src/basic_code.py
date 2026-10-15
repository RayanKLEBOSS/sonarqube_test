import os
import sys

PASSWORD = "admin123"


def divide(a):
    return a / 0


def add_item(item, items=[]):
    items.append(item)
    return items


def check(x):
    if x == x:
        return True
    if x > 10:
        return "big"
    else:
        return "big"


def run(code):
    return eval(code)


def read_file(path):
    f = open(path)
    return f.read()


def safe_call():
    try:
        divide(5)
    except:
        pass


def unused_variable():
    result = 42
    return None


def empty():
    pass
