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
    
    def insertAtEnd(self, data):
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

    def insertAtStart(self, data):
        newNode = Node()
        newNode.setData(data)
        if not self.length:
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            newNode.setNext(self.head)
            self.head.setPrev(newNode)
            if self.length == 1:
                self.tail = self.head
                self.tail.setPrev(self.head)
            self.head = newNode
            self.length += 1
    
    def insertAtPosition(self, position, data):
        if position > self.length:
            raise IndexError()
        elif position-1 == 0:
            self.insertAtStart(data)
        elif position == self.length:
            self.insertAtEnd(data)
        else:
            newNode = Node()
            newNode.setData(data)
            currentNode = self.head
            for i in range(position-2):
                currentNode = currentNode.getNext()
            newNode.setPrev(currentNode)
            newNode.setNext(currentNode.getNext())
            currentNode.setNext(newNode)
            nextNode = currentNode.getNext()
            nextNode.setPrev(newNode)
            self.length +=1

    def deleteAtBeginning(self):
        newHead = self.head.getNext()
        newHead.setPrev(None)
        self.head = newHead
        self.length -= 1

    def deleteAtEnd(self):
        newTail = self.tail.getPrev()
        prevPrevTail = newTail.getPrev()
        newTail.setNext(None)
        newTail.setPrev(prevPrevTail)
        self.length -= 1

    def deleteValue(self, data):
        currentNode = self.head
        if currentNode.data == data:
            self.deleteAtBeginning()
        while currentNode.next:
            if currentNode.data == data:
                prevNode = currentNode.getPrev()
                nextNode = currentNode.getNext()
                prevNode.setNext(nextNode)
                nextNode.setPrev(prevNode)
                currentNode = None
                self.length -= 1
                return
            currentNode = currentNode.getNext()
        raise Exception('data not found')


if __name__ == '__main__':
    linked_list = DoublyLinkedList()
    linked_list.insertAtStart(0)
    linked_list.insertAtStart(1)
    linked_list.insertAtStart(2)
    linked_list.insertAtStart(3)
    linked_list.insertAtStart(4)
    linked_list.insertAtStart(5)
    linked_list.deleteValue(5)

    print(linked_list)
    print(linked_list.length)