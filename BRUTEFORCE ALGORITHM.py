def max_min(a):
    n = len(a)
    if n == 1:
        max_val = min_val = a[0]

    elif n == 2:
        if a[0] > a[1]:
            max_val = a[0]
            min_val = a[1]
        else:
            max_val = a[1]
            min_val = a[0]
    else:
        max_val = min_val = a[0]
        for i in range(1, n):
            if a[i] > max_val:
                max_val = a[i]
            if a[i] < min_val:
                min_val = a[i]
    return max_val, min_val