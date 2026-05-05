class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b = 0
        n = len(prices) -1
        s = n
        for i in range(1,n):
            if s > i and prices[b] > prices [i]:
                b = i
            if n-i > b and prices[s] < prices[n -i]:
                s = n -i

        profit = prices[s] - prices[b]
        return profit if profit > 0 else 0