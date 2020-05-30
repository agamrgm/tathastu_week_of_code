def kthSmallest(arr, n, k): 

    arr.sort() 

    return arr[k-1] 

if _name=='main_': 

    arr = [12, 3, 5, 7, 19] 

    n = len(arr) 

    k = 2

    print("K'th smallest element is", 

          kthSmallest(arr, n, k))
