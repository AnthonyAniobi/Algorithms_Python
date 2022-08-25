class Node:
    def __init__(self) -> None:
        self.data = None
        self.next = None
    
    def setData(self, data):
        self.data = data
    def getData(self):
        return self.data
    def setNext(self, next):
        self.next = next
    def getNext(self):
        return self.next
    def hasNext(self)->bool:
        return self.next != None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.length = 0

    def __str__(self) -> str:
        if self.length == 0:
            return '[]'
        else:
            elements = []
            tempNode = self.head
            elements.append(tempNode.data)
            while tempNode.hasNext():
                tempNode = tempNode.getNext()
                elements.append(tempNode.data)
            return f'{elements}'
    
    def insertAtBeginning(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
            self.length = 1
        else:
            newNode.setNext(self.head)
            self.head = newNode
            self.length += 1
    
    def insertAtEnd(self, data):
        newNode = Node()
        newNode.setData(data)
        if self.length == 0:
            self.head = newNode
            self.length = 1
        else:
            current = self.head
            while current.hasNext():
                current = current.getNext()
            current.setNext(newNode)
            self.length +=1
    
    def insertAtPosition(self, position, data):
        newNode = Node()
        newNode.setData(data)
        current = self.head
        if position == 0:
            raise IndexError()
        if position == 1:
            self.insertAtBeginning(data)
            return       
        for x in range(position-2):
            if not current.hasNext():
                raise IndexError()
            current = current.getNext()
        newNode.setNext(current.getNext())
        current.setNext(newNode)
        self.length +=1

    def deleteFromBeginning(self):
        if self.length == 0:
            raise Exception('Can\'t delete from an empty list')
        if self.length == 0:
            self.head == None
            self.length = 0
        else:
            nextNode = self.head.getNext()
            self.head = nextNode
            self.length -= 1   

    def deleteAtEnd(self):
        if self.length == 0:
            raise Exception('Can\'t delete from an empty list')
        if self.length == 0:
            self.head == None
            self.length = 0
        else:
            prevNode = self.head
            nextNode = prevNode.getNext()
            while nextNode.hasNext():
                prevNode = nextNode
                nextNode = nextNode.getNext()
            prevNode.setNext(None)
            self.length -= 1

    def deleteValue(self, value):
        if self.length == 0:
            raise Exception('Can\'t delete from am empty list')
        current = self.head
        if current.data == value:
            self.deleteFromBeginning()
            return
        previous = Node()
        while current.getData:
            if current.data == value:
                if current.hasNext():
                    previous.setNext(current.getNext())
                else:
                    current = None
                    previous.setNext(None)
                self.length -=1
                return
            previous = current
            current = current.getNext()
    
    def clear(self):
        self.length = 0
        self.head = None



if __name__ == '__main__':
    linked_list = SinglyLinkedList()
    linked_list.insertAtEnd(20)
    linked_list.insertAtEnd(30)
    linked_list.insertAtEnd(40)
    linked_list.insertAtEnd(50)
    linked_list.insertAtEnd(60)
    linked_list.insertAtEnd(70)
    linked_list.insertAtEnd(80)
    linked_list.deleteValue(80)
    linked_list.clear()

    print(linked_list)
    print(linked_list.length)