## 题目描述：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent <= 0:
            raise ZeroDivisionError('0的0次方没有意义！')
        if exponent == 0:
            return 1
        result = 1
        for _ in range(abs(exponent)):
            result = result * base
        if exponent < 0:
            result = 1 / result
        return result

s = Solution()
print(s.Power(0, 3))


## 考虑到2的32次方可用2的16次方的平方实现
class Solution2:
    def Power(self, base, exponent):
        # write code here
        if base == 0 and exponent <= 0:
            raise ZeroDivisionError('0的0次方没有意义！')
        if exponent == 0:
            return 1

        result = self.PowerUnsigned(base, abs(exponent)) 
        if exponent < 0:
            result = 1 / result
        return result

    def PowerUnsigned(self, base, exponent):
        if exponent == 0:
            return 1
        if exponent == 1:
            return base
        result = self.PowerUnsigned(base, exponent >> 1)
        result *= result
        if exponent & 1:
            result *= base
        return result


s = Solution2()
print(s.Power(2, 3))