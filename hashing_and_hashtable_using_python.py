# Implement the hashing algorithm and hash table abstract data type


class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def put(self, key, value):
        hash_value = self.hash_function(key, self.size)
        if self.keys[hash_value] is None:
            self.keys[hash_value] = key
            self.values[hash_value] = value
        else:
            next_hash_value = self.rehash_function(hash_value, self.size)
            while self.keys[next_hash_value] is not None and \
                    self.keys[next_hash_value] != key:
                next_hash_value = self.rehash_function(next_hash_value, self.size)
            if self.keys[next_hash_value] is None:
                self.keys[next_hash_value] = key
                self.values[next_hash_value] = value
            else:
                self.values[next_hash_value] = value

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        if self.keys[hash_value] == key:
            return self.values[hash_value]
        else:
            next_hash_value = self.rehash_function(hash_value, self.size)
            while self.keys[next_hash_value] is not None and \
                    self.keys[next_hash_value] != key:
                next_hash_value = self.rehash_function(next_hash_value, self.size)

            if self.keys[next_hash_value] == key:
                return self.values[next_hash_value]
            else:
                return "Not found"

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash_function(old_hash, size):
        return (old_hash + 1) % size

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(H.keys, H.values)

print("Running the get method")
print(H[20])
print(H[44])
print(H[69])
