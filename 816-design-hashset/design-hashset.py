class MyHashSet(object):

    def __init__(self):
        self.temp = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key not in self.temp:
            self.temp.append(key)
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.temp:
            self.temp.remove(key)
        

    def contains(self, key):
        """
        :type key: int
        :rtype: bool
        """
        return key in self.temp