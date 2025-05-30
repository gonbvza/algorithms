from merge_sorted_k_lists import merge_k_lists
"""
This file is different to the find_path as this one uses linked lists
"""
class ListNode(object):
    """ ListNode Class"""

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

merge_list_coverage = {
    "is_node" : False, 
    "next": False
} 


def print_coverage(coverage_keys):
    for key, value in coverage_keys.items():
        print(f"The branch {key}: {value}")

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

def main():
    lists = [
        list_to_linked([1, 2, 3]),
        list_to_linked([4, 5, 6])
    ]
    
    print("Coverage for the function merge_sorted_k_lists")
    merge_k_lists(lists, merge_list_coverage);
    print_coverage(merge_list_coverage)

if __name__ == "__main__":
    main()
