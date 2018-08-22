## 题目描述：求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,
## 但是对于后面问题他就没辙了。ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        bit = len(str(n))
        count = 0
        for i in range(bit):
            cb = int(str(n)[i])
            if cb == 1:
                count += (n % 10 ** (bit-1-i) + 1)
            elif cb >= 2:
                count += 10 ** (bit-1-i)
            if bit-2-i >= 0:
                count += cb * (bit-1-i) * 10 ** (bit-2-i)
        return count

s = Solution()
print(s.NumberOf1Between1AndN_Solution(21345))
