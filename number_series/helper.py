def square_pattern(n):
    pattern_list = []
    for i in range(1, n+1):
        pattern_list.append(i**2)
    return pattern_list

    # # Using list comps
    # pattern_list = [i**2 for i in range(1, n+1)]
    # return pattern_list


def add_square_pattern(n):
    pattern_list = []
    x = 1
    for i in range(1, n+1):
        pattern_list.append(x)
        x = x + i**2
    return pattern_list


def cube_pattern(n):
    pattern_list = [i**3 for i in range(1, n+1)]
    return pattern_list

# 1, 3, 8, 18


def square_plus_one_pattern(n):
    pattern_list = []
    x = 1
    for i in range(1, n+1):
        pattern_list.append(x)
        x = x + i**2 + 1
    return pattern_list


# 1, 3, 12,
def cube_plus_one_pattern(n):
    pattern_list = []
    x = 1
    for i in range(1, n+1):
        pattern_list.append(x)
        x = x + i**3 + 1
    return pattern_list
