class Solution(object):
    def findDisappearedNumbers(self, nums):
        temp = set(range(1, len(nums) + 1))
        for num in nums:
            temp.discard(num)
        return list(temp)