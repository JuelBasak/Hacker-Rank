def average(array):
    array = set(array)
    return sum(array) / len(array)


print(average([161, 182, 161, 154, 176, 170, 167, 171, 170, 174]))