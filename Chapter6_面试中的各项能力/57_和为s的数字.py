## 题目描述：输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        p1 = 0
        p2 = len(array) - 1
        result = []
        while p1 < p2:
            add = array[p1] + array[p2]
            if add == tsum:
                result.append((array[p1], array[p2]))
                p2 -= 1
                p1 += 1
            elif add > tsum:
                p2 -= 1
            else:
                p1 += 1
        if not result:
            return []
        return min(result, key=lambda x: x[0] * x[1])

s = Solution()
print(s.FindNumbersWithSum([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20], 21))
