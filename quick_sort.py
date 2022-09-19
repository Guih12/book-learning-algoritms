def quick_sort(arr):
  if len(arr) < 2:
    return arr
  else:
    pivot = arr[0]
    minor = [i for i in arr[1:] if i <= pivot]
    high = [i for i in arr[1:] if i > pivot]

    return quick_sort(minor) + [pivot] + quick_sort(high)


print(quick_sort([2, 5, 6, 10, 70, 4]))