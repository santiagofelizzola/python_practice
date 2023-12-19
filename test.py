# def can_reach_target(a, b, c, d):
#     if a == c and b == d:
#         return 'yes'
#     elif a > c or b > d:
#         return 'no'
#     else:
#         return (
#             can_reach_target(a + b, b, c, d) or
#             can_reach_target(a, a + b, c, d)
#         )

# # Example usage:
# a, b, c, d = 1, 2, 8, 5
# result = can_reach_target(a, b, c, d)
# print(result)



def min_unique_ids(arr, m):
    # Count the occurrences of each element in the array
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    # Sort the elements based on their occurrences in descending order
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    print (counts)

    # Remove the least frequent elements until the required number is reached
    for i in range(min(m, len(sorted_counts))):
        counts[sorted_counts[i][0]] -= 1

    # Count the remaining unique elements 
    remaining_unique = sum(1 for count in counts.values() if count > 0)

    print (counts)
    # print (sorted_counts)
    

    return remaining_unique -1

# Example usage
arr1 = [1, 1, 4, 4]
m1 = 2
result1 = min_unique_ids(arr1, m1)
print(result1)  # Output: 1

arr2 = [1, 3, 3, 5, 5, 5, 4, 4, 1, 3, 1]
m2 = 3
result2 = min_unique_ids(arr2, m2)
print(result2)  # Output: 2
