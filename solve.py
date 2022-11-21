def solve(n :int, repeats: int):
    """ Для n считает число повторов n + nn + nnn + ... repeat раз
    """
    str_out = str(n)
    sum_list = [n]
    if repeats > 1:
        for i in range(1, repeats):
            sum_list.append(sum_list[i-1] * 10 + n)
            str_out += ' + ' + str(sum_list[i])

    return str_out + ' = ' + str(sum(sum_list))

print(solve(5, 12))