def magic_calculation(a, b):
    result = 0

    for n in range(1, 3):
        if n > a:
            raise ValueError('Too far')
        else:
            result += a ** b / n

    return result
