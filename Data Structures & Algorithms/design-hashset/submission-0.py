class MyHashSet:

    def __init__(self):
        # Number of buckets
        self.size = 1000

        # Create empty buckets
        self.buckets = []
        for i in range(self.size):
            self.buckets.append([])

    def add(self, key: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]

        # Check if key already exists
        for value in bucket:
            if value == key:
                return  # already in set

        # Otherwise add it
        bucket.append(key)

    def remove(self, key: int) -> None:
        index = key % self.size
        bucket = self.buckets[index]

        # Look for the key and remove it
        for i in range(len(bucket)):
            if bucket[i] == key:
                bucket.pop(i)
                return

    def contains(self, key: int) -> bool:
        index = key % self.size
        bucket = self.buckets[index]

        for value in bucket:
            if value == key:
                return True

        return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)