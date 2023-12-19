def simple_array_sum(array):
    sum = 0
    for i in range(len(array)):
        sum += array[i]
        print(sum)
    return sum


test_array = [1, 2, 3, 4, 5]
simple_array_sum(test_array)