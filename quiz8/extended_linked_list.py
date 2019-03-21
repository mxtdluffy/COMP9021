# Written by Di Peng for COMP9021

from linked_list_adt import *

class ExtendedLinkedList(LinkedList):
    def __init__(self, L = None):
        super().__init__(L)

    def rearrange(self, step):
        node = self.head 
        record = step
        original_node = self.head
        # move the node to the last node
        for i in range(len(self) - 2):
            node = node.next_node
        # connect the last new_node to the head
        new_node = node.next_node
        new_node.next_node = self.head
        # move to the position of Sth 
        for i in range(step - 2):
            original_node = original_node.next_node
        self.head = original_node.next_node
        node = self.head
        original_node.next_node = self.head.next_node
        original_node = self.head
        '''
        linkedlist_length = len(self)
        node = self.head
        end_node = node
        while end_node.next_node:
            end_node = end_node.next_node
        print('end_node:', end_node.value)

        head = node
        for i in range(step - 1):
            head = head.next_node
        self.head = head
        print('node:', node.value)
        
        print('self.head:', self.head.value)
        new_node = self.head
        for _ in range(linkedlist_length):
            for _ in range(step):
                if not head:
                    head = node
                print('head:', head.value)
                head = head.next_node
            new_node.next_node = head
            new_node = new_node.next_node
            print('new_node:', new_node.value)
        '''
        #######################
        '''
        linkedlist_length = len(self)
        record = step
        original_node = self.head
        new_node = original_node
        record_node = original_node

        head = original_node
        for i in range(step - 2):
            head = head.next_node
        new_node.next_node = head.next_node
            
        for _ in range(step):
            record_node.next_node = head.next_node
            record_node = head
            print('1 record_node:', record_node.value)
            print()
            while record_node:
                for _ in range(step-1):
                    record_node = record_node.next_node
                    if not record_node:
                        break
                    print('2 record_node:', record_node.value)
                if not record_node:
                    break
                print('new_node:', new_node.value)
                new_node.next_node = record_node.next_node
                new_node = new_node.next_node
                print('new_node:', new_node.value)
            head.next_node = original_node.next_node
            head = original_node
            print('head:', head.value)
            for i in range(record - 1):
                head = head.next_node
            record -= 1
            
        self.head = new_node
        '''
        ###########################
        '''
        new_list = list()
        new_node = Node()
        record = step
        while record > 0:
            original_node = self.head
            for _ in range(record-1):
                original_node = original_node.next_node
            new_node = original_node
            new_node.next_node = None
            new_list.append(new_node)
            for _ in range(step):
                original_node = original_node.next_node
            new_node = original_node
            new_node.next_node = None
            new_list.append(new_node)
            record -= 1

        new_linkedlist = ExtendedLinkedList()
        new_linkedlist.head = new_list.pop()
        new_node = new_linkedlist.head
        for i in range(len(new_list)):
            new_node.next_node = new_list.pop()
            new_node = new_node.next_node

        self.head = new_node
        '''
        ################
        while step > 1:
            record = step
            while record > 1:
                node = node.next_node
                if node is new_node:
                    step -= 1
                record -= 1
            # remove the selected node
            original_node.next_node = node.next_node
            node.next_node = node.next_node.next_node
            node = original_node.next_node
            original_node = original_node.next_node
        new_node.next_node = None
