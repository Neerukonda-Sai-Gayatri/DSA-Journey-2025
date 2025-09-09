class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        if not (1 <= n <= 10**3):
            raise ValueError("Array size must be between 1 and 10^3")
        for num in arr:
            if not (1 <= num <= 10**6):
                raise ValueError("Array elements must be between 1 and 10^6")
        for i in range(n):
            m = i
            for j in range(i+1, n):
                if arr[m] > arr[j]:
                    m = j
            arr[i], arr[m] = arr[m], arr[i]
        return arr
