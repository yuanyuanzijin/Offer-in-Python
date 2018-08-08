## 题目描述：用一条语句判断某个整数是不是2的整数次方
## 如果一个整数是2的整数次方，那么它的二进制只有一个1。用面试题15中的3解法，用这个数-1和这个数做与运算，即可把唯一的一个1变成0
class Solution:
    def NumberOf1(self, n):
        # write code here
        if n <= 0:
            return False
        if n & (n-1):
            return False
        else:
            return True

## 测试用例
s = Solution()
print(s.NumberOf1(32))


## 题目描述：输入两个整数m和n，计算m需要改变二进制中的多少位才能变成n
## 先做异或运算，再统计1的个数
class Solution2:
    def NumberOf1(self, m, n):
        # write code here
        p = m ^ n
        count = 0
        while p:
            p = (p-1) & p
            count += 1
        return count

## 测试用例
s = Solution2()
print(s.NumberOf1(32, 16))