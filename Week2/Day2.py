class Solution:
    def sortColors(self, nums):
        n = len(nums)
        if not (1 <= n <= 300):
            raise ValueError("not valid")
        for e in nums:
            if not (0 <= e <= 2):
                raise ValueError("not valid")

        a, b, c = 0, 0, n - 1
        while b <= c:
            if nums[b] == 0:
                nums[a], nums[b] = nums[b], nums[a]
                a += 1
                b += 1
            elif nums[b] == 2:
                nums[b], nums[c] = nums[c], nums[b]
                c -= 1
            else:
                b += 1
        return nums
