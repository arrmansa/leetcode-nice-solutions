# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from itertools import chain

def ListNode__iter__(l):
    yield l.val
    while (l:=l.next) is not None:
        yield l.val

setattr(ListNode, "__iter__", ListNode__iter__)

def convert_to_ListNode_reverse(l: list) -> Optional[ListNode]:
    current = None
    for i in l:
        current = ListNode(val=i, next=current)
    return current

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists:
            return convert_to_ListNode_reverse(sorted(chain(*(l for l in lists if l is not None)), reverse=True))
