# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        total = 0
        nb = 0
        car = 0
        res = []
        while (l1 or l2 or nb):
            v1 = l1.val if l1  else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + nb
            car = total % 10
            nb = total // 10
            if (l1):
                l1 = l1.next
            if (l2):
                l2 = l2.next
            res.append(car)
        node= ListNode() 
        l3 = node
        for i in range(len(res)):
            l3.next = ListNode(res[i])
            l3 = l3.next
        return node.next

