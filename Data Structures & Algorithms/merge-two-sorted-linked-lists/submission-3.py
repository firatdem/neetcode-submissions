# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # set up a dummy node and assign it to our tail
        # we will use tail to attach the list nodes given
        # our conditions

        dummy = ListNode()
        tail = dummy
        #print(list1.val) # this is the VALUE - important distinction to make
        #print(list1) # this is the ADDRESS

        while list1 and list2: # we have to toggle through linked list using while
            if list1.val < list2.val:
                tail.next = list1 # it is pointing to the ADDRESS, we are not appending
                                  # to a list
                list1 = list1.next # Then we go to the next value
            else:
                tail.next = list2
                list2 = list2.next
            
            # Need to move tail pointer over or we keep rewriting same pointer
            tail = tail.next
        
        # edge case of if either list not empty still
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        
        return dummy.next # This is how we return, not quite sure why conceptually
