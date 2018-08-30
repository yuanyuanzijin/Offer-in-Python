## 题目描述：一个整型数组里除了一个数字之外，其他的数字都出现了三次。
## 牛客网没有该题，不保证通过所有测试用例
class Solution:
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return None
        add = 0
        for i in array:
            add += int(str(bin(i)).split('b')[1])
        add = list(str(add))
        r = []
        for b in add:
            r.append(str(int(b) % 3))
        r = int(''.join(r))
        return r
        

s = Solution()
print(s.FindNumsAppearOnce([1, 2, 2, 2, 3, 3, 3]))
