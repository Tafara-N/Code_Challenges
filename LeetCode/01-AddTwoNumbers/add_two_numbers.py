#!/usr/bin/python3

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

	def addTwoNumbers(l1, l2):
    dummy_head = ListNode(0)
    p, q, curr = l1, l2, dummy_head
    carry = 0
    while p is not None or q is not None:
        x = p.val if p is not None else 0
        y = q.val if q is not None else 0
        sum = carry + x + y
        carry = sum // 10
        curr.next = ListNode(sum % 10)
        curr = curr.next
        if p is not None: p = p.next
        if q is not None: q = q.next
    if carry > 0:
        curr.next = ListNode(carry)
    return dummy_head.next
