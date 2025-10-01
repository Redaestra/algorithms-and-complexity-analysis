class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class OneLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_end(self, value):
        new_node = Node(value)
        if self.tail is None:  # список пуст
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def add_start(self, value):
        new_node = Node(value)
        if self.head is None:  # список пуст
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def del_end(self):
        if self.length == 0:
            raise IndexError("Удаление из пустого списка")
        to_return = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return to_return.value

    def del_start(self):
        if self.length == 0:
            raise IndexError("Удаление из пустого списка")
        to_return = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return to_return.value

    def get_by_index(self, index):
        if not (0 <= index < self.length):
            raise IndexError("Индекс вне диапазона")
        if index <= self.length // 2:
            current = self.head
            for i in range(index):
                current = current.next
        else:
            current = self.tail
            for i in range(self.length - 1, index, -1):
                current = current.prev
        return current.value

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Пустой список"

    def __len__(self):
        return self.length

            
# Tests:
lst = OneLinkedList()
print(lst)
lst.add_end(1)
lst.add_end(2)
lst.add_start(3)
lst.add_start(4)
print(lst)
print(f'удалил значение: {lst.del_end()}')
print(f'удалил значение: {lst.del_start()}')
print(lst)
print(lst.get_by_index(0))