import unittest
from main import Character, DoubleLinkedList


class TestDoublyLinkedList(unittest.TestCase):
    def test_length(self):
        dll = DoubleLinkedList()
        self.assertEqual(dll.length(), 0)
        dll.append(Character('A'))
        self.assertEqual(dll.length(), 1)
        dll.append(Character('B'))
        self.assertEqual(dll.length(), 2)

    def test_append(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        self.assertEqual(str(dll), "A <-> B")

    def test_insert(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.insert(Character('C'), 1)
        self.assertEqual(str(dll), "A <-> C <-> B")
        with self.assertRaises(IndexError):
            dll.insert(Character('D'), 5)

    def test_delete(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.append(Character('C'))
        self.assertEqual(dll.delete(1), Character('B'))
        self.assertEqual(str(dll), "A <-> C")
        with self.assertRaises(IndexError):
            dll.delete(5)

    def test_deleteAll(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.append(Character('A'))
        dll.deleteAll(Character('A'))
        self.assertEqual(str(dll), "B")

    def test_get(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        self.assertEqual(dll.get(1), Character('B'))
        with self.assertRaises(IndexError):
            dll.get(5)

    def test_clone(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        cloned = dll.clone()
        self.assertEqual(str(dll), str(cloned))
        dll.append(Character('C'))
        self.assertNotEqual(str(dll), str(cloned))

    def test_reverse(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.append(Character('C'))
        dll.reverse()
        self.assertEqual(str(dll), "C <-> B <-> A")

    def test_findFirst(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.append(Character('A'))
        self.assertEqual(dll.findFirst(Character('A')), 0)
        self.assertEqual(dll.findFirst(Character('B')), 1)
        self.assertEqual(dll.findFirst(Character('C')), -1)

    def test_findLast(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.append(Character('A'))
        self.assertEqual(dll.findLast(Character('A')), 2)
        self.assertEqual(dll.findLast(Character('B')), 1)
        self.assertEqual(dll.findLast(Character('C')), -1)

    def test_clear(self):
        dll = DoubleLinkedList()
        dll.append(Character('A'))
        dll.append(Character('B'))
        dll.clear()
        self.assertEqual(dll.length(), 0)

    def test_extend(self):
        dll1 = DoubleLinkedList()
        dll1.append(Character('A'))
        dll1.append(Character('B'))
        dll2 = [Character('C'), Character('D')]
        dll1.extend(dll2)
        self.assertEqual(str(dll1), "A <-> B <-> C <-> D")


if __name__ == "__main__":
    unittest.main()
