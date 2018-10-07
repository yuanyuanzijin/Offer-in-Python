## 题目描述“将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的库函数。 
## 数值为0或者字符串不是一个合法的数值则返回0。
class Solution:
    def StrToInt(self, s):
        # write code here
        cond1 = (len(s) == 0)
        cond2 = (len(s) == 1) and (s[0] in ['+', '-'])
        if cond1 or cond2:
            self.errorFlag = True
            return 0

        flag = 0
        p = 0
        if s[0] in ['+', '-']:
            p += 1
            if s[0] == '-':
                flag = 1
        
        num = 0
        while p < len(s):
            first = ord(s[p]) - 48
            if first not in range(0, 10):
                self.errorFlag = True
                return 0
            num = num * 10 + first
            p += 1
        return num if not flag else -num


s = Solution()
print(s.StrToInt(''))
