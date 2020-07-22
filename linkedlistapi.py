class LinkedList(object):
    '''
    A linked list implementation that holds arbitrary objects.
    '''

    def __init__(self):
        '''Creates a linked list.'''
        self.head = None
        self.size = 0


    def debug_print(self):
        '''Prints a representation of the entire list.'''
        print('{} >>> {}'.format(self.size, ', '.join([ str(item) for item in self ])))


    def __iter__(self):
        '''Iterates through the linked list, implemented as a generator.'''
        for node in self._iter_nodes():
            yield node.value


    def _iter_nodes(self):
        '''Iterates through the nodes of the list, implemented as a generator.'''
        current = self.head
        while current != None:
            yield current
            current = current.next


    def _get_node(self, index):
        '''Retrieves the Node object at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''

    def add(self, item):
        '''Adds an item to the end of the linked list.'''
        n = Node(item)
        if self.size == 0:
            self.head = n
            self.size = self.size + 1
            return
        for i in self._iter_nodes():
            if i.next == None:
                i.next = n
                self.size = self.size + 1
                return

    # def insert(self, index, item):
    #     '''Inserts an item at the given index, shifting remaining items right.'''
    #     if self.size < index:
    #         print('Error: Out of bounds')
    #         return True
    #     if index == 0:
    #         x = self.head
    #         self.head = n
    #         self.head.next = x
    #         while x.next is not None:
    #             x = x.next
    #         self.size += 1
    #         return
    #     counter = 0
    #     n = Node(item)
    #     for i in self._iter_nodes():
    #         if counter == index-1:
    #             x = i.next
    #             i.next = n
    #             n.next = x
    #             self.size += 1
    #             while x.next is not None:
    #                 x = x.next
    #             return
    #         counter += 1

    def set(self, index, item):
        '''Sets the given item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if self.size < index:
            print('Error: Out of bounds')
            return True
        if index == 0:
            self.head.value = item
            return
        counter = 0
        for i in self._iter_nodes():
            if counter == index:
                i.value = item
                return            
            counter += 1

    def get(self, index):
        '''Retrieves the item at the given index.  Throws an exception if the index is not within the bounds of the linked list.'''
        if index == 0:
            return self.head.value
        counter = 0
        for i in self._iter_nodes():
            if counter == index:
                return i.value
            counter += 1

    def delete(self, index):
        '''Deletes the item at the given index. Throws an exception if the index is not within the bounds of the linked list.'''
        if self.size < index:
            print('Error: Out of bounds')
            return True
        if index == 0:
            x = self.head.next
            self.head = x
            while x.next is not None:
                x = x.next
            self.size -= 1
            return
        counter = 0
        x = Node(None)
        for i in self._iter_nodes():
            if counter == index:
                x = i
            counter += 1
        counter = 0
        for i in self._iter_nodes():
            if counter == index-1:
                i.next = x.next
                while x.next is not None:
                    x = x.next
                self.size -= 1
                return
            counter += 1

    def swap(self, index1, index2):
        '''Swaps the values at the given indices.'''
        if self.size < index1 or self.size < index2:
            print('Error: Out of bounds')
            return True
        if index1 == 0:
            v1 = self.head.value
            v2 = self.get(index2)
        elif index2 == 0:
            v2 = self.head.value
            v1 = self.get(index1)
        else:
            v1 = self.get(index1)
            v2 = self.get(index2)
        self.set(index1,v2)
        self.set(index2,v1)



######################################################
###   A node in the linked list

class Node(object):
    '''A node on the linked list'''

    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return '<Node: {}>'.format(self.value)