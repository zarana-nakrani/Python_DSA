def fruits_in_basket(arr):
    start, end = 0, 0
    max_fruits = 0
    baskets = {}
    for end in range(len(arr)):
        right_char = arr[end]
        if right_char not in baskets:
            baskets[right_char] = 0
        baskets[right_char] += 1

        while len(baskets) > 2:
            left_char = arr[start]
            start += 1
            baskets[left_char] -= 1
            if baskets[left_char] == 0:
                del baskets[left_char]

        max_fruits = max(max_fruits, end - start + 1)
    return max_fruits

print(fruits_in_basket(['A', 'B', 'C', 'B', 'B', 'C']))
