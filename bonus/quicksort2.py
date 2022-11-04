
def quicksort(arr, inicio, fim):
  if inicio >= fim:
    return

  pivot = arr[(inicio+fim)//2]
  i = inicio
  j = fim

  print("pivot ---->", pivot)
  print(i, j)
  while i <= j:
    while i < j and arr[i] < pivot:
      i += 1
    while i < j and arr[j] > pivot:
      j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    print("troca:", arr)
    print(i, j)
    i += 1
    j -= 1
    
  return
  quicksort(arr, inicio, j) # j
  quicksort(arr, i, fim) # i

if __name__ == "__main__":
  arr = [8, 5, 2, 9, 5, 6, 3]
  quicksort(arr, 0, len(arr) - 1)
  print(arr)
