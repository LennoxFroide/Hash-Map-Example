from testlinked import linkedList, linkedList2, linkedList3

# Just to check that we have successfully imported the linked list
# linkedList.printList()

# Our base array to hold the 3 linked lists
baseArray = [None]*3
# Limiting the size of base array
print(f'Length of base array: {len(baseArray)}')

# Adding our linked lists to the base array
baseArray[0] = linkedList
baseArray[1] = linkedList2
baseArray[2] = linkedList3

# Adding our first linked list at 0th index
for idx in range(len(baseArray)):
    # Counter to see the idx of the printed linked list
    counter = idx
    if baseArray[idx] != None:
        print(f'This is the linked list at the {idx}th index of base array')
        # Printing our linked lists
        baseArray[idx].printList()
