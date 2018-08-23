## 题目描述：在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）。
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        d = {}
        for i in s:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        for j in range(len(s)):
            if d[s[j]] == 1:
                return j
        return -1

s = Solution()
print(s.FirstNotRepeatingChar("abaccdeff"))
