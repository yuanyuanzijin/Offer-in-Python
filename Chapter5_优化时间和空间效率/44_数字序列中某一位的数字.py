## 题目描述：数字以0123456789101112131415...存储，求第n位对应的数字。
## 牛客网没有该题
class Solution:
    def findDigit(self, n):
        if n == 0:
            return 0
        rest = n-1
        bit = 1
        tmp = rest
        while True:
            tmp -= bit * 9 * 10 ** (bit-1)
            if tmp < 0:
                break
            else:
                rest = tmp
                bit += 1
        current = rest // bit + 10 ** (bit-1)
        return str(current)[rest % bit]

s = Solution()
print(s.findDigit(int(input("请输入数字："))))
