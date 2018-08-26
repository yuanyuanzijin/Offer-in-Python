## 题目描述：输入两个链表，找出它们的第一个公共结点。
## 方法一：用栈，从后往前查找最后一个公共节点
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        s1 = []
        s2 = []
        pNode1 = pHead1
        pNode2 = pHead2
        while pNode1:
            s1.append(pNode1)
            pNode1 = pNode1.next
        while pNode2:
            s2.append(pNode2)
            pNode2 = pNode2.next

        pNode = None
        while s1 and s2:
            n1 = s1.pop()
            n2 = s2.pop()
            if n1 == n2:
                pNode = n1
        return pNode
            

## 方法二：让长的链表的指针先走，两个指针相遇则为第一个公共节点
class Solution2:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        pNode1 = pHead1
        pNode2 = pHead2
        num1 = 0
        num2 = 0
        while pNode1:
            num1 += 1
            pNode1 = pNode1.next
        while pNode2:
            num2 += 1
            pNode2 = pNode2.next
        
        pNode1 = pHead1
        pNode2 = pHead2
        gap = abs(num1 - num2)
        while gap:
            if num1 > num2:
                pNode1 = pNode1.next
                gap -= 1
            elif num1 < num2:
                pNode2 = pNode2.next
                gap -= 1
        
        while pNode1 and pNode2:
            if pNode1 == pNode2:
                return pNode1
            pNode1 = pNode1.next
            pNode2 = pNode2.next
        
        return None


