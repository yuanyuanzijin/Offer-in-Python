## 题目描述：汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。对于一个给定的字符序列S，
## 请你把其循环左移K位后的序列输出。例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。是不是很简单？OK，搞定它！
## 借用上题的思路，先反转两个部分，再反转字符，用Python这么写有点弄巧成拙，但为了练思路嘛
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) < n:
            return ""
        part1 = self.reversed(s[:n])
        part2 = self.reversed(s[n:])
        s = self.reversed(part1 + part2)
        return s
        
    def reversed(self, s):
        new = ''
        for i in range(len(s)-1, -1, -1):
            new += s[i]
        return new


## Python大法好
class Solution2:
    def LeftRotateString(self, s, n):
        # write code here
        if not s or len(s) < n:
            return ""
        return s[n:] + s[:n]

s = Solution()
print(s.LeftRotateString("abcdefg", 2))
