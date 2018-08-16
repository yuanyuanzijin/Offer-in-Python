## 题目描述:输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
## 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。 (注意: 在返回值的list中，数组长度大的数组靠前)
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        self.result = []
        self.number = expectNumber
        self.Find(root)
        return sorted(self.result, key=lambda x: len(x), reverse=True)

    def Find(self, root, history=[]):
        d = history + [root.val]
        if not root.left and not root.right and sum(d) == self.number:
            self.result.append(d)
            return
        if root.left:
            self.Find(root.left, d)
        if root.right:
            self.Find(root.right, d)
