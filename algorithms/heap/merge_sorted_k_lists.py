"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""


from queue import PriorityQueue


# Definition for singly-linked list.
class ListNode(object):
    """ ListNode Class"""

    def __init__(self, val):
        self.val = val
        self.next = None

def merge_k_lists(lists, coverage_keys):
    """ Merge List """
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node:
            coverage_keys["is_node"] = True
            q.put((node.val, node))
    while not q.empty():
        curr.next = q.get()[1]  # These two lines seem to
        curr = curr.next  # be equivalent to :-   curr = q.get()[1]
        if curr.next:
            coverage_keys["next"] = True
            q.put((curr.next.val, curr.next))
    return dummy.next


"""
I think my code's complexity is also O(nlogk) and not using heap or priority queue,
n means the total elements and k means the size of list.

The mergeTwoLists function in my code comes from the problem Merge Two Sorted Lists
whose complexity obviously is O(n), n is the sum of length of l1 and l2.

To put it simpler, assume the k is 2^x, So the progress of combination is like a full binary tree,
from bottom to top. So on every level of tree, the combination complexity is n,
because every level have all n numbers without repetition.
The level of tree is x, ie log k. So the complexity is O(n log k).

for example, 8 ListNode, and the length of every ListNode is x1, x2,
x3, x4, x5, x6, x7, x8, total is n.

on level 3: x1+x2, x3+x4, x5+x6, x7+x8 sum: n

on level 2: x1+x2+x3+x4, x5+x6+x7+x8 sum: n

on level 1: x1+x2+x3+x4+x5+x6+x7+x8 sum: n
"""
