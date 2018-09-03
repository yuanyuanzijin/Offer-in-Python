## 题目描述：请定义一个队列实现max得到队列里的最大值，要求max、push_back和pop_front的时间复杂度都是O(1)。
## 牛客网没有该题，不保证通过全部情况
class Solution:
    def __init__(self):
        self.q = []
        self.queue = []
        self.begin = 0
        self.end = -1

    def push_back(self, num):
        self.queue.append(num)
        self.end += 1
        if not self.q:
            self.q.append(self.end)
        while self.q and self.queue[self.q[-1]-self.begin] <= self.queue[-1]:
            self.q.pop()
        self.q.append(self.end)

    def pop_front(self):
        self.queue.pop(0)
        self.begin += 1
        if self.q[0] < self.begin:
            self.q.pop(0)

    def max(self):
        return self.queue[self.q[0]-self.begin]


## 测试用例
s = Solution()
l = [1, 6, 8, 1, 5, 3, 2, 5, 3]
for i in l:
    s.push_back(i)
print(s.queue)
print(s.q)
print(s.max())
for _ in range(3):
    s.pop_front()
print(s.queue)
print(s.q)
print(s.max())