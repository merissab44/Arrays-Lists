def two_sum(array, target):
    pairs = []
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                pairs.append([array[i], array[j]])
    return pairs

print(two_sum([5, 3, 6, 8, 2, 4, 7],10))