## 题目描述：在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。 
## 例如，链表1->2->3->3->4->4->5 处理后为 1->2->5

## 方便调试，自定义ListNode类，在牛客网上不需要自己定义
class ListNode:
    def __init__(self, x, y=None):
        self.val = x
        self.next = y
        
    def getSubNode(self, index):
        for i in range(index):
            self = self.next
        return self
    
    def __str__(self):
        nodes = []
        while self:
            nodes.append(str(self.val))
            self = self.next
        return " -> ".join(nodes)


## 方法一：和书上思路大体一致
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        pNode = pHead
        pPre = None
        lastval = None
        while pNode:
            if (pNode.val != lastval):
                if not pNode.next or (pNode.val != pNode.next.val):
                    if pPre:
                        pPre.next = pNode
                        pPre = pPre.next
                    else:
                        pPre = pNode
                        pHead = pPre
            lastval = pNode.val
            pNode = pNode.next
        if pPre:
            pPre.next = None
            return pHead
        else:
            return None


## 方法二：个人方法，由于首节点可能被删除，因此在链表前加了一个空节点，按照正常的判断做就可以。
class Solution2:
    def deleteDuplication(self, pHead):
        # write code here
        pNode = ListNode(None)
        pNode.next = pHead
        pHead = pNode
        pPre = pHead
        pNode = pNode.next
        lastval = None
        while pNode:
            if (pNode.val != lastval):
                if not pNode.next or (pNode.val != pNode.next.val):
                    pPre.next = pNode
                    pPre = pPre.next
            lastval = pNode.val
            pNode = pNode.next
        pPre.next = None
        return pHead.next


## 测试用例
def createNode(nodes):
    if nodes:
        return ListNode(nodes[0], createNode(nodes[1:]))
    else:
        return None

s = Solution2()
node = createNode([1,1,1,2,3,5,5,6,6])
print("原始链表：", node)
nodeNew = s.deleteDuplication(node)
print("新链表：", nodeNew)