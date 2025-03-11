class MyHashMap:

    def __init__(self): 
        self.values = [-1]*(10**6 + 1)
        
    def put(self, key: int, value: int) -> None:
        self.values[key] = value

    def get(self, key: int) -> int:
        return self.values[key]

    def remove(self, key: int) -> None:
        self.values[key] = -1

output = [None] 
myHashMap =  MyHashMap()
output.append(myHashMap.put(1, 1)) #The map is now [[1,1]]
output.append(myHashMap.put(2, 2)) # The map is now [[1,1], [2,2]]
output.append(myHashMap.get(1))    # return 1, The map is now [[1,1], [2,2]]
output.append(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
output.append(myHashMap.put(2, 1)) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
output.append(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
output.append(myHashMap.remove(2)) # remove the mapping for 2, The map is now [[1,1]]
output.append(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]

print(output)