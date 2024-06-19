class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

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

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=' -> ' if current.next else '')
        current = current.next
    print()

# Function to take input from user and test the linked list reversal
def user_input_linked_list():
    arr = list(map(int, input("Enter the elements of the linked list separated by spaces: ").split()))
    linked_list = create_linked_list(arr)
    print("Original linked list:")
    print_linked_list(linked_list)
    reversed_list = reverse_linked_list(linked_list)
    print("Reversed linked list:")
    print_linked_list(reversed_list)

# Take input from user and test the function
user_input_linked_list()
