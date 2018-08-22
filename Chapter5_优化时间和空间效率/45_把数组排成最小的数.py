## 题目描述：输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。例如输入数组{3，32，321}，
## 则打印出这三个数字能排成的最小数字为321323。
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        from functools import cmp_to_key
        numlist = list(map(str, numbers))
        numlist.sort(key=cmp_to_key(lambda a, b: self.Compare(a, b)))
        return int("".join(numlist))
    
    def Compare(self, a, b):
        return 1 if int(a+b) >= int(b+a) else -1

s = Solution()
print(s.PrintMinNumber([3, 321, 32]))