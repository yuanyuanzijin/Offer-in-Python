## 题目描述：用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
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
