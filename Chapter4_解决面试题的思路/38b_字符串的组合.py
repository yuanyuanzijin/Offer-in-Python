## 题目描述：输入一个字符串,按字典序打印出该字符串中字符的所有组合。例如输入字符串abc, 则打印出由字符a,b,c所能排列出来的组合有a,b,c,ab,ac,bc,abc。
## 分解递归
class Solution:
    def __init__(self):
        self.result = []
        
    def Combination(self, ss):
        # write code here
        if not ss:
            return []
        for i in range(1, len(ss)+1):
            self.comb(ss, "", i)
        return sorted(self.result)
        
    def comb(self, ss, h, num):
        if num == 0:
            if h and h not in self.result:
                self.result.append(h)
            else:
                return
        if not ss or len(ss) < num:
            return
        self.comb(ss[1:], h+ss[0], num-1)
        self.comb(ss[1:], h, num)


## python自带库
class Solution2:
    def Combination(self, ss):
        # write code here
        import itertools
        if not ss:
            return []
        result = []
        for num in range(1, len(ss)+1):
            result += [''.join(i) for i in itertools.combinations(ss, num)]
        return set(result)


s1 = Solution()
print(s1.Combination('abc'))
s2 = Solution2()
print(s2.Combination('abc'))
