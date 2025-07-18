class MyHashSet(object):

    def __init__(self):
        self.temp = set([])

    def add(self, key):
        self.temp.add(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.temp.discard(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        if key not in self.temp:
            return False
        return True