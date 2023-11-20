class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def is_cycle(head):
    slow = head
    fast = head
    has_cycle = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    # 判断环的入口
    if has_cycle:
        # 将慢指针移动到开头
        slow = head
        # 两个指针以相同速度移动，下次相遇的地方就是入口
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return True, slow.value
    else:
        return False, None

head = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node2
node5.next = None

res = list(is_cycle(head))
print(res)