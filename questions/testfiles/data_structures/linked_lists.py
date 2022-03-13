class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SinglyLinkedList:
    def __init__(self,):
        self.head = None

    def create_list(self, arr):
        self.head = ListNode(val=arr[0])
        curr = self.head
        for idx in range(1, len(arr)):
            curr.next = ListNode(arr[idx])
            curr = curr.next
        return self.head

    def linked_list_to_arr(self, linked_list):
        arr = []
        curr = linked_list
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr


