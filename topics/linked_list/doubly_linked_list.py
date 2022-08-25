class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
        self.prev = None
    
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev
    
    def setData(self, data):
        self.data = data
    def setNext(self, next):
        self.next = next
    def setPrev(self, prev):
        self.prev = prev

    def __str__(self) -> str:
        return str(self.data)

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0
    
    def __str__(self) -> str:
        if self.length == 0:
            return '[]'
        else:
            elements = []
            tempNode = self.head
            elements.append(tempNode.data)
            while tempNode.getNext():
                tempNode = tempNode.getNext()
                elements.append(tempNode.data)
            return f'{elements}'
    
    def clear(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def append(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            if self.length==1:
                self.head.setNext(newNode)
                newNode.setPrev(self.head)
            else:
                self.tail.setNext(newNode)
                newNode.setPrev(self.tail)
            self.tail = newNode
            self.length +=1

if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.append(0)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)

    print(linked_list)
    print(linked_list.length)