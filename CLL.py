"""
FelipedelosH

Circular Linked List
"""

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.pivot = None


    def addData(self, data):
        new_node = Node(data)
        if self.pivot == None:
            self.pivot = new_node
            self.pivot.next = self.pivot
        else:
            _copy = self.pivot

            while _copy.next != self.pivot:
                _copy = _copy.next

            _copy.next = new_node
            new_node.next = self.pivot


    def getData(self, index):
        if self.pivot == None:
            return None
        
        _copy = self.pivot
        _counter = 0
        while _counter < index:
            _copy = _copy.next
            _counter = _counter + 1

        return _copy.data
    


    def isDataInList(self, data):
        if self.pivot == None:
            return False
        
        _copy = self.pivot

        while _copy.next != self.pivot:
            if _copy.data == data:
                return True

            _copy = _copy.next

        return False
    

    def updateValue(self, index, data):
        _count = self.count()

        if index >= 0 and index < _count:
            _copy = self.pivot
            _counter = 0
            while _counter < index:
                _copy = _copy.next
                _counter = _counter + 1

            # UPDATE
            _copy.data =  data


    def deleteValue(self, data):
        if self.pivot != None:
            _copy = self.pivot
            
            # Case 0: the data is in a head
            if _copy.data == data:
                # The list only have single element
                if _copy.next == self.pivot:
                    self.pivot = None
                # The list have more elements
                else:
                    while _copy.next != self.pivot:
                        _copy = _copy.next

                    self.pivot = self.pivot.next
                    _copy.next = _copy.next.next
            # Case 1: the data it'nt in a heath
            else:
                _previous = None
                while _copy.next != self.pivot:
                    _previous = _copy
                    _copy = _copy.next

                    if _copy.data == data:
                        _previous.next = _copy.next


    def count(self):
        if self.pivot == None:
            return 0
        
        _counter = 1
        _copy = self.pivot

        while _copy.next != self.pivot:
            _counter = _counter + 1
            _copy = _copy.next

        return _counter
    

    def converDataInArray(self):
        data = []

        if self.pivot != None:
            _copy = self.pivot
            while True:
                data.append(_copy.data)
                _copy = _copy.next

                if _copy == self.pivot:
                    break

        return data

    def showAllData(self):
        if self.pivot != None:
            _copy = self.pivot
            while True:
                print(_copy.data)
                _copy = _copy.next

                if _copy == self.pivot:
                    break

    def isEmpty(self):
        return self.pivot == None
