class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        if not (1 <= n <= 1000):
            raise ValueError("Array size must be between 1 and 1000")
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
        return arr
