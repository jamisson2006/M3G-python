class Node(Transformable):
    NONE = 144
    ORIGIN = 145
    X_AXIS = 146
    Y_AXIS = 147
    Z_AXIS = 148
    
    def __init__(self, handle=None):
        if handle is not None:
            super().__init__(handle)

    def get_parent(self):
        return Engine.instantiate_java_peer(self.get_parent_impl())
    
    def get_parent_impl(self):
        # Implementação nativa a ser definida
        pass

    def get_alpha_factor(self):
        return self.native_get_alpha_factor()

    def native_get_alpha_factor(self):
        # Implementação nativa a ser definida
        pass

    def is_rendering_enabled(self):
        return self.native_is_rendering_enabled()

    def native_is_rendering_enabled(self):
        # Implementação nativa a ser definida
        pass

    def is_picking_enabled(self):
        return self.native_is_picking_enabled()

    def native_is_picking_enabled(self):
        # Implementação nativa a ser definida
        pass

    def get_scope(self):
        return self.native_get_scope()

    def native_get_scope(self):
        # Implementação nativa a ser definida
        pass

    def set_alpha_factor(self, value):
        self.native_set_alpha_factor(value)

    def native_set_alpha_factor(self, value):
        # Implementação nativa a ser definida
        pass

    def set_rendering_enable(self, enable):
        self.native_set_rendering_enable(enable)

    def native_set_rendering_enable(self, enable):
        # Implementação nativa a ser definida
        pass

    def set_picking_enable(self, enable):
        self.native_set_picking_enable(enable)

    def native_set_picking_enable(self, enable):
        # Implementação nativa a ser definida
        pass

    def set_scope(self, value):
        self.native_set_scope(value)

    def native_set_scope(self, value):
        # Implementação nativa a ser definida
        pass

    def get_transform_to(self, node, transform):
        return self.native_get_transform_to(node, transform)

    def native_get_transform_to(self, node, transform):
        # Implementação nativa a ser definida
        pass

    def set_alignment(self, z_reference, z_target, y_reference, y_target):
        self.set_alignment_impl(z_reference, z_target, y_reference, y_target)
        Engine.add_xot(z_reference)
        Engine.add_xot(y_reference)

    def set_alignment_impl(self, z_reference, z_target, y_reference, y_target):
        # Implementação nativa a ser definida
        pass

    def get_alignment_target(self, value):
        return self.native_get_alignment_target(value)

    def native_get_alignment_target(self, value):
        # Implementação nativa a ser definida
        pass

    def get_alignment_reference(self, axis):
        return Engine.instantiate_java_peer(self.get_alignment_reference_impl(axis))

    def get_alignment_reference_impl(self, axis):
        # Implementação nativa a ser definida
        pass

    def align(self, node):
        self.native_align(node)

    def native_align(self, node):
        # Implementação nativa a ser definida
        pass
