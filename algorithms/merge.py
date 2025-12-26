def merge_sort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if l < r:
        m = (l + r) // 2
        yield from merge_sort(arr, l, m)
        yield from merge_sort(arr, m + 1, r)

        left = arr[l:m+1]
        right = arr[m+1:r+1]

        i = j = 0
        k = l

        while i < len(left) and j < len(right):
            yield arr, k, k
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
            yield arr, k-1, k-1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            yield arr, k-1, k-1
