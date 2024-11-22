class Appearance(Object3D):
    def __init__(self, handle=None):
        if handle:
            super().__init__(handle)
        else:
            self.handle = self.create()
            Engine.add_java_peer(self.handle, self)
            self.ii = self.__class__ != Appearance

    def get_material(self):
        return Engine.instantiate_java_peer(self.get_material_impl())

    def get_fog(self):
        return Engine.instantiate_java_peer(self.get_fog_impl())

    def get_compositing_mode(self):
        return Engine.instantiate_java_peer(self.get_compositing_mode_impl())

    def get_polygon_mode(self):
        return Engine.instantiate_java_peer(self.get_polygon_mode_impl())

    def set_material(self, material):
        self.set_material_impl(material)
        Engine.add_xot(material)

    def set_fog(self, fog):
        self.set_fog_impl(fog)
        Engine.add_xot(fog)

    def set_compositing_mode(self, compositing_mode):
        self.set_compositing_mode_impl(compositing_mode)
        Engine.add_xot(compositing_mode)

    def set_polygon_mode(self, polygon_mode):
        self.set_polygon_mode_impl(polygon_mode)
        Engine.add_xot(polygon_mode)

    def get_texture(self, index):
        return Engine.instantiate_java_peer(self.get_texture_impl(index))

    def set_texture(self, index, texture):
        self.set_texture_impl(index, texture)
        Engine.add_xot(texture)

    def create(self):
        return self.create_appearance()

    def get_layer(self):
        return self.get_layer_impl()

    def set_layer(self, layer):
        self.set_layer_impl(layer)

    def finalize(self):
        pass

    # Native methods
    def create_appearance(self):
        return Engine.native_create_appearance()

    def get_material_impl(self):
        return Engine.native_get_material(self.handle)

    def get_fog_impl(self):
        return Engine.native_get_fog(self.handle)

    def get_compositing_mode_impl(self):
        return Engine.native_get_compositing_mode(self.handle)

    def get_polygon_mode_impl(self):
        return Engine.native_get_polygon_mode(self.handle)

    def set_material_impl(self, material):
        return Engine.native_set_material(self.handle, material)

    def set_fog_impl(self, fog):
        return Engine.native_set_fog(self.handle, fog)

    def set_compositing_mode_impl(self, compositing_mode):
        return Engine.native_set_compositing_mode(self.handle, compositing_mode)

    def set_polygon_mode_impl(self, polygon_mode):
        return Engine.native_set_polygon_mode(self.handle, polygon_mode)

    def get_texture_impl(self, index):
        return Engine.native_get_texture(self.handle, index)

    def set_texture_impl(self, index, texture):
        return Engine.native_set_texture(self.handle, index, texture)

    def get_layer_impl(self):
        return Engine.native_get_layer(self.handle)

    def set_layer_impl(self, layer):
        return Engine.native_set_layer(self.handle, layer)
