## 用两个栈实现队列，非常巧妙
class Solution:
    def __init__(self):
        self.list1 = []
        self.list2 = []
    
    def push(self, node):
        # write code here
        self.list1.append(node)
        
    def pop(self):
        if not self.list2:
            while self.list1:
                self.list2.append(self.list1.pop())
        return self.list2.pop()

## 相关题目
## 用两个队列实现一个栈
## 待完成