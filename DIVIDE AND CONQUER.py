def min_max(a, i, n):
    if n == 2:
        if a[i] > a[i + 1]:
            max_val = a[i]
            min_val = a[i + 1]
        else:
            max_val = a[i + 1]
            min_val = a[i]
    else:
        mid = n // 2
        max1, min1 = min_max(a, i, mid)
        max2, min2 = min_max(a, i + mid, n - mid)
        min_val = min(min1, min2)
        max_val = max(max1, max2)

    return max_val, min_val