input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    for t in array :
        if t == number :
            return True
    return False


result = is_number_exist(4, input)
print(result)