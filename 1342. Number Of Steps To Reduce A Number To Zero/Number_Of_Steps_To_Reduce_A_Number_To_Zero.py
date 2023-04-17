class Solution:
    def numberOfSteps(self, num: int) -> int:
        a = num
        steps=0
        while a!=0:
            steps+=1
            if a % 2 == 0:
                a//=2
                continue
            else:
                a-=1
                continue
        return steps
    
obj = Solution()
obj.numberOfSteps(123)