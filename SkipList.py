from random import randint, seed

class Node:
    def __init__(self, value, level):
        """Constructor for a node.
            
            Parameters:
            value (Obj): Value inside of node being constructed.
            level (int): Level where the node will be located."""
        self.value = value
        self.next = [None]*level # Generates an None list the size of the level.

class SkipList:
    def __init__(self, MAX_LEVELS):
        self.head = Node(None, MAX_LEVELS)
        self.levels = 1
        self.MAX_LEVELS = MAX_LEVELS
    
    def contains(self, value):
        """Searches for a value in the SkipList.
        
            Parameters:
            value (Obj): Object to be searched for.
            
            Returns:
            (bool): Whether the object was found in the SkipList."""
        curNode = self.head 

        for i in range(self.levels - 1, -1, -1):
            while curNode.next[i] != None:
                if curNode.next[i].value > value:
                    break # Goes a level down
                if curNode.next[i].value == value:
                    return True
                curNode = curNode.next[i]
        return False
    
    def remove(self, value):
        """Searches for a value in the SkipList, and removes it
            if found.
        
            Parameters:
            value (Obj): Object to be removed.
            
            Returns:
            (bool): Whether the object was removed in the SkipList."""
        curNode = self.head
        found = False

        for i in range(self.levels - 1, -1, -1):
            while curNode.next[i] != None:
                if curNode.next[i].value == value:
                    found = True
                    curNode.next[i] = curNode.next[i].next[i]
                    break
                if curNode.next[i].value > value:
                    break # Goes a level down 

                curNode = curNode.next[i]
        return found
    
    def insert(self, value):
        """Creates a new node with value and random level access and then inserts it into the SkipList
            
            Parameters:
            value (Obj): Value to be inserted into the SkipList."""
        level = 0
        
        while randint(0, 1) == 1 and level < self.MAX_LEVELS:
            level += 1

            if level == self.levels and self.levels < self.MAX_LEVELS:
                self.levels += 1
                break

        newNode = Node(value, level + 1)
        curNode = self.head

        for i in range(self.levels - 1, -1, -1):
            while curNode.next[i] != None:
                if curNode.next[i].value > value:
                    break # Goes down a level
                curNode = curNode.next[i]
            if i <= level:
                newNode.next[i] = curNode.next[i]
                curNode.next[i] = newNode

    def toString(self):
        #four lines below prints the skip list sideways and shows memory addresses that each space in next array points to
        node_nexts = self.head.next[0]
        while (node_nexts != None):
            print(f"{node_nexts.value}: {node_nexts.next}")
            node_nexts = node_nexts.next[0]


        # level_elements = []
        # curNode = self.head.next[0] # Points to base level
        # level_elements.append(curNode.next)

        # while curNode.next[0] != None:
        #     curNode = curNode.next[0]
        #     level_elements.append(curNode.next)

        # padded_level_elements = [lst + [None] * ((self.MAX_LEVELS) - len(lst)) for lst in level_elements]

        # for i in range(self.MAX_LEVELS - 1, -1, -1):
        #     for j in range(len(padded_level_elements)):
        #         currentNode = padded_level_elements[j][i]
        #         if currentNode == None:
        #             print(" ")
        #         else:
        #             print(currentNode.value, end="")
        #     print()
