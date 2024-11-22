class Background(Object3D):
    BORDER = 32
    REPEAT = 33
    
    def __init__(self, handle=None):
        if handle is None:
            self.handle = self.create()
            Engine.addJavaPeer(self.handle, self)
            self.ii = (self.__class__ != Background)
        else:
            super().__init__(handle)

    def get_image(self):
        return Engine.instantiateJavaPeer(self.get_image_impl())
    
    def set_image(self, image):
        self.set_image_impl(image)
        Engine.addXOT(image)
    
    def finalize(self):
        pass  # Implement finalize logic if needed
    
    @staticmethod
    def create():
        return Background.create_native()
    
    def get_color(self):
        return self.get_color_native()
    
    def get_image_mode_x(self):
        return self.get_image_mode_x_native()
    
    def get_image_mode_y(self):
        return self.get_image_mode_y_native()
    
    def get_crop_x(self):
        return self.get_crop_x_native()
    
    def get_crop_y(self):
        return self.get_crop_y_native()
    
    def get_crop_width(self):
        return self.get_crop_width_native()
    
    def get_crop_height(self):
        return self.get_crop_height_native()
    
    def is_color_clear_enabled(self):
        return self.is_color_clear_enabled_native()
    
    def is_depth_clear_enabled(self):
        return self.is_depth_clear_enabled_native()
    
    def set_color(self, color):
        self.set_color_native(color)
    
    def set_color_clear_enable(self, enable):
        self.set_color_clear_enable_native(enable)
    
    def set_depth_clear_enable(self, enable):
        self.set_depth_clear_enable_native(enable)
    
    def set_image_mode(self, mode_x, mode_y):
        self.set_image_mode_native(mode_x, mode_y)
    
    def set_crop(self, x, y, width, height):
        self.set_crop_native(x, y, width, height)

    # Native methods
    def create_native(self):
        pass  # Implement the native method for creating Background instance
    
    def get_image_impl(self):
        pass  # Implement the native method for getting the image
    
    def set_image_impl(self, image):
        pass  # Implement the native method for setting the image
    
    def get_color_native(self):
        pass  # Implement the native method to get the color
    
    def get_image_mode_x_native(self):
        pass  # Implement the native method to get image mode X
    
    def get_image_mode_y_native(self):
        pass  # Implement the native method to get image mode Y
    
    def get_crop_x_native(self):
        pass  # Implement the native method to get crop X
    
    def get_crop_y_native(self):
        pass  # Implement the native method to get crop Y
    
    def get_crop_width_native(self):
        pass  # Implement the native method to get crop width
    
    def get_crop_height_native(self):
        pass  # Implement the native method to get crop height
    
    def is_color_clear_enabled_native(self):
        pass  # Implement the native method to check if color clear is enabled
    
    def is_depth_clear_enabled_native(self):
        pass  # Implement the native method to check if depth clear is enabled
    
    def set_color_native(self, color):
        pass  # Implement the native method to set color
    
    def set_color_clear_enable_native(self, enable):
        pass  # Implement the native method to enable color clear
    
    def set_depth_clear_enable_native(self, enable):
        pass  # Implement the native method to enable depth clear
    
    def set_image_mode_native(self, mode_x, mode_y):
        pass  # Implement the native method to set image mode
    
    def set_crop_native(self, x, y, width, height):
        pass  # Implement the native method to set crop
