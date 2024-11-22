class Light(Node):
    AMBIENT = 128
    DIRECTIONAL = 129
    OMNI = 130
    SPOT = 131

    def __init__(self):
        self.handle = self.create()
        super().__init__(self.handle)
        Engine.add_java_peer(self.handle, self)
        self.ii = self.__class__ != Light

    @staticmethod
    def create():
        """Native method to create a Light instance."""
        # This would be mapped to the actual native code call for 'create'
        return 1  # Placeholder for actual native call

    def get_mode(self):
        """Get the mode of the light."""
        return self._get_mode()

    def get_color(self):
        """Get the color of the light."""
        return self._get_color()

    def get_intensity(self):
        """Get the intensity of the light."""
        return self._get_intensity()

    def get_spot_angle(self):
        """Get the spot angle of the light (if applicable)."""
        return self._get_spot_angle()

    def get_spot_exponent(self):
        """Get the spot exponent of the light (if applicable)."""
        return self._get_spot_exponent()

    def get_constant_attenuation(self):
        """Get the constant attenuation of the light."""
        return self._get_constant_attenuation()

    def get_linear_attenuation(self):
        """Get the linear attenuation of the light."""
        return self._get_linear_attenuation()

    def get_quadratic_attenuation(self):
        """Get the quadratic attenuation of the light."""
        return self._get_quadratic_attenuation()

    def set_mode(self, mode):
        """Set the mode of the light."""
        self._set_mode(mode)

    def set_color(self, color):
        """Set the color of the light."""
        self._set_color(color)

    def set_intensity(self, intensity):
        """Set the intensity of the light."""
        self._set_intensity(intensity)

    def set_spot_angle(self, spot_angle):
        """Set the spot angle of the light (if applicable)."""
        self._set_spot_angle(spot_angle)

    def set_spot_exponent(self, spot_exponent):
        """Set the spot exponent of the light (if applicable)."""
        self._set_spot_exponent(spot_exponent)

    def set_attenuation(self, constant, linear, quadratic):
        """Set the attenuation parameters (constant, linear, quadratic)."""
        self._set_attenuation(constant, linear, quadratic)

    # Placeholder native methods
    def _get_mode(self): pass
    def _get_color(self): pass
    def _get_intensity(self): pass
    def _get_spot_angle(self): pass
    def _get_spot_exponent(self): pass
    def _get_constant_attenuation(self): pass
    def _get_linear_attenuation(self): pass
    def _get_quadratic_attenuation(self): pass
    def _set_mode(self, mode): pass
    def _set_color(self, color): pass
    def _set_intensity(self, intensity): pass
    def _set_spot_angle(self, spot_angle): pass
    def _set_spot_exponent(self, spot_exponent): pass
    def _set_attenuation(self, constant, linear, quadratic): pass
