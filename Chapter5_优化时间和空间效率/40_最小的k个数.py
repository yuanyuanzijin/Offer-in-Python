## 题目描述：输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
## 解法一，待更新

## 解法二，时间复杂度O(nlogk)
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or not k:
            return []
        minlist = []
        for i in tinput:
            if len(minlist) < k:
                minlist.append(i)
            else:
                max_index = self.findMaxIndex(minlist)
                if i < minlist[max_index]:
                    minlist[max_index] = i
        return sorted(minlist)

    def findMaxIndex(self, l):
        return max(range(len(l)), key=l.__getitem__)
