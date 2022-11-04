
def quicksort(arr, start, end):
  keep_start = start
  keep_end = end
  pivot = arr[(start+end)//2]

  if len(arr[start:end+1]) <= 1:
    return arr

  while start < end:
    while i < j and arr[start] < pivot:
      start += 1
    while i < j and arr[end] > pivot:
      end -= 1

    tmp = arr[start]
    arr[start] = arr[end]
    arr[end] = tmp
    start += 1
    end -= 1

  arr = quicksort(arr, start, keep_end)
  arr = quicksort(arr, keep_start, end)
  return arr

if __name__ == "__main__":
  arr = list(map(int, input().rstrip().split()))
  print(quicksort(arr, 0, len(arr) - 1))
