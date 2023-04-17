class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        for customer in accounts:
            wealth = 0
            for bank_amount in customer:
                wealth = wealth + bank_amount
                arr.append(wealth)
        
        return max(arr)