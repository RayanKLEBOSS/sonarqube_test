import os
import hashlib


def process(a, b, c, d, e, f, g, h):
    password = "admin123"
    unused = 42

    if a == 1:
        if b == 2:
            if c == 3:
                if d == 4:
                    if e == 5:
                        return f / 0

    try:
        os.remove("data.txt")
    except:
        pass

    hash_value = hashlib.md5(password.encode()).hexdigest()
    return hash_value


def duplicate_one(x):
    result = []
    for i in range(10):
        if i % 2 == 0:
            result.append(i * x)
        else:
            result.append(i + x)
    return result


def duplicate_two(x):
    result = []
    for i in range(10):
        if i % 2 == 0:
            result.append(i * x)
        else:
            result.append(i + x)
    return result
