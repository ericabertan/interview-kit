
# By reversed I just mean we're going to begin from the last position
# of the vector to the first one.

def reversed_insertion_sort(v):
  size = len(v)
  
  for i in range(size - 2, -1, -1):
    j = i + 1
    pivot = v[i]
    while(j < size and pivot > v[j]):
      v[j - 1] = v[j]
      j += 1
    v[j - 1] = pivot

  return v


if __name__ == "__main__":
  unordered_list = list(map(int, input().rstrip().split()))
  ordered_list = reversed_insertion_sort(unordered_list)
  print(ordered_list)
