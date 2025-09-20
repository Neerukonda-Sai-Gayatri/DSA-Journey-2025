class Solution(object):
    def rearrangeArray(self, nums):
        
        positives = [num for num in nums if num > 0]
        negatives = [num for num in nums if num < 0]
        result = []
        for p, n in zip(positives, negatives):
            result.append(p)
            result.append(n)
        return result
