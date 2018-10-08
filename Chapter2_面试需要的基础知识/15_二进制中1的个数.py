## 题目描述：输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
## 负数会引起死循环的解法
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count


## 常规解法
class Solution2:
    def NumberOf1(self, n):
        # write code here
        count = 0
        flag = 1
        while flag < 2 ** 32:
            if n & flag:
                count += 1
            flag = flag << 1
        return count


## 书上的巧妙解法，但Python会出现负数死循环
## 把一个整数减去1后和原来的数做位与运算，相当于把这个整数二进制表示中最右边的1变成0
class Solution3:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n:
            n = (n-1) & n
            count += 1
        return count


## 其他解法（适用Python）
class Solution4:
    def NumberOf1(self, n):
        # write code here
        num = 0
        if n < 0:
            n = 2 ** 32 - abs(n)
        for i in str(bin(n)).split('b')[1]:
            num += int(i)
        return num


## 测试用例
s = Solution3()
print(s.NumberOf1(-10))
