
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right  = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def main():
    print('Start Executing Main')
    print (quicksort([2, 5, 7, 9, 1, 4, 2]))

if __name__ == '__main__':
    main()

