## 题目描述：一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return None
        r = 0
        for a in array:
            r = r ^ a
        n = self.getFirstBitIs1(r)
        
        r1 = 0
        r2 = 0
        for a in array:
            if self.IsBit1(a, n):
                r1 = r1 ^ a
            else:
                r2 = r2 ^ a
        return [r1, r2]

    def getFirstBitIs1(self, r):
        n = 0
        while True:
            if r & 1 == 1:
                break
            n += 1
            r  = r >> 1
        return n

    def IsBit1(self, num, index):
        num = num >> index
        return num & 1


s = Solution()
print(s.FindNumsAppearOnce([1, 2, 3, 2]))
