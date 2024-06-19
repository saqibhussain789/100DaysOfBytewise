class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    # Find the middle of the linked list
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # Reverse the second half of the linked list
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # Check if the first half and the reversed second half are the same
    left, right = head, prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True

# Helper function to create linked list from list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Function to take input from user and create linked list
def input_linked_list():
    elements = input("Enter the elements of the linked list separated by spaces: ")
    arr = list(map(int, elements.split()))
    return create_linked_list(arr)

# Take input from user and test the function
linked_list = input_linked_list()
if is_palindrome(linked_list):
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
