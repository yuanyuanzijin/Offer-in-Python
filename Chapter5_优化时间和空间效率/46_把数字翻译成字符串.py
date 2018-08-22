## 给定一个数字，按照字母顺序翻译成a,b,c,d...，求共有多少种翻译方法。
## 牛客网没有该题
class Solution:
    def getCount(self, n):
        if n <= 0:
            return 0
        self.count = 0
        self.Calculate(str(n))
        return self.count

    def Calculate(self, n):
        if not n:
            self.count += 1
            return
        self.Calculate(n[1:])
        if len(n) >= 2 and int(n[:2]) in range(10, 26):
            self.Calculate(n[2:])

s = Solution()
while True:
    n = input("请输入要查询的数字（回车退出）：")
    if not n:
        break
    print(s.getCount(int(n)))
        
