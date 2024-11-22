class RayIntersection:
    def __init__(self, handle=None):
        if handle is None:
            self.swerveHandle = self.create()
            Engine.addJavaPeer(self.swerveHandle, self)
        else:
            self.swerveHandle = handle

    @staticmethod
    def create():
        # Simulating the native create() method
        return Engine.createRayIntersection()

    def finalize(self):
        # Simulating the native finalize() method
        pass

    def getDistance(self):
        return Engine.getDistance(self.swerveHandle)

    def getIntersected(self):
        return Engine.instantiateJavaPeer(self.getIntersectedImpl())

    def getIntersectedImpl(self):
        return Engine.getIntersectedImpl(self.swerveHandle)

    def getSubmeshIndex(self):
        return Engine.getSubmeshIndex(self.swerveHandle)

    def getNormalX(self):
        return Engine.getNormalX(self.swerveHandle)

    def getNormalY(self):
        return Engine.getNormalY(self.swerveHandle)

    def getNormalZ(self):
        return Engine.getNormalZ(self.swerveHandle)

    def getTextureS(self, paramInt):
        return Engine.getTextureS(self.swerveHandle, paramInt)

    def getTextureT(self, paramInt):
        return Engine.getTextureT(self.swerveHandle, paramInt)

    def getRay(self, paramArrayOffloat):
        Engine.getRay(self.swerveHandle, paramArrayOffloat)

    @staticmethod
    def cacheFID():
        Engine.cacheFID(RayIntersection)
