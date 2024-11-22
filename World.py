class World(Group):
    def __init__(self, handle=None):
        if handle:
            super().__init__(handle)
        else:
            self.handle = self.create()
            Engine.addJavaPeer(self.handle, self)
            self.ii = (self.__class__ != World)
    
    def get_active_camera(self):
        return Engine.instantiateJavaPeer(self.get_active_camera_impl())
    
    def get_background(self):
        return Engine.instantiateJavaPeer(self.get_background_impl())
    
    def set_active_camera(self, active_camera):
        self.set_active_camera_impl(active_camera)
        Engine.addXOT(active_camera)
    
    def set_background(self, background):
        self.set_background_impl(background)
        Engine.addXOT(background)

    def finalize(self):
        pass  # Finalize in Python is typically managed by garbage collection

    @staticmethod
    def create():
        return 1  # Placeholder for the actual creation logic

    def get_active_camera_impl(self):
        # Call the appropriate native method or simulation
        return 1

    def get_background_impl(self):
        # Call the appropriate native method or simulation
        return 1

    def set_active_camera_impl(self, camera):
        # Implement the setting of active camera
        pass

    def set_background_impl(self, background):
        # Implement the setting of background
        pass
