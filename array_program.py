# Assessment 3.2 - Linear Data Structure: ARRAY
# Name: Salazar, Ralph L. | BSIT-2B


class ArrayStructure:
    def __init__(self, capacity):
        # Step 1: empty array of fixed capacity, size counter = 0
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0

    def insert(self, item):
        # Store the item at the current size index, then increment size
        if self.size == self.capacity:
            print("Array is full!")
            return
        self.data[self.size] = item
        self.size += 1
        print(f"Inserted '{item}' at index {self.size - 1}  | size = {self.size}")

    def delete(self):
        # Decrement size; the element is removed from the logical view
        if self.size == 0:
            print("Array is empty!")
            return
        self.size -= 1
        print(f"Deleted  '{self.data[self.size]}' from index {self.size} | size = {self.size}")

    def display(self):
        print("Array view:", self.data[:self.size])


def main():
    last_name = input("Enter your last name: ").strip().upper()
    if not last_name:
        print("No input given.")
        return

    print("Letters to process:", " - ".join(last_name))
    arr = ArrayStructure(len(last_name))   # capacity adjusts to the name

    print("\n--- Insertion Phase ---")
    for ch in last_name:
        arr.insert(ch)
        arr.display()

    print("\n--- Deletion Phase (press Enter to delete each letter) ---")
    while arr.size > 0:
        input("\nPress Enter to delete the next letter...")
        arr.delete()
        arr.display()

    print("\nArray is now empty.")


if __name__ == "__main__":
    main()