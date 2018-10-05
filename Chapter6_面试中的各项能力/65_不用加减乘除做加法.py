## 题目描述：写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
class Solution:
    def Add(self, num1, num2):
        # write code here
        mask = 0xFFFFFFFF
        while True:
            sum_ = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum_ & mask
            num2 = carry & mask
            if not carry:
                break
        return sum_ if sum_ <= 0x7FFFFFFF else ~(sum_ ^ mask)
            
s = Solution()
print(s.Add(-2, -1))
