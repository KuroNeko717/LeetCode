class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr=[]
        for x in range(1,n+1):
            if x % 3 == 0 and x % 5== 0:
                arr.append("FizzBuzz")
            elif x % 3 == 0:
                arr.append("Fizz")
            elif x % 5 == 0:
                arr.append("Buzz")
            else:
                arr.append(str(x))
        return arr
    
# Optimum Solution:
# class Solution:
#     def fizzBuzz(self, n: int) -> List[str]:
#         answer = []
#         for i in range(1,n+1):
#             if i % 3 != 0 and i % 5 != 0:
#                 answer.append(str(i))
#             else:
#                 if i % 3 == 0 and i % 5 == 0:
#                     answer.append("FizzBuzz")
#                     continue
#                 else:
#                     if i % 3 == 0:
#                         answer.append("Fizz")
#                         continue
#                     if i % 5 == 0:
#                         answer.append("Buzz")
#                         continue
                
#         return answer
