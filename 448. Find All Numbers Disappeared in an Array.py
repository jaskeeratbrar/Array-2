
## time complexity - O(n)
## space complexity - O(1)

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        for i in nums:
            idx = abs(i) -1
            nums[idx] = -1 * abs(nums[idx])

        arr = []
        for i, n in enumerate(nums):
            if n > 0:
                arr.append(i+1)

        return arr







        
