## 题目描述：输入一个链表，反转链表后，输出新链表的表头。
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        pPre = pHead
        pNext = pHead.next
        pHead.next = None
        while pNext:
            pHead = pNext
            pNext = pHead.next
            pHead.next = pPre
            pPre = pHead
        return pHead
