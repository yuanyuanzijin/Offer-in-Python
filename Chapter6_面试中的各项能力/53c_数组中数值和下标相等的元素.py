## 题目描述：一个单调递增的数组每个元素都是整数且唯一，请找出任意一个数值等于下标的元素。
## 牛客网没有该题，未经过全面的测试
## 从头到尾遍历，时间复杂度O(n)
class Solution:
    def GetNumber(self, data):
        # write code here
        for i in range(len(data)):
            if i == data[i]:
                return data[i]
        return -1

## 从头到尾遍历，时间复杂度O(logn)
class Solution2:
    def GetNumber(self, data):
        # write code here
        self.data = data
        p = self.find(0, len(data)-1)
        return p
    
    def find(self, begin, end):
        if begin > end:
            return -1
        mid = (begin + end) // 2
        if self.data[mid] == mid:
            return mid
        elif self.data[mid] < mid:
            return self.find(mid+1, end)
        else:
            return self.find(begin, mid-1)


s = Solution2()
print(s.GetNumber([0,2,3,4]))
