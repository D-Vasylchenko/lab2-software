class Character:
    def __init__(self, value: str):
        if len(value) != 1:
            raise ValueError("Value must be a single character")
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Character) and self.value == other.value

    def __str__(self):
        return self.value


class Node:
    def __init__(self, data: Character):
        self.data = data
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size + 1

    def append(self, element: Character) -> None:
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def insert(self, element: Character, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.size == 0:
                self.tail = new_node
        elif index == self.size:
            self.append(element)
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node
        self.size += 1

    def delete(self, index: int) -> Character:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            removed = self.head
            self.head = removed.next
            if self.head:
                self.head.prev = None
        elif index == self.size - 1:
            removed = self.tail
            self.tail = removed.prev
            if self.tail:
                self.tail.next = None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            removed = current
            removed.prev.next = removed.next
            if removed.next:
                removed.next.prev = removed.prev
        self.size -= 1
        return removed.data

    def deleteAll(self, element: Character) -> None:
        current = self.head
        while current:
            if current.data == element:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.size -= 1
            current = current.next

    def get(self, index: int) -> Character:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def clone(self) -> 'DoubleLinkedList':
        cloned_list = DoubleLinkedList()
        current = self.head
        while current:
            cloned_list.append(current.data)
            current = current.next
        return cloned_list

    def reverse(self) -> None:
        current = self.head
        prev = None
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def findFirst(self, element: Character) -> int:
        current = self.head
        index = 0
        while current:
            if current.data == element:
                return index
            current = current.next
            index += 1
        return -1

    def findLast(self, element: Character) -> int:
        current = self.tail
        index = self.size - 1
        while current:
            if current.data == element:
                return index
            current = current.prev
            index -= 1
        return -1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def extend(self, elements: list) -> None:
        for element in elements:
            self.append(element)

    def __str__(self) -> str:
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' <-> '.join(elements)


dll = DoubleLinkedList()

dll.append(Character('A'))
dll.append(Character('B'))
dll.append(Character('C'))

print(dll)

dll.insert(Character('D'), 2)
print(dll)

print(dll.delete(1))
print(dll)

dll.deleteAll(Character('D'))
print(dll)

print(dll.get(1))

dll.reverse()

print(dll.findFirst(Character('A')))
print(dll.findLast(Character('A')))

dll.clear()
print(dll)

dll.extend([Character('X'), Character('Y'), Character('Z')])
print(dll)
