## 题目描述：大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
## 循环方法
class Solution:
    def Fibonacci(self, n):
        # write code here
        ans = [0, 1]
        for i in range(2, n+1):
            ans.append(ans[i-1] + ans[i-2])
        return ans[n]


class Solution2:
    def jumpFloor(self, number):
        # write code here
        a = 0
        b = 1
        for _ in range(number):
            a, b = b, a + b
        return a


## 递归方法，不一定可以完成，效率低
class Solution3:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.Fibonacci(n-1) + self.Fibonacci(n-2)
