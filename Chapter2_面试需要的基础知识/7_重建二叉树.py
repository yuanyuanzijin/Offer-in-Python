## 前序遍历第一个节点就是根节点的位置，在中序遍历中可以找到对应的位置，划出左子树和右子树
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos+1], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos+1:], tin[pos+1:])
        return root