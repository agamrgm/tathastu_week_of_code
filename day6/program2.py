def sort012( a, arr_size): 

    lo = 0

    hi = arr_size - 1

    mid = 0

    while mid <= hi: 

        if a[mid] == 0: 

            a[lo], a[mid] = a[mid], a[lo] 

            lo = lo + 1

            mid = mid + 1

        elif a[mid] == 1: 

            mid = mid + 1

        else: 

            a[mid], a[hi] = a[hi], a[mid]  

            hi = hi - 1

    return a 

def printArray( a): 

    for k in a: 

        print k, 

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1] 

arr_size = len(arr) 

arr = sort012( arr, arr_size) 

print "Array after segregation :\n", 

printArray(arr)
_____________

program3.py

def segregate(arr, size): 

    j = 0

    for i in range(size): 

        if (arr[i] <= 0): 

            arr[i], arr[j] = arr[j], arr[i] 

            j += 1  

    return j

def findMissingPositive(arr, size): 

    for i in range(size): 

        if (abs(arr[i]) - 1 < size and arr[abs(arr[i]) - 1] > 0): 

            arr[abs(arr[i]) - 1] = -arr[abs(arr[i]) - 1] 

    for i in range(size): 

        if (arr[i] > 0): 

            return i + 1

    return size + 1

def findMissing(arr, size): 

    shift = segregate(arr, size) 

    return findMissingPositive(arr[shift:], size - shift)  

arr = [ 0, 10, 2, -10, -20 ] 

arr_size = len(arr)  

missing = findMissing(arr, arr_size)  

print("The smallest positive missing number is ", missing) 
