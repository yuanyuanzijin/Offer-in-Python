## 题目描述：输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc, 则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
## 替换的思想
class Solution:
    def __init__(self):
        self.result = []
        
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self.perm(ss, 0)
        return sorted(self.result)
        
    def perm(self, ss, begin):
        if begin >= len(ss)-1:
            if ss not in self.result:
                self.result.append(ss)
            return
        words = list(ss)
        self.perm(ss, begin+1)
        for i in range(begin+1, len(words)):
            words[begin], words[i] = words[i], words[begin]
            self.perm(''.join(words), begin+1)


## python自带库
class Solution2:
    def Permutation(self, ss):
        # write code here
        import itertools
        if not ss:
            return []
        return sorted(set([''.join(i) for i in itertools.permutations(ss, len(ss))]))


s1 = Solution()
s2 = Solution2()
print(s1.Permutation('asda'))
print(s2.Permutation('asda'))
