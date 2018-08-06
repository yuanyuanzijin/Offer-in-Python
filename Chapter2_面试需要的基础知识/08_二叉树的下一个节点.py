## 如果有右子树，则为右子树的最左子节点，否则看下一条
## 如果该节点没有父节点（即为根节点），则没有结果，否则看下一条
## 如果该节点是父节点的左子节点，则为它的父节点，否则看下一条
## 逐层向上，直到当前节点为父节点的左子节点时，得到答案，答案为它的父节点
class Solution:
    def GetNext(self, pNode):
        # write code here
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        if not pNode.next:
            return None
        if pNode == pNode.next.left:
            return pNode.next
        while pNode.next:
            if pNode == pNode.next.left:
                return pNode.next
            else:
                pNode = pNode.next
        return None