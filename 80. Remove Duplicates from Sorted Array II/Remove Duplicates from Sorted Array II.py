class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in set(nums):
            while nums.count(i)>2:
                nums.remove(i)