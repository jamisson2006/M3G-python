class Texture2D(Transformable):
    FILTER_BASE_LEVEL = 208
    FILTER_LINEAR = 209
    FILTER_NEAREST = 210
    FUNC_ADD = 224
    FUNC_BLEND = 225
    FUNC_DECAL = 226
    FUNC_MODULATE = 227
    FUNC_REPLACE = 228
    WRAP_CLAMP = 240
    WRAP_REPEAT = 241

    def __init__(self, handle=None, image=None):
        if handle is not None:
            super().__init__(handle)
        else:
            self.handle = self.create(image)
            Engine.addJavaPeer(self.handle, self)
            self.ii = self.__class__ != Texture2D
            Engine.addXOT(image)

    @staticmethod
    def create(image):
        # Esta função cria o Texture2D, equivalente ao método estático Java.
        # Implemente a lógica correspondente no Python.
        return Engine.createTexture2D(image)

    def getImage(self):
        return Engine.instantiateJavaPeer(self.getImageImpl())

    def setImage(self, image):
        self.setImageImpl(image)
        Engine.addXOT(image)

    def getBlending(self):
        return self.getBlendingImpl()

    def getBlendColor(self):
        return self.getBlendColorImpl()

    def getImageFilter(self):
        return self.getImageFilterImpl()

    def getLevelFilter(self):
        return self.getLevelFilterImpl()

    def setBlending(self, blending):
        self.setBlendingImpl(blending)

    def setBlendColor(self, blend_color):
        self.setBlendColorImpl(blend_color)

    def getWrappingS(self):
        return self.getWrappingSImpl()

    def getWrappingT(self):
        return self.getWrappingTImpl()

    def setWrapping(self, s, t):
        self.setWrappingImpl(s, t)

    def setFiltering(self, min_filter, mag_filter):
        self.setFilteringImpl(min_filter, mag_filter)

    # Métodos nativos em Java são agora métodos que invocam funções equivalentes em Python ou usam bindings.
    def finalize(self):
        pass  # Em Python, o garbage collector se encarrega do gerenciamento de memória.

    def getImageImpl(self):
        return Engine.getImageImpl(self.handle)

    def setImageImpl(self, image):
        Engine.setImageImpl(self.handle, image)

    def getBlendingImpl(self):
        return Engine.getBlending(self.handle)

    def getBlendColorImpl(self):
        return Engine.getBlendColor(self.handle)

    def getImageFilterImpl(self):
        return Engine.getImageFilter(self.handle)

    def getLevelFilterImpl(self):
        return Engine.getLevelFilter(self.handle)

    def setBlendingImpl(self, blending):
        Engine.setBlending(self.handle, blending)

    def setBlendColorImpl(self, blend_color):
        Engine.setBlendColor(self.handle, blend_color)

    def getWrappingSImpl(self):
        return Engine.getWrappingS(self.handle)

    def getWrappingTImpl(self):
        return Engine.getWrappingT(self.handle)

    def setWrappingImpl(self, s, t):
        Engine.setWrapping(self.handle, s, t)

    def setFilteringImpl(self, min_filter, mag_filter):
        Engine.setFiltering(self.handle, min_filter, mag_filter)
