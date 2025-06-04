class Character:
    def __init__(self, value: str):
        if len(value) != 1:
            raise ValueError("Value must be a single character")
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Character) and self.value == other.value

    def __str__(self):
        return self.value


class DoubleLinkedList:
    def __init__(self):
        self.items = []

    def length(self) -> int:
        return len(self.items)

    def append(self, element: Character) -> None:
        self.items.append(element)

    def insert(self, element: Character, index: int) -> None:
        if index < 0 or index > len(self.items):
            raise IndexError("Index out of bounds")
        self.items.insert(index, element)

    def delete(self, index: int) -> Character:
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items.pop(index)

    def deleteAll(self, element: Character) -> None:
        self.items = [item for item in self.items if item != element]

    def get(self, index: int) -> Character:
        if index < 0 or index >= len(self.items):
            raise IndexError("Index out of bounds")
        return self.items[index]

    def clone(self) -> 'DoubleLinkedList':
        cloned_list = DoubleLinkedList()
        cloned_list.items = self.items[:]
        return cloned_list

    def reverse(self) -> None:
        self.items.reverse()

    def findFirst(self, element: Character) -> int:
        try:
            return self.items.index(element)
        except ValueError:
            return -1

    def findLast(self, element: Character) -> int:
        try:
            return len(self.items) - 1 - self.items[::-1].index(element)
        except ValueError:
            return -1

    def clear(self) -> None:
        self.items.clear()

    def extend(self, elements: list) -> None:
        self.items.extend(elements)

    def __str__(self) -> str:
        return ' <-> '.join(str(item) for item in self.items)


# Тестування методів
dll = DoubleLinkedList()

dll.append(Character('A'))
dll.append(Character('B'))
dll.append(Character('C'))
print(dll)  # A <-> B <-> C

dll.insert(Character('D'), 2)
print(dll)  # A <-> B <-> D <-> C

print(dll.delete(1))  # B
print(dll)  # A <-> D <-> C

dll.deleteAll(Character('D'))
print(dll)  # A <-> C

print(dll.get(1))  # C

cloned = dll.clone()
print(cloned)

dll.reverse()
print(dll)

print(dll.findFirst(Character('A')))
print(dll.findLast(Character('A')))

dll.clear()
print(dll)

dll.extend([Character('X'), Character('Y'), Character('Z')])
print(dll)

