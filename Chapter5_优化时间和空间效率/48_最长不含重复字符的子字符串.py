## 题目描述：给定一个字符串，找出不含有重复字符的最长子串的长度。
## LeetCode测试通过
class Solution:
    def lengthOfLongestSubstring(self, s):
        cur_str = ""
        max_str = ""
        for i in s:
            if i not in cur_str:
                cur_str += i
            else:
                if len(cur_str) > len(max_str):
                    max_str = cur_str
                cur_str = cur_str[cur_str.index(i)+1:] + i
        if len(cur_str) > len(max_str):
            max_str = cur_str
        return max_str

s = Solution()
print(s.lengthOfLongestSubstring(" "))