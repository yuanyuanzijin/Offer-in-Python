## 题目描述：把n个骰子扔到地上，所有朝上的点数之和为s，输入n，打印出s的所有可能值的概率。
## 牛客网没有该题，不保证通过所有样例
class Solution:
    def solveAllPro(self, n):
        if n < 1:
            return []
        prob = 6
        length = prob * n
        array = [[0 for _ in range(length+1)], [0 for _ in range(length+1)]]
        for i in range(1, prob+1):   
            array[0][i] = 1
        flag = 1
        for i in range(2, n+1):
            for j in range(1, i):
                array[flag][j] = 0
            for j in range(i, length+1):
                array[flag][j] = sum(array[1-flag][max(j-prob, 0):j])
            flag = 1-flag
        total = prob ** n
        result = array[1-flag][n:]
        return [x/total for x in result]

s = Solution()
p = s.solveAllPro(10)
print(p, len(p), sum(p))
