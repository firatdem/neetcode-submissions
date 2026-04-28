class MyHashSet:

    def __init__(self):
        self.size = 10000
        self.buckets = []

        # Create empty buckets
        for i in range(self.size):
            self.buckets.append([])

    # Hash function
    def _hash(self, key):
        return key % self.size

    def add(self, key: int) -> None:
        h = self._hash(key)

        # Check if key already exists in that bucket
        for existing in self.buckets[h]:
            if existing == key:
                return      # already there → do nothing

        # Otherwise append
        self.buckets[h].append(key)

    def remove(self, key: int) -> None:
        h = self._hash(key)

        # Search only in the correct bucket
        bucket = self.buckets[h]

        for i in range(len(bucket)):
            if bucket[i] == key:
                # Delete by index
                del bucket[i]
                return

    def contains(self, key: int) -> bool:
        h = self._hash(key)

        for existing in self.buckets[h]:
            if existing == key:
                return True

        return False
