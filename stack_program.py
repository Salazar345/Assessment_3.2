# Assessment 3.2 - Linear Data Structure: STACK (LIFO)
# Name: Salazar, Ralph L. | BSIT-2B


class Stack:
    def __init__(self):
        # Step 1: empty stack
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        # Place item on top of the stack
        self.items.append(item)
        print(f"Pushed '{item}'  | stack (bottom -> top): {self.items}")

    def pop(self):
        # Remove and return the top item
        if self.is_empty():
            print("Stack underflow!")
            return None
        item = self.items.pop()
        print(f"Popped '{item}'  | stack (bottom -> top): {self.items}")
        return item


def main():
    last_name = input("Enter your last name: ").strip().upper()
    if not last_name:
        print("No input given.")
        return

    print("Letters to process:", " - ".join(last_name))
    stack = Stack()

    print("\n--- Push Phase ---")
    for ch in last_name:
        stack.push(ch)

    print("\n--- Pop Phase (press Enter to pop each letter) ---")
    while not stack.is_empty():
        input("\nPress Enter to pop the top letter...")
        stack.pop()

    print("\nStack is now empty.")


if __name__ == "__main__":
    main()