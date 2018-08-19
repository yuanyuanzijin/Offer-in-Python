## 题目描述：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.nodes = []
    
    def middleout(self, root):
        if root.left:
            self.middleout(root.left)
        self.nodes.append(str(root.val))
        if root.right:
            self.middleout(root.right)

    def __str__(self):
        self.nodes = []
        self.middleout(self)
        return " -> ".join(self.nodes)


class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if pRootOfTree == None:
            return None
        pHead = self.getLeft(pRootOfTree)
        self.ConvertNode(pRootOfTree)
        return pHead

    def ConvertNode(self, pRootOfTree):
        pCurrent = pRootOfTree
        pLeft = pCurrent.left
        pRight = pCurrent.right
        if pLeft != None:
            self.ConvertNode(pLeft)
            leftMax = self.getRight(pLeft)
            leftMax.right = pCurrent
            pCurrent.left = leftMax
        if pRight != None:
            self.ConvertNode(pRight)
            rightMin = self.getLeft(pRight)
            rightMin.left = pCurrent
            pCurrent.right = rightMin
        
    def getLeft(self, pRoot):
        pNode = pRoot
        while pNode.left:
            pNode = pNode.left
        return pNode

    def getRight(self, pRoot):
        pNode = pRoot
        while pNode.right:
            pNode = pNode.right
        return pNode


## 测试用例
node = TreeNode(10, TreeNode(6, TreeNode(4), TreeNode(8)), TreeNode(14, TreeNode(12), TreeNode(16)))
print(node)
s = Solution()
s.Convert(node)
