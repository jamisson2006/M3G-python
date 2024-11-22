class IndexBuffer(Object3D):
    def __init__(self, handle=None):
        if handle is not None:
            super().__init__(handle)
        else:
            super().__init__()

    def get_index_count(self):
        """Get the count of indices."""
        raise NotImplementedError("get_index_count method must be implemented by subclass")

    def get_index_count_impl(self):
        """Native method for getting index count."""
        # Implement the native functionality in a platform-specific way, or simulate with Python
        pass

    def get_indices(self, indices):
        """Fill the provided array with indices."""
        raise NotImplementedError("get_indices method must be implemented by subclass")

    def get_indices_impl(self, indices):
        """Native method for getting indices."""
        # Implement the native functionality in a platform-specific way, or simulate with Python
        pass
