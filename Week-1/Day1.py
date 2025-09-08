class Solution:
    def bubbleSort(self, arr):
        n = len(arr)

        if not (1 <= n <= 10**3):
            print ("Array size must be between 1 and 10^3")
            return arr

        for element in arr:
            if not (1 <= element <= 10**3):
                print ("Array elements must be between 1 and 10^3")
                return arr

    
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr   
