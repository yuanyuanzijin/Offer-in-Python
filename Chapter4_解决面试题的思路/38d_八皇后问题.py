## 题目描述：在8x8的棋盘上摆放八个皇后，使得任意两个皇后不得处在同一行，同一列或者同一条对角线上，问共有多少种摆法？
class Solution:
    def Queen(self, size):
        # write code here
        import itertools
        result = []
        for p in itertools.permutations(range(size), size):
            result.append(p)
            for c in itertools.combinations(range(size), 2):
                if c[0]-c[1] == p[c[0]]-p[c[1]] or c[0]-c[1] == p[c[1]]-p[c[0]]:
                    result.pop()
                    break
        return len(result)


import math
s = Solution()
size = 8
nums = s.Queen(size)
print("不在同一行或同一列的情况总数：%d" % math.factorial(size))
print("答案数量：%d" % nums)
