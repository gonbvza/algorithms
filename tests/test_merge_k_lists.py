from algorithms.heap import merge_sorted_k_lists
import unittest

class ListNode(object):
    """ ListNode Class"""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def list_to_linked(lst):
    """
    Function to create a linked list from an array
    """
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for v in lst[1:]:
        current.next = ListNode(v)
        current = current.next
    return head 

def linked_to_list(node):
    """
    Function to create an array from a linked list
    """
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


class TestSinglePath(unittest.TestCase):
    def setUp(self):
        self.lists = [
            list_to_linked([1, 2, 3]),
            list_to_linked([4, 5, 6])
        ]

        self.graph_without_neighbours = {
            'A': [],
        }

    def test_merge_lists(self):
        merged_lists = merge_sorted_k_lists.merge_k_lists(self.lists)
        self.assertEqual([1, 2, 3, 4, 5, 6], linked_to_list(merged_lists))


