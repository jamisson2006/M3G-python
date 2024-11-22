class KeyframeSequence(Object3D):
    LINEAR = 176
    SLERP = 177
    SPLINE = 178
    SQUAD = 179
    STEP = 180
    CONSTANT = 192
    LOOP = 193

    def __init__(self, num_keyframes, num_components, interpolation):
        self.handle = self.create(num_keyframes, num_components, interpolation)
        super().__init__(self.handle)
        Engine.add_java_peer(self.handle, self)
        self.ii = self.__class__ != KeyframeSequence

    @staticmethod
    def create(num_keyframes, num_components, interpolation):
        """Native method to create a KeyframeSequence."""
        # This would be mapped to the actual native code call for 'create'
        return 1  # Placeholder for actual native call

    def get_duration(self):
        """Get the duration of the KeyframeSequence."""
        return self._get_duration()

    def get_repeat_mode(self):
        """Get the repeat mode."""
        return self._get_repeat_mode()

    def get_keyframe_count(self):
        """Get the number of keyframes."""
        return self._get_keyframe_count()

    def get_component_count(self):
        """Get the number of components."""
        return self._get_component_count()

    def get_interpolation_type(self):
        """Get the interpolation type."""
        return self._get_interpolation_type()

    def get_valid_range_first(self):
        """Get the first valid range."""
        return self._get_valid_range_first()

    def get_valid_range_last(self):
        """Get the last valid range."""
        return self._get_valid_range_last()

    def set_duration(self, duration):
        """Set the duration of the KeyframeSequence."""
        self._set_duration(duration)

    def set_repeat_mode(self, repeat_mode):
        """Set the repeat mode."""
        self._set_repeat_mode(repeat_mode)

    def get_keyframe(self, index, array_of_floats):
        """Get a keyframe."""
        return self._get_keyframe(index, array_of_floats)

    def set_keyframe(self, index, component_count, array_of_floats):
        """Set a keyframe."""
        self._set_keyframe(index, component_count, array_of_floats)

    def set_valid_range(self, first, last):
        """Set the valid range."""
        self._set_valid_range(first, last)

    # Placeholder native methods
    def _get_duration(self): pass
    def _get_repeat_mode(self): pass
    def _get_keyframe_count(self): pass
    def _get_component_count(self): pass
    def _get_interpolation_type(self): pass
    def _get_valid_range_first(self): pass
    def _get_valid_range_last(self): pass
    def _set_duration(self, duration): pass
    def _set_repeat_mode(self, repeat_mode): pass
    def _get_keyframe(self, index, array_of_floats): pass
    def _set_keyframe(self, index, component_count, array_of_floats): pass
    def _set_valid_range(self, first, last): pass
