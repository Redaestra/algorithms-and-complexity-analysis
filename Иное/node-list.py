class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class OneLinkedList:
    def __init__(self):
        self.head = None 

    def add_end(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def add_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        
    def del_end(self):
        current = self.head
        prev = None
        while current.next:
            prev = current
            current = current.next
        prev.next = None
        return current.value
    
    def del_start(self):
        head = self.head
        new_head = head.next
        self.head = new_head
        return head.value
    
    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values) if values else "Пустой список"
            
            
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