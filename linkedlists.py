class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def data(self):
        return self.data

    def next(self):
        return self.next

    def setData(self,settingData):
        self.data = settingData

    def setNext(self,settingNext):
        self.next = settingNext

class LinkedList:

    def __init__(self):
        self.head = None

    def empty(self):
        return self.head == None

    def add(self,newItem):
        newItem = Node(newItem)
        newItem.setNext(self.head)
        self.head = newItem

    def breadth(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.next()

        return count

    def find(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.data() == item:
                found = True
            else:
                current = current.next()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data() == item:
                found = True
            else:
                previous = current
                current = current.next()

        if previous == None:
            self.head = current.next()
        else:
            previous.setNext(current.next())