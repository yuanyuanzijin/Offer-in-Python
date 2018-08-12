## 题目描述：输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        if pHead1.val <= pHead2.val:
            newHead = pHead1
            newHead.next = self.Merge(pHead1.next, pHead2)
        else:
            newHead = pHead2
            newHead.next = self.Merge(pHead1, pHead2.next)
        return newHead
