class SkinnedMesh(Mesh):
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            super().__init__(args[0])  # Calling the superclass constructor
        elif len(args) == 4 and all(isinstance(arg, (VertexBuffer, IndexBuffer, Appearance, Group)) for arg in args):
            self.swerveHandle = self.createMultiSubmesh(args[0], Engine.getJavaPeerArrayHandles(args[1:3]), Engine.getJavaPeerArrayHandles([args[3]]), args[3])
            Engine.addJavaPeer(self.swerveHandle, self)
            self.ii = (self.__class__ != SkinnedMesh)
            Engine.addXOT(args[0])
            Engine.addXOT(args[1])
            Engine.addXOT(args[2])
            Engine.addXOT(args[3])
        elif len(args) == 4 and isinstance(args[1], IndexBuffer):
            self.swerveHandle = self.createSingleSubmesh(args[0], args[1], args[2], args[3])
            Engine.addJavaPeer(self.swerveHandle, self)
            self.ii = (self.__class__ != SkinnedMesh)
            Engine.addXOT(args[0])
            Engine.addXOT(args[1])
            Engine.addXOT(args[2])
            Engine.addXOT(args[3])

    @staticmethod
    def createMultiSubmesh(vertices, submeshes, appearances, skeleton):
        return Engine.createMultiSubmesh(vertices, submeshes, appearances, skeleton)

    @staticmethod
    def createSingleSubmesh(vertices, submesh, appearance, skeleton):
        return Engine.createSingleSubmesh(vertices, submesh, appearance, skeleton)

    def finalize(self):
        pass

    def getSkeleton(self):
        return Engine.instantiateJavaPeer(self.getSkeletonImpl())

    def getSkeletonImpl(self):
        return Engine.getSkeletonImpl(self.swerveHandle)

    def addTransform(self, bone, weight, firstVertex, numVertices):
        self.addTransformImpl(bone, weight, firstVertex, numVertices)
        Engine.addXOT(bone)

    def addTransformImpl(self, bone, weight, firstVertex, numVertices):
        Engine.addTransformImpl(self.swerveHandle, bone, weight, firstVertex, numVertices)

    def getBoneVertices(self, node, vertices, weights):
        return Engine.getBoneVertices(self.swerveHandle, node, vertices, weights)

    def getBoneTransform(self, node, transform):
        Engine.getBoneTransform(self.swerveHandle, node, transform)
