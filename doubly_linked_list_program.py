# Assessment 3.2 - Linear Data Structure: DOUBLY LINKED LIST
# Name: Salazar, Ralph L. | BSIT-2B


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None    # link to the previous node
        self.next = None    # link to the next node


class DoublyLinkedList:
    def __init__(self):
        # Step 1: head = NULL, tail = NULL
        self.head = None
        self.tail = None

    def insert_at_tail(self, data):
        # The tail pointer lets us append without traversing the list
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"Inserted '{data}' | forward: {self.forward()}")

    def delete_at_head(self):
        # Move head to the next node and fix the new head's prev link
        if self.head is None:
            print("List is empty!")
            return
        removed = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None             # list became empty
        else:
            self.head.prev = None
        removed.next = None              # fully unlink the removed node
        print(f"Deleted  '{removed.data}' | forward: {self.forward()}")

    def forward(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        return "NULL <-> " + " <-> ".join(parts + ["NULL"]) if parts else "NULL"

    def backward(self):
        parts = []
        current = self.tail
        while current is not None:
            parts.append(str(current.data))
            current = current.prev
        return " <-> ".join(parts) if parts else "NULL"


def main():
    last_name = input("Enter your last name: ").strip().upper()
    if not last_name:
        print("No input given.")
        return

    print("Letters to process:", " - ".join(last_name))
    dll = DoublyLinkedList()

    print("\n--- Insertion Phase ---")
    for ch in last_name:
        dll.insert_at_tail(ch)

    print("\nTraversing backward (tail -> head):", dll.backward())

    print("\n--- Deletion Phase (press Enter to delete each node) ---")
    while dll.head is not None:
        input("\nPress Enter to delete the head node...")
        dll.delete_at_head()

    print("\nDoubly linked list is now empty (head = NULL, tail = NULL).")


if __name__ == "__main__":
    main()