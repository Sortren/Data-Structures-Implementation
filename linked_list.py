class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self) -> None:
        self.length = 0
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.length += 1
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next

            last_node.next = new_node
            self.length += 1

    def pop(self) -> int:
        if self.length > 1:
            one_before_last = None
            last_node = self.head

            while last_node.next is not None:
                one_before_last = last_node
                last_node = last_node.next

            one_before_last.next = None
            self.length -= 1
            return last_node
        else:
            tmp = self.head
            self.head = None
            self.length -= 1
            return tmp

    def print(self):
        if self.length > 0:
            last_node = self.head

            print("[", end="")
            while last_node.next is not None:
                print(last_node, end=", ")
                last_node = last_node.next
            print(last_node, end="]")
        else:
            print("The list is empty")

    def __len__(self):
        return self.length
