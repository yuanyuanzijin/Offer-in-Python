## 题目描述：一个长度为n-1内的n个数字每个都是唯一的，且都在0~n-1之内，找出缺失的数字。
## 牛客网没有该题，未经过全面的测试
## 从头到尾遍历，时间复杂度O(n)
class Solution:
    def GetNumber(self, data):
        # write code here
        for i in range(len(data)):
            if i != data[i]:
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
            return self.find(mid+1, end)
        
        if begin == mid:
            return mid
        else:
            return self.find(begin, mid-1)


s = Solution2()
print(s.GetNumber([0,1,3,4]))
