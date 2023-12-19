def diagonal_difference(array):
    primary_diagonal = 0
    secondary_diagonal = 0
    for i in range(len(array)):
        primary_diagonal += array[i][i]
        print(primary_diagonal)
    for i in range(len(array)):
        secondary_diagonal += array[i][-1 - i]
        print(secondary_diagonal)
    difference = abs(primary_diagonal - secondary_diagonal)
    print(difference)
    return difference

test_array = [ [ 11, 2, 4 ], [ 4, 5, 6 ], [ 10, 8, -12 ] ]

diagonal_difference(test_array)
