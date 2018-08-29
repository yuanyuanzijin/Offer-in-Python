## 题目描述：给定一棵二叉搜索树，请找出其中的第k小的结点。例如，（5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:
            return None
        self.result = []
        self.midOrder(pRoot)
        if k > len(self.result):
            return None
        else:
            return self.result[k-1]
    
    def midOrder(self, pRoot):
        if not pRoot:
            return
        self.midOrder(pRoot.left)
        self.result.append(pRoot)
        self.midOrder(pRoot.right)
