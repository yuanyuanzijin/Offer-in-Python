## 题目描述：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
## 方法一：有大量的重复遍历
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        left = self.Treedeep(pRoot.left)
        right = self.Treedeep(pRoot.right)
        if abs(left - right) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)
    
    def Treedeep(self, root):
        if not root:
            return 0
        left = self.Treedeep(root.left)
        right = self.Treedeep(root.right)
        return max(left, right) + 1


## 方法二：边遍历边判断
class Solution2:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        deep = self.findNext(pRoot)
        if deep != False:
            return True
        else:
            return False
    
    def findNext(self, root):
        if not root:
            return 0
        left = self.findNext(root.left)
        right = self.findNext(root.right)
        if left is False or right is False:
            return False
        diff = abs(left - right)
        if diff > 1:
            return False
        else:
            return max(left, right) + 1
            
