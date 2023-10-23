def magic_calculation(a, b):
    result = 0
    for n in range(1, 3):
        try:
            if n > a:
                raise Exception('Too far')
            else:
                result += a ** b / n
        except ValueError:
            result = b + a
            break
    return (result)
