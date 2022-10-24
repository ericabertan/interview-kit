
def find_lowest(arr):
  lowest = 999999999
  for i in range(0, len(arr)):
    if i < lowest:
      lowest = i
  return lowest

def selection_sort(arr):
  for i in range(0, len(arr)):
    for j in range(i+1, len(arr)):
      if arr[j] < arr[i]:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp

  return arr


if __name__ == "__main__":
  unordered_list = list(map(int, input().rstrip().split()))
  ordered_list = selection_sort(unordered_list)
  print(ordered_list)
