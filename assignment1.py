def two_sum(array, target):
    pairs = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                pairs.append([array[i], array[j]])
    return pairs

print(two_sum([5, 3, 6, 8, 2, 4, 7],10))

# PROBLEM 2
def two_sum_sorted(numbers, target):
    pairs = []
    i = 0
    j = len(numbers) - 1
    while i < j:
        if numbers[i] + numbers[j] == target:
            pairs.append([i+1, j+1])
            i += 1
            j -= 1
        elif numbers[i] + numbers[j] < target:
            i += 1
        else:
            j -= 1
    return pairs

print(two_sum_sorted([2,7,11,15],9))

# PROBLEM 3
def largest_values(array, k):
    largest = []
    for i in range(k):
        for j in range(len(array)):
            if array[j] > array[i]:
                array[i], array[j] = array[j], array[i]
        largest.append(array[i])
        array.remove(array[i])
    return largest

print(largest_values([5, 1, 3, 6, 8, 2, 4, 7],3))

