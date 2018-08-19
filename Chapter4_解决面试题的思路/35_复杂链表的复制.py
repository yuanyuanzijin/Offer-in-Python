## 题目描述：输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），返回结果为复制后复杂链表的head。
## （注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

## 方法一：时间复杂度O(n)
class Solution2:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None

        pNode = pHead
        while pNode:
            pNext = pNode.next
            pClone = RandomListNode(pNode.label)
            pNode.next = pClone
            pClone.next = pNext
            pNode = pNext

        flag = 0
        pNode = pHead
        while pNode:
            if flag % 2 == 0:
                pRandom = pNode.random
                if pRandom:
                    pNode.next.random = pRandom.next
            pNode = pNode.next
            flag += 1
        
        pNode = pHead
        pHeadNew = pHead.next
        pNodeNew = pHeadNew
        pNode.next = pNodeNew.next
        pNode = pNode.next

        while pNode:
            pNodeNew.next = pNode.next
            pNodeNew = pNodeNew.next
            pNode.next = pNodeNew.next
            pNode = pNode.next
        return pHeadNew


## 方法二，单纯的复制，时间复杂度O(n^2)，实测时间过长，可能存在问题
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        pNode = pHead
        pHeadNew = RandomListNode(pHead.label)
        pNodeNew = pHeadNew
        while pNode.next:
            pNode = pNode.next
            pNodeNew.next = RandomListNode(pNode.label)
            pNodeNew = pNodeNew.next

        pNode = pHead
        pNodeNew = pHeadNew
        while pNode:
            p1 = pHead
            p2 = pNode.random
            if not p2:
                continue
            step = 0
            while p1 != p2:
                p1 = p1.next
                step += 1
            
            p3 = pHeadNew
            for _ in range(step):
                p3 = p3.next
            pNodeNew.random = p3
            
            pNode = pNode.next
            pNodeNew = pNodeNew.next
        return pHeadNew

