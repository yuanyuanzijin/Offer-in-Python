## 题目描述：给一段长度为n的绳子，请把绳子剪成m段(m>1)，使每段绳子的乘积最大，得出该值。
## 由于牛客网没有该题，不保证通过所有用例

## 方法一：动态规划
class Solution:
    def maxProduct(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        result = [0, 1, 2, 3]
        for i in range(4, n+1):
            max_ = 0
            for j in range(1, i//2+1):
                max_ = max(max_, result[j]*result[i-j])
            result.append(max_)
        return max_


## 方法二：贪婪算法
class Solution2:
    def maxProduct(self, n):
        if n <= 1:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        seg3 = n // 3
        if n % 3 == 1:
            seg3 -= 1
        seg2 = (n - seg3 * 3) // 2
        return 3**seg3 * 2**seg2


s = Solution()
s2 = Solution2()
for n in range(30):
    print(n, s.maxProduct(n), s2.maxProduct(n))
