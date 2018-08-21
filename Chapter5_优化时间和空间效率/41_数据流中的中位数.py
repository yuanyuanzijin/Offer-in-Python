## 题目描述：如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
## 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
## 使用GetMedian()方法获取当前读取数据的中位数。

class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []
        
    def Insert(self, num):
        # write code here
        self.list1.append(num)
        leftMax = max(self.list1)
        self.list2.append(leftMax)
        self.list1.remove(leftMax)
        if len(self.list1) < len(self.list2):
            rightMin = min(self.list2)
            self.list1.append(rightMin)
            self.list2.remove(rightMin)

        
    def GetMedian(self, nums):
        # write code here
        if len(self.list1) - len(self.list2) == 1:
            return max(self.list1)
        else:
            return (max(self.list1) + min(self.list2)) / 2.0