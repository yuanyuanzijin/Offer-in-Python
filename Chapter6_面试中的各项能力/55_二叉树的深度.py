## 题目描述：输入一棵二叉树，求该树的深度。从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
## 方法一：全部遍历
class Solution:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        self.result = []
        self.findNext(pRoot, 1)
        return max(self.result)
    
    def findNext(self, root, deep):
        if not root:
            self.result.append(deep-1)
            return
        self.findNext(root.left, deep+1)
        self.findNext(root.right, deep+1)


## 方法二：书中的
class Solution2:
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        deep = self.findNext(pRoot)
        return deep
    
    def findNext(self, root):
        if not root:
            return 0
        left = self.findNext(root.left)
        right = self.findNext(root.right)
        return max(left, right) + 1

