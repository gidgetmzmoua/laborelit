def find_offsets_greater_than_10(arr):
    offsets = [i for i in range(len(arr)) if arr[i] > 10]
    return offsets
