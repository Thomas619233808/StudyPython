# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        # 终止条件：当前为空 or 下一个为空
        if not head or not head.next:
            return head
        # 从最后一个节点开始
        cur = self.reverseList(head.next)
        # 此时cur为最后一个节点，head.next 指向cur
        # 将cur.nxet指向head，则完成翻转
        head.next.next = head
        # 防止行程环路，head.next为空
        head.next = None
        return cur

    # 双指针写法
    def reverseList2(self, head):
        # 申请两个指针
        pre = None
        cur = head
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 当前节点指向前一个节点
            cur.next = pre
            # pre和cur 都往前一位
            pre = cur
            cur = tmp
        return pre

