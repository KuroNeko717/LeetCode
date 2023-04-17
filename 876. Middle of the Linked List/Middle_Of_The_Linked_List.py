# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        dummy_head = head
        while dummy_head is not None:
            count+=1
            dummy_head=dummy_head.next
        for x in range(count//2):
            head=head.next
        return head