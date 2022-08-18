def search_binary(list, item):
    down = 0
    high = len(list) - 1

    while down <= high:
        mid = (down + high) / 2
        kick = list[mid]

        if kick == item:
            return mid
        
        if kick > item:
            high = mid - 1
        else:
            down = mid + 1

    return None

list = [1, 2, 3, 4, 5]

result = search_binary(list, 2)
print(result)