## 题目描述：给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，
## 那么一共存在6个滑动窗口，他们的最大值分别为{4,4,6,6,6,5}； 针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个： {[2,3,4],2,6,2,5,1}， 
## {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
class Solution:
    def maxInWindows(self, num, size):
        # write code here
        if not size:
            return []
        result = []
        q = []
        for i in range(len(num)):
            if not q:
                q.append(i)
            if i - q[0] >= size:
                q.pop(0)
            while q and num[q[-1]] <= num[i]:
                q.pop()
            q.append(i)
            if i >= size-1:
                result.append(num[q[0]])
        return result
