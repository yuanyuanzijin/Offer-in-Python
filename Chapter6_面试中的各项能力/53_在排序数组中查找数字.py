## 题目描述：统计一个数字在排序数组中出现的次数。
## 从头到尾遍历，时间复杂度O(n)
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        count = 0
        for i in data:
            if i == k:
                count += 1
        return count

## 从头到尾遍历，时间复杂度O(logn)
class Solution2:
    def GetNumberOfK(self, data, k):
        # write code here
        self.data = data
        self.k = k
        p1 = self.find(0, len(data)-1, mode="first")
        if p1 < 0:
            return 0
        p2 = self.find(0, len(data)-1, mode="last")
        return p2-p1+1

    def find(self, begin, end, mode):
        if begin > end:
            return -1
        mid = (begin + end) // 2
        print(begin, end, mid)
        if self.data[mid] > self.k:
            return self.find(begin, mid-1, mode)
        elif self.data[mid] < self.k:
            return self.find(mid+1, end, mode)
        
        if mode == "first":
            if begin == mid:
                return begin
            if self.data[mid-1] != self.data[mid]:
                return mid
            return self.find(begin, mid-1, mode)
        else:
            if end == mid:
                return end
            if self.data[mid+1] != self.data[mid]:
                return mid
            return self.find(mid+1, end, mode)

        
s = Solution2()
print(s.GetNumberOfK([3,3,3,3],3))
        

