class Sprite3D(Node):
    def __init__(self, handle=None, scaled=False, image=None, appearance=None):
        if handle is not None:
            super().__init__(handle)
        else:
            self.handle = self.create(scaled, image, appearance)
            Engine.addJavaPeer(self.handle, self)
            self.ii = self.__class__ != Sprite3D
            Engine.addXOT(image)
            Engine.addXOT(appearance)

    @staticmethod
    def create(scaled, image, appearance):
        # Esta função cria o Sprite3D, equivalente ao método estático Java.
        # Implemente a lógica correspondente no Python.
        return Engine.createSprite3D(scaled, image, appearance)

    def getAppearance(self):
        return Engine.instantiateJavaPeer(self.getAppearanceImpl())

    def getImage(self):
        return Engine.instantiateJavaPeer(self.getImageImpl())

    def setAppearance(self, appearance):
        self.setAppearanceImpl(appearance)
        Engine.addXOT(appearance)

    def setImage(self, image):
        self.setImageImpl(image)
        Engine.addXOT(image)

    def getCropHeight(self):
        return self.getCropHeightImpl()

    def getCropWidth(self):
        return self.getCropWidthImpl()

    def getCropX(self):
        return self.getCropXImpl()

    def getCropY(self):
        return self.getCropYImpl()

    def isScaled(self):
        return self.isScaledImpl()

    def setCrop(self, x, y, width, height):
        self.setCropImpl(x, y, width, height)

    # Métodos nativos em Java são agora métodos que invocam funções equivalentes em Python ou usam bindings.
    def finalize(self):
        pass  # Em Python, o garbage collector se encarrega do gerenciamento de memória.

    def getAppearanceImpl(self):
        return Engine.getAppearanceImpl(self.handle)

    def getImageImpl(self):
        return Engine.getImageImpl(self.handle)

    def setAppearanceImpl(self, appearance):
        Engine.setAppearanceImpl(self.handle, appearance)

    def setImageImpl(self, image):
        Engine.setImageImpl(self.handle, image)

    def getCropHeightImpl(self):
        return Engine.getCropHeight(self.handle)

    def getCropWidthImpl(self):
        return Engine.getCropWidth(self.handle)

    def getCropXImpl(self):
        return Engine.getCropX(self.handle)

    def getCropYImpl(self):
        return Engine.getCropY(self.handle)

    def isScaledImpl(self):
        return Engine.isScaled(self.handle)

    def setCropImpl(self, x, y, width, height):
        Engine.setCrop(self.handle, x, y, width, height)
