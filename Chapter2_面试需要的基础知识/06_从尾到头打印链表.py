## 题目描述：输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
## 思路一，使用栈可以反转链表
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        s = []
        head = listNode
        while head:
            s.append(head.val)
            head = head.next
        return [s.pop() for i in range(len(s))]


## 思路二，递归的本质也是栈，可以使用递归
class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if not listNode:
            return []
        self.l = []
        head = listNode
        self.getNext(head)
        self.l.append(head.val)
        return self.l
    
    def getNext(self, head):
        if head.next:
            head = head.next
            self.getNext(head)
            self.l.append(head.val)


## 自己的想法，python可以轻松实现从头插入
class Solution3:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        l = []
        node = listNode
        while node:
            l.insert(0, node.val)
            node = node.next
        return l