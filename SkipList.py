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
    def __init__(self, max_levels):
        """Constructor for a SkipList.
        
            Parameters:
            max_levels (int): Maximum number of levels the SkipList can have.
            """
        self.head = Node(None, max_levels)
        self.levels = 1
        self.max_levels = max_levels
    
    def contains(self, value):
        """Searches for a value in the SkipList.
        
            Parameters:
            value (Obj): Object to be searched for.
            
            Returns:
            (bool): Whether the object was found in the SkipList."""
        current_node = self.head 

        for i in range(self.levels - 1, -1, -1):
            while current_node.next[i] != None:
                if current_node.next[i].value > value:
                    break # Goes a level down
                if current_node.next[i].value == value:
                    return True
                current_node = current_node.next[i]
        return False
    
    def remove(self, value):
        """Searches for a value in the SkipList, and removes it
            if found.
        
            Parameters:
            value (Obj): Object to be removed.
            
            Returns:
            (bool): Whether the object was removed in the SkipList."""
        current_node = self.head
        found = False

        for i in range(self.levels - 1, -1, -1):
            while current_node.next[i] != None:
                if current_node.next[i].value == value:
                    found = True
                    current_node.next[i] = current_node.next[i].next[i]
                    break
                if current_node.next[i].value > value:
                    break # Goes a level down 

                current_node = current_node.next[i]
        return found
    
    def insert(self, value):
        """Creates a new node with value and random level access and then inserts it into the SkipList
            
            Parameters:
            value (Obj): Value to be inserted into the SkipList.
            
            Returns:
            (bool): Whether the object was inserted into the SkipList."""
        level = 0
        inserted = False
        
        while randint(0, 1) == 1 and level < self.max_levels:
            level += 1

            if level == self.levels and self.levels < self.max_levels:
                self.levels += 1
                break

        new_node = Node(value, level + 1)
        current_node = self.head

        for i in range(self.levels - 1, -1, -1):
            while current_node.next[i] != None:
                if current_node.next[i].value > value:
                    break # Goes down a level
                current_node = current_node.next[i]

            if i <= level and current_node.value != new_node.value:
                new_node.next[i] = current_node.next[i]
                current_node.next[i] = new_node
                inserted = True
                
        return inserted

    def display(self):
        """Prints the SkipList in a readable format."""
        nodes = []
        curNode = self.head.next[0]
        
        while curNode != None:
            value = curNode.value
            current_node_stack = [value if i < len(curNode.next) else " " * len(str(curNode.value)) for i in range(self.levels)]

            nodes.append(current_node_stack)
            curNode = curNode.next[0]

        for i in range(self.levels - 1, -1, -1):
            for j in range(len(nodes)):
                print(nodes[j][i], end=" ")
            print()
