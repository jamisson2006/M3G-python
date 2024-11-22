class Transformable(Object3D):
    def __init__(self, handle=None):
        if handle:
            super().__init__(handle)
        else:
            super().__init__()

    def get_translation(self, array_of_float):
        # Implementar o método nativo getTranslation
        pass

    def get_scale(self, array_of_float):
        # Implementar o método nativo getScale
        pass

    def get_orientation(self, array_of_float):
        # Implementar o método nativo getOrientation
        pass

    def set_translation(self, float1, float2, float3):
        # Implementar o método nativo setTranslation
        pass

    def set_scale(self, float1, float2, float3):
        # Implementar o método nativo setScale
        pass

    def set_orientation(self, float1, float2, float3, float4):
        # Implementar o método nativo setOrientation
        pass

    def translate(self, float1, float2, float3):
        # Implementar o método nativo translate
        pass

    def scale(self, float1, float2, float3):
        # Implementar o método nativo scale
        pass

    def pre_rotate(self, float1, float2, float3, float4):
        # Implementar o método nativo preRotate
        pass

    def post_rotate(self, float1, float2, float3, float4):
        # Implementar o método nativo postRotate
        pass

    def get_transform(self, transform):
        # Implementar o método nativo getTransform
        pass

    def get_composite_transform(self, transform):
        # Implementar o método nativo getCompositeTransform
        pass

    def set_transform(self, transform):
        # Implementar o método nativo setTransform
        pass
