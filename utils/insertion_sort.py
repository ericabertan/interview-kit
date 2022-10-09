
def insertion_sort(v):
  size = len(v)

  for j in range(1, size):
    pivot = v[j]
    i = j - 1
    while (i >= 0 and pivot < v[i]):
      v[i + 1] = v[i]
      i -= 1
    v[i + 1] = pivot

  return v

if __name__ == "__main__":
  unordered_list = list(map(int, input().rstrip().split()))
  ordered_list = insertion_sort(unordered_list)
  print(ordered_list)
