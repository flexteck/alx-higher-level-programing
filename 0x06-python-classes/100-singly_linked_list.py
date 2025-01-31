#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """retrieve the data value"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets value for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve value for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set it's value"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        """return a string rep. of the list, one node per line"""
        nodes = []
        current = self.__head

        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)
    
    def sorted_insert(self, value):
        """Insert a new node in the sorted position (increasing order)"""
        new_node = Node(value)

        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head

            while current.next_node is not  None and current.next_node.data < new_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

