## 题目描述：求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
class Solution:
    def Sum_Solution(self, n):
        # write code here
        if n == 1:
            return 1
        else:
            return n + self.Sum_Solution(n-1)
