# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        intsum = self.ll_to_int(l1) + self.ll_to_int(l2)
        return self.convert_to_ListNode(str(intsum)[::-1])

    @classmethod
    def ll_to_int(cls, l: Optional[ListNode]) -> int:
        return int("".join(cls.ll_to_str_gen(l))[::-1])

    @staticmethod
    def convert_to_ListNode(l: str) -> Optional[ListNode]:
        current = to_return = ListNode()
        for i in l:
            current.next = ListNode(val=i)
            current = current.next
        return to_return.next

    @staticmethod
    def ll_to_str_gen(l):
        yield str(l.val)
        while l:=l.next:
            yield str(l.val)
