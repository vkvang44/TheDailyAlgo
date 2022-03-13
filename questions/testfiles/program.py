# class for list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
   # write your code here
    prev = None
    while head:
       temp = head
       head = head.next
       temp.next = prev
       prev = temp
    return prev
       