# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # easy to set dummy, i guess it saves from declaring in loop
        dummy = ListNode()
        tail = dummy

        # also note how when we are assigning the value from the lists
        # we only have to use the list name as the assigner, and no val or next
        while list1 and list2:
            # if value in list 1 is bigger than list 2, have our tail node
            # point to that node
            # then navigtate to next element in respective list
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next # this is how we go to next ll element

            else:
                tail.next = list2 
                list2 = list2.next # this is how we go to next ll element
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next
