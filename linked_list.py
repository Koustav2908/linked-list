class UnderflowError(Exception):
    """Exception raised when an operation is attempted but the linked list is empty."""

    pass


class OutOfRangeError(Exception):
    """Exception raised at an attempt to access an index which is out of range in the linked list."""

    pass


class Node:
    """
    A node in the singly linked list.

    Attributes:
        value: The data stored in the node.
        next: A reference to the next node.
    """

    def __init__(self, value):
        """
        Innitialize a new node with a given value.

        Args:
            value: The data to store in the node.
        """

        self.value = value
        self.next = None


class LinkedList:
    """
    A class that manages the creation, deletion, and printing a single linked list.

    Attributes:
        head: The first node of the list.
        nodes_count: The total number of nodes present in the list.
    """

    def __init__(self):
        """Innitialize and empty list."""
        self.head = None
        self.nodes_count = 0

    def add(self, value):
        """
        Add a node at the end of the list.

        Args:
            value: The data to be added to the list.
        """

        if self.head is None:
            self.head = Node(value)

        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = Node(value)
        self.nodes_count += 1

    def print_list(self):
        """
        Print all the elements in the list.

        Raises:
            UnderflowError: If the list is empty.
        """

        if self.head is None:
            raise UnderflowError("Underflow - Linked list empty.")

        else:
            temp = self.head

            print("The elements of the linked list are:")

            while temp is not None:
                print(temp.value, "->", end=" ")
                temp = temp.next

            print("NULL")

    def delete(self, n):
        """
        Delete a node from a given position (1-based indexing) from the list.

        Args:
            n: The position of the node to delete.

        Raises:
            UnderflowError: If the list is empty.
            OutOfRangeError: If the index is out of valid range.
        """

        if self.head is None:
            raise UnderflowError("Underflow - Linked list empty.")

        elif n <= 0 or n > self.nodes_count:
            raise OutOfRangeError(
                f"Invalid index {n}. Valid range is 1 to {self.nodes_count}."
            )

        elif n == 1:
            print(f"{self.head.value} deleted from the list.")
            self.head = self.head.next
            self.nodes_count -= 1

        else:
            temp = self.head

            for _ in range(n - 2):
                temp = temp.next

            print(f"{temp.next.value} deleted from the list.")
            temp.next = (temp.next).next
            self.nodes_count -= 1
