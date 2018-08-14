## 题目描述：定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（各函数时间复杂度应为O（1））。
class Solution:
    def __init__(self):
        self.value = []
        self.value_min = []
    
    def push(self, node):
        # write code here
        if not self.value_min or node <= self.value_min[-1]:
            self.value_min.append(node)
        else:
            self.value_min.append(self.value_min[-1])
        self.value.append(node)
    
    def pop(self):
        # write code here
        self.value.pop()
        self.value_min.pop()

    def top(self):
        # write code here
        return self.value[-1]

    def min(self):
        # write code here
        return self.value_min[-1]
