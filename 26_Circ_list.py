class Element:
    def __init__(self, value, link):
        self.value = value
        self.link = link

    def __str__(self):
        return f'Value {self.value} --> link {self.link}'


class LinkedList:
    def __init__(self, data):
        self.data = data

    def insert_at_end(self, value):
        if len(self.data) == 0:
            self.data.append(Element(value, None))
        else:
            self.data[-1].link = value
            self.data.append(Element(value, None))

    def insert_at_head(self, value):
        if len(self.data) == 0:
            self.data.append(Element(value, None))
        else:
            self.data.insert(0, Element(value, self.data[0].value))

    def delete(self, index):
        self.data[index - 1].link = self.data[index].link
        del self.data[index]

    def delete_head(self):
        del self.data[0]

    def search(self, index):
        return self.data[index]

    def is_empty(self):
        return not bool(len(self.data))

    def __str__(self):
        return str([str(el) for el in self.data])


# my_list = LinkedList([])
#
# my_list.insert_at_end(1)
# print(my_list)
# my_list.insert_at_head(3)
# print(my_list)
# my_list.insert_at_end(4)
# print(my_list)
# my_list.delete(1)
# print(my_list)
# my_list.delete_head()
# print(my_list)


class BipolarElement:
    def __init__(self, prev_link, value, next_link):
        self.prev_link = prev_link
        self.value = value
        self.next_link = next_link

    def __str__(self):
        return f'Prev link {self.prev_link} value {self.value} next link {self.next_link}'


class BipolarLinkedList:
    def __init__(self, data):
        self.data = data

    def insert_at_end(self, value):
        if not len(self.data):
            self.data.append(BipolarElement(None, value, None))
        else:
            self.data[-1].next_link = value
            self.data.append(BipolarElement(self.data[-1].value, value, None))

    def insert_at_head(self, value):
        if not len(self.data):
            self.data.append(BipolarElement(None, value, None))
        else:
            self.data[0].prev_link = value
            self.data.insert(0, BipolarElement(None, value, self.data[0].value))

    def delete(self, index):
        self.data[index - 1].next_link = self.data[index].next_link
        self.data[index + 1].prev_link = self.data[index].prev_link
        del self.data[index]

    def delete_head(self):
        del self.data[0]
        self.data[0].prev_link = None

    def search(self, index):
        return self.data[index]

    def is_empty(self):
        return not bool(len(self.data))

    def __str__(self):
        return str([str(el) for el in self.data])


my_list = BipolarLinkedList([])

my_list.insert_at_end(1)
print(my_list)
my_list.insert_at_head(3)
print(my_list)
my_list.insert_at_end(4)
print(my_list)
my_list.delete(1)
print(my_list)
my_list.delete_head()
print(my_list)


# Circular linkedlist
