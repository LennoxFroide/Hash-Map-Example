array = [2,3,4,5,6,7]

map = dict()
for idx in range(len(array)):
    if array[idx] not in map:
        map[array[idx]] = idx

"""-----*------*------*-------*------*-------*--------*--------*-------*--------*-------*-------*--------"""
class HashMap:
    # We need the blueprint for our map which is a python dictionary
    def __init__(self):
        self.mapper = dict()

    # Insert: O(1) time | O(1) space
    def put(self,key,value) -> None:
        """This method takes a key,value pair and adds them to the hash map
        """
        # Inserting the key,value pair for the first time
        if key not in self.mapper:
            self.mapper[key] = value
        else:
            # If the key,value pair is already in the list, we update the value
            self.mapper[key] = self.mapper[key] + value

        

    # Search O(1) time | O(1) space
    def search(self,key) -> int:
        if key in self.mapper:
            return (self.mapper[key] - 1)
        else:
            return -1

    # Delete O(1) time | O(1) space
    def delete(self, key) -> None:
        if key in self.mapper:
            del self.mapper[key]
        else:
            return "The key-value pair is not in the linked list!"

    # Print
    def printMap(self) -> list:
        return self.mapper
        
print(map)

# print(map[2])

# Instance of our class
myHash = HashMap()
# Inserting a key value pair into our map
myHash.put(1,1)
myHash.put(2,1)
myHash.put(3,1)
myHash.put(4,1)
myHash.put(4,2)
print(f'The hash map before the delete call: {myHash.printMap()}')
myHash.delete(4)
print(f'The hash map after the delete call: {myHash.printMap()}')
