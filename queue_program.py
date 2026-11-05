# Assessment 3.2 - Linear Data Structure: QUEUE (FIFO)
# Name: Salazar, Ralph L. | BSIT-2B


class Queue:
    def __init__(self, capacity):
        # Step 1: empty queue with front and rear pointers
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0      # index of the next item to leave
        self.rear = 0       # index where the next item will enter

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.rear == self.capacity

    def enqueue(self, item):
        # Insert item at the rear
        if self.is_full():
            print("Queue overflow!")
            return
        self.data[self.rear] = item
        self.rear += 1
        print(f"Enqueued '{item}' | front={self.front}, rear={self.rear} | "
              f"queue (front -> rear): {self.data[self.front:self.rear]}")

    def dequeue(self):
        # Remove item from the front
        if self.is_empty():
            print("Queue underflow!")
            return None
        item = self.data[self.front]
        self.data[self.front] = None
        self.front += 1
        print(f"Dequeued '{item}' | front={self.front}, rear={self.rear} | "
              f"queue (front -> rear): {self.data[self.front:self.rear]}")
        return item


def main():
    last_name = input("Enter your last name: ").strip().upper()
    if not last_name:
        print("No input given.")
        return

    print("Letters to process:", " - ".join(last_name))
    queue = Queue(len(last_name))

    print("\n--- Enqueue Phase ---")
    for ch in last_name:
        queue.enqueue(ch)

    print("\n--- Dequeue Phase (press Enter to dequeue each letter) ---")
    while not queue.is_empty():
        input("\nPress Enter to dequeue the front letter...")
        queue.dequeue()

    print("\nQueue is now empty.")


if __name__ == "__main__":
    main()