class Key:
    def __init__(self, key):
        self.key = key

    def set_key(self, key):
        """Set the key value."""
        self.key = key

    def __hash__(self):
        """Return the hash value for the key."""
        return self.key

    def __eq__(self, other):
        """Check if two Key objects are equal based on their key values."""
        if isinstance(other, Key):
            return self.key == other.key
        return False

    def __str__(self):
        """Return the string representation of the key."""
        return str(self.key)
