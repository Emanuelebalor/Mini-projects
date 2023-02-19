
# binary search
def binary_search(n: list, target: int):
    middle = 0
    start = 0
    end = len(n)
    steps = 0

    while start <= end:
        print(f"Steps {steps} : {n[start: end+1]}")
        steps += 1
        middle = (start + end) // 2

        if target == n[middle]:
            return middle
        elif target < n[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1


# binary search with recursion
def binary_search_recursive(n: list, target: int, start, end):

    if end >= start:
        middle = (start + end) // 2

        if n[middle] == target:
            return middle

        elif target < n[middle]:
            return binary_search_recursive(n, target, start, middle-1)

        else:
            return binary_search_recursive(n, target, middle+1, end)

    else:
        return -1


