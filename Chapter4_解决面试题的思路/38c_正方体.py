## 题目描述：输入一个含有8个数字的数组，判断有没有可能把这8个数字分别放在正方体的8个顶点上，使得正方体上三组相对的面上的4个顶点的和都相等。
class Solution:
    def __init__(self):
        self.result = []
        
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        ss = ''.join(ss)
        self.perm(ss, 0)
        for i in self.result:
            i = list(map(int, list(i)))
            if i[0]+i[1]+i[2]+i[3] == i[4]+i[5]+i[6]+i[7] and i[0]+i[2]+i[4]+i[6] == i[1]+i[3]+i[5]+i[7] and i[0]+i[1]+i[4]+i[5] == i[2]+i[3]+i[6]+i[7]:
                print(i)
        
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


s = Solution()
s.Permutation('12345678')
