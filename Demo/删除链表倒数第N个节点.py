class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dunmy = ListNode(0)
        dunmy.next = head
        slow = fast = dunmy
        # 先走n+1步，在之后快慢指针同时前进且快指针到末尾的时候，慢指针指向倒数第n+1处
        # 指向倒数第n+1处只需要更新该指针的next就可以达到删除目的  
        for _ in range(n + 1):
            fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dunmy.next

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
cur = head
print('原链表')
while cur:
    print(cur.val, end='->')
    cur = cur.next

solution = Solution()
newhead = solution.removeNthFromEnd(head, 2)
print('\n删除后')
while newhead:
    print(newhead.val, end='->')
    newhead = newhead.next
