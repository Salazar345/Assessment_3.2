# Assessment 3.2 - Linear Data Structure: SINGLY LINKED LIST
# Name: Salazar, Ralph L. | BSIT-2B


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        # Step 1: head = NULL
        self.head = None

    def insert_at_tail(self, data):
        # Create a new node and traverse to the tail to append it
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        print(f"Inserted '{data}' | list: {self.to_string()}")

    def delete_at_head(self):
        # head = head.next ; the old head becomes unlinked
        if self.head is None:
            print("List is empty!")
            return
        removed = self.head
        self.head = self.head.next
        removed.next = None          # fully unlink the removed node
        print(f"Deleted  '{removed.data}' | list: {self.to_string()}")

    def to_string(self):
        parts = []
        current = self.head
        while current is not None:
            parts.append(str(current.data))
            current = current.next
        return " -> ".join(parts + ["NULL"])


def main():
    last_name = input("Enter your last name: ").strip().upper()
    if not last_name:
        print("No input given.")
        return

    print("Letters to process:", " - ".join(last_name))
    sll = SinglyLinkedList()

    print("\n--- Insertion Phase ---")
    for ch in last_name:
        sll.insert_at_tail(ch)

    print("\n--- Deletion Phase (press Enter to delete each node) ---")
    while sll.head is not None:
        input("\nPress Enter to delete the head node...")
        sll.delete_at_head()

    print("\nLinked list is now empty (head = NULL).")


if __name__ == "__main__":
    main()