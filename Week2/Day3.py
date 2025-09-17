class Solution(object):
    def majorityElement(self, nums):
       n=len(nums)
       if not(1<=n<=5*(10**4)):
        raise ValueError("not valid")
        return 0
       for e in nums:
        if not(-10**9<=e<=10**9):
            raise ValueError("not valid")
            return 0
        candidate = None
        count = 0
        
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif num == candidate:
                count += 1
            else:
                count -= 1
        return candidate