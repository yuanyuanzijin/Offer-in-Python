## 题目描述：小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。但是他并不满足于此,
## 他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。
## 现在把问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
## 和上题思路一致
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 2:
            return []
        p1 = 1
        p2 = 2
        result = []
        while p1 < p2 and p2 <= tsum//2 + 1:
            add = sum(range(p1, p2+1))
            if add == tsum:
                result.append([x for x in range(p1, p2+1)])
                p1 += 1
                p2 += 1
            elif add > tsum:
                p1 += 1
            else:
                p2 += 1
        if not result:
            return []
        return sorted(result, key=lambda x: x[0])

s = Solution()
print(s.FindContinuousSequence(15))
