class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def get(self, index):
        current = self.head
        for i in range(index):
            if current is None:
                raise IndexError("Index out of range.")
            current = current.next
        if current is None:
            raise IndexError("Index out of range.")
        return current.data

    def remove(self, index):
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    raise IndexError("Index out of range.")
                current = current.next
            if current.next is None:
                raise IndexError("Index out of range.")
            current.next = current.next.next

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        return ' '.join(str(item) for item in self)


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
