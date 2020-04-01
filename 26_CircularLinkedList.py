class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.last = None

    # This function is only for empty list
    def add_to_empty(self, data):

        if self.last is not None:
            return self.last

        # Creating the newnode temp
        temp = Node(data)
        self.last = temp

        # Creating the link
        self.last.next = self.last
        return self.last

    def add_begin(self, data):

        if self.last is None:
            return self.add_to_empty(data)

        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp

        return self.last

    def add_end(self, data):

        if self.last is None:
            return self.add_to_empty(data)

        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp

        return self.last

    def add_after(self, data, item):

        if self.last is None:
            return None

        temp = Node(data)
        p = self.last.next
        while p:
            if p.data == item:
                temp.next = p.next
                p.next = temp

                if p == self.last:
                    self.last = temp
                    return self.last
                else:
                    return self.last
            p = p.next
            if p == self.last.next:
                print(item, "not present in the list")
                break

    def traverse(self):
        if self.last is None:
            print("List is empty! =(")
            return

        temp = self.last.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.last.next:
                break


# Driver Code
if __name__ == '__main__':
    llist = CircularLinkedList()

    llist.traverse()

    llist.add_to_empty(0)
    llist.add_begin(1)
    llist.add_begin(2)
    llist.add_end(88)
    llist.add_end(120)
    llist.add_after(100, 88)
    llist.traverse()
