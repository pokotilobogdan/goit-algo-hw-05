﻿class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        
    def __str__(self):
        result = ''
        for pairs in self.table:
            result += str(pairs) + '\n'
        return result
    
    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        key_hash = self.hash_function(key)
        key_value = [key, value]

        if self.table[key_hash] is None:
            self.table[key_hash] = list([key_value])
            return True
        else:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.table[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.hash_function(key)
        if self.table[key_hash] is not None:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    self.table[key_hash].pop(self.table[key_hash].index(pair))
        return None


if __name__ == '__main__':
    H = HashTable(5)
    
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)

    # print(H.get("apple"))   # Виведе: 10
    # print(H.get("orange"))  # Виведе: 20
    # print(H.get("banana"))  # Виведе: 30
    
    print("Original HashTable:")
    print()
    print(H)
    print()
    print()
    
    print("Deleting orange...")
    print()
    
    H.delete("orange")
    print(H)
    print()
    
    print("Deleting apple...")
    print()
    
    H.delete("apple")
    print(H)
    print()
    
    print("Deleting banana...")
    print()
    
    H.delete("banana")
    print(H)
    print()
