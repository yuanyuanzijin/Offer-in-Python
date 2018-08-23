## 题目描述：把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
## 求按从小到大的顺序的第N个丑数。
## 最直观的，时间复杂度过高，牛客网不通过
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        count = 0
        n = 0
        while count < index:
            n += 1
            if self.isUgly(n):
                count += 1
        return n


    def isUgly(self, n):
        while n % 2 == 0:
            n = n / 2
        while n % 3 == 0:
            n = n / 3
        while n % 5 == 0:
            n = n / 5
        if n == 1:
            return True
        else:
            return False


## 用空间换时间的算法
class Solution2:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        result = [1]
        t2 = 0
        t3 = 0
        t5 = 0
        while len(result) < index:
            m2 = result[t2] * 2
            m3 = result[t3] * 3
            m5 = result[t5] * 5
            m = min(m2, m3, m5)
            if m2 == m:
                t2 += 1
            if m3 == m:
                t3 += 1
            if m5 == m:
                t5 += 1
            result.append(m)
        return result[-1]


index = int(input("请输入N："))
s = Solution()
print(s.GetUglyNumber_Solution(index))
s2 = Solution2()
print(s2.GetUglyNumber_Solution(index))
