def max_min(a):

    a.sort()  # O(n log n)
    max_val = a[-1]  # O(1)
    min_val = a[0]   # O(1)
    return max_val, min_val