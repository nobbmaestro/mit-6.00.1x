"""Person."""


# pylint: disable=C0103
class Person:
    """Person Class."""

    def __init__(self, name):
        """Initialize Person."""
        self.name = name
        try:
            firstBlank = name.rindex(' ')
            self.lastName = name[firstBlank + 1:]

        except ValueError:
            self.lastName = name

        self.age = None

    def getLastName(self):
        """Return last name."""
        return self.lastName

    def setAge(self, age):
        """Set age."""
        self.age = age

    def getAge(self):
        """Return age."""
        if self.age is None:
            raise ValueError
        return self.age

    def __lt__(self, other):
        """Lt method."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """Str method."""
        return self.name
