class MyHashMap(object):

    def __init__(self):
        self.temp = dict({})

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.temp[key] = value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        return self.temp.get(key, -1)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.temp:
            del self.temp[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)