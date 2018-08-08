## 题目描述：在O(1)时间内删除链表节点。 
## 例如，链表1->2->3->4->5删除后为 1->2->3->5
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

class Solution:
    def deleteDuplication(self, pHead, pDeleted):
        # write code 
        if not pHead or not pDeleted:
            return None
        if not pHead.next:
            return None

        if pDeleted.next:
            pDeleted.val = pDeleted.next.val
            pDeleted.next = pDeleted.next.next
        else:
            pNode = pHead
            while pNode.next != pDeleted:
                pNode = pNode.next
            pNode.next = None
        return pHead


## 测试用例
def createNode(nodes):
    if nodes:
        return ListNode(nodes[0], createNode(nodes[1:]))
    else:
        return None

s = Solution()
node = createNode([1,3,5,7,9,11,13,15])
print("原始链表：", node)
deleteIndex = 5
nodeDeleted = node.getSubNode(deleteIndex)
print("要删除的节点值：", nodeDeleted.val)
s.deleteDuplication(node, nodeDeleted)
print("删除后的链表：", node)
