def two_sum(a, t):
    # your code here
    pairs = []
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == t:
                pairs.append([a[i], a[j]])
    return pairs

print(two_sum([5, 3, 6, 8, 2, 4, 7],10))