class Solution(object):
    def twoSum(self, nums, target):
      n=len(nums)
      if not(2<= n<=10000):
        print('Not Valid')
        return nums
      for element in nums:
        if not(-10**9<=element<=10**9):
             print('Not Valid')
             return nums
      if not(-10**9<=target<=10**9):
        print('Not Valid')
        return nums
      flag=False 
      for i in range(n):
        for j in range(i+1,n):
            if(nums[i]+nums[j]==target):
                flag=True
                return i,j
      if(flag==False):
        print('No answer')
    