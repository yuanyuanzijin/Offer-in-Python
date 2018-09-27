## 用两个队列实现栈，也非常巧妙
class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    
    def push(self, node):
        # write code here
        if self.list1:
            l = self.list1
        else:
            l = self.list2
        l.append(node)
        
    def pop(self):
        if self.list1:
            l1 = self.list1
            l2 = self.list2
        else:
            l1 = self.list2
            l2 = self.list1
        while len(l1) > 1:
            l2.append(l1.pop(0))
        return l1.pop(0)


s = Solution()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
s.push(4)
print(s.pop())
s.push(5)
print(s.pop())
print(s.pop())
print(s.pop())
