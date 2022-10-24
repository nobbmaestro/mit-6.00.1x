"""Final Exam, Problem 7.

Implement the class myDict with the methods below, which will represent a dictionary without using a dictionary object.
The methods you implement below should have the same behavior as a dict object, including raising appropriate
exceptions. Your code does not have to be efficient. Any code that uses a Python dictionary object will receive 0.

For example:
  With a dict:       With a myDict:
  -------------------------------------------------------------------------------
  d = {}             md = myDict()        # initialize a new object using
                                            your choice of implementation

  d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

  print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

  del(d[1])          md.delete(1)         # use delete method to remove
                                            key,value pair associated with key 1
"""


# pylint: disable=C0103
class myDict:
    """Implements a dictionary without using a dictionary."""

    def __init__(self):
        """Initialize of myDict."""
        self.key = []
        self.value = []

    def __str__(self):
        """Str method."""
        if self.key == "" and self.value == "":
            return '{}'

        string = ""
        for i in range(len(self.key)):
            string += (str(self.key[i]) + ": " + str(self.value[i]))
            if i != len(self.key) - 1:
                string += ", "
        return '{' + string + '}'

    def assign(self, k, v):
        """Assign value.

        Args:
            k (any): the key
            v (any): the value
        """
        if k in self.key:
            for i in range(len(self.key)):
                if self.key[i] == k:
                    self.value[i] = v
        else:
            self.key.append(k)
            self.value.append(v)

    def getval(self, k):
        """Return value at index.

        Args:
            k (key): key value
        """
        try:
            for i in range(len(self.key)):
                if self.key[i] == k:
                    return self.value[i]
            raise KeyError('successfully raised')

        except TypeError:
            return self.value

    def delete(self, k):
        """Delete value at index.

        Args:
            k (key): key value
        """
        for i in range(len(self.key)):
            if self.key[i] == k:
                self.key.remove(k)
                self.value.remove(self.value[i])
                return None

        raise KeyError('successfully raised')
