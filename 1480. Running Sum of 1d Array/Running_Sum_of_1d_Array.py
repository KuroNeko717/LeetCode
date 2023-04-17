class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        val=0
        for i in range(0,len(nums)):
            nums[i]+=val
            val= nums[i]
        return nums
    
# Optimum and best solution
# class Solution:
#     def runningSum(self, nums: List[int]) -> List[int]:
#         ret = [nums[0]]
#         for v in nums[1:]:
#             ret.append(ret[-1] + v)
#         return ret