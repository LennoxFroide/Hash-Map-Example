# A class to show the structure of our node
class Node:
    """Each node will have a field to store data and link to next node"""
    def __init__(self,value):
        self.value = value
        self.next = None

# A class to host all linked list functions
class LinkedList:
    """We only have a pointer to the head node"""
    def __init__(self):
        self.head = None

    # Insert method: O(n) time | O(1) space
    def insert(self,node):
        """This method takes a node and inserts it at the end of a linked list
        """
        #Checking if our list is empty and setting the head node
        if self.head is None:
            self.head = node
            return
        else:
            # We need a pointer to iterate the entire length of the list from head to last node
            currentNode = self.head
            # Iterating through list and inserting at tail position
            while currentNode.next:
                # Keep looping to the tail
                currentNode = currentNode.next
            # Once we hit the tail, we insert
            currentNode.next = node

    # Print method: O(n) time | 0(1) space
    def printList(self):
        """This method prints out all of the elements in a linked list
        """
        # If list is empty we print that we have an empty list
        if self.head == None:
            print("The linked list is empty!!!")
            return
        # We have more nodes in the list thus we need to iterate its entire length
        else:
            currentNode = self.head
            # As long as we have more node
            counter = 1
            while currentNode.next:
                print(f'Node {counter} ->{currentNode.value}')
                currentNode = currentNode.next
                counter += 1


# Creating an instance of our linked list class
linkedList = LinkedList()
# Creating nodes to insert into our first linked list
node1 = Node(10)
node2 = Node(11)
node3 = Node(12)
node4 = Node(13)
node5 = Node(14)
node6 = Node(15)
# Ask for input from user to determine the length of list
# Create a set number of nodes depending on users input
# Inserting our nodes into the linked list
linkedList.insert(node1)
linkedList.insert(node2)
linkedList.insert(node3)
linkedList.insert(node4)
linkedList.insert(node5)
linkedList.insert(node6)

"--*----*-----*------*------*------*------*------*------*-------*------*------*-------*-------*-----*-----*------*------"
# Creating a second linked list
linkedList2 = LinkedList()
# Creating nodes to insert into our second linked list
node7 = Node(20)
node8 = Node(21)
node9 = Node(22)
node10 = Node(23)
node11 = Node(24)
node12 = Node(25)
# Inserting nodes into the second linked list
linkedList2.insert(node7)
linkedList2.insert(node8)
linkedList2.insert(node9)
linkedList2.insert(node10)
linkedList2.insert(node11)
linkedList2.insert(node12)

"--*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----*-----"
# Creating a third linked list
linkedList3 = LinkedList()
# Creating nodes to insert into our third linked list
node13 = Node(30)
node14 = Node(31)
node15 = Node(32)
node16 = Node(33)
node17 = Node(34)
node18 = Node(35)
# Inserting nodes into our third linked list
linkedList3.insert(node13)
linkedList3.insert(node14)
linkedList3.insert(node15)
linkedList3.insert(node16)
linkedList3.insert(node17)
linkedList3.insert(node18)


# Drive code to ensure that we only call this when its the main and not an imported module
if __name__ == '__main__':
    # Printing our linked list
    # if linkedList:
    print('This is the first linked list:')
    linkedList.printList()
    # elif linkedList2:
    print('This is the second linked list:')
    linkedList2.printList()
    # elif linkedList3:
    print('This is the third linked list:')
    linkedList3.printList()
        
