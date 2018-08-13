## 题目描述：操作给定的二叉树，将其变换为源二叉树的镜像。
## 递归方式
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None or root.left == None and root.right == None:
            return
        root.left, root.right = root.right, root.left
        self.Mirror(root.left)
        self.Mirror(root.right)
        return

## 循环方式
class Solution2:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        pStack = [root]
        while pStack:
            pHead = pStack.pop()
            pHead.left, pHead.right = pHead.right, pHead.left
            if pHead.left:
                pStack.append(pHead.left)
            if pHead.right:
                pStack.append(pHead.right)
        