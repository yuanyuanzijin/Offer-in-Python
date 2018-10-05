## 题目描述：股票价格存在数组中，请问买卖股票的最大利润是多少？

# 牛客网没有该题
class Solution:
    def getMaxProfit(self, array):
        if len(array) < 2:
            return 0
        minValue = array[0]
        maxProfit = 0
        for a in array:
            maxProfit = max(maxProfit, a-minValue)
            minValue = min(minValue, a)
        return maxProfit


s = Solution()
print(s.getMaxProfit([5, 2, 3, 9, 5, 6, 1, 6, 5]))
