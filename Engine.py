import weakref

class Engine:
    # Constants for various types
    ANIMATIONCONTROLLER = 0
    ANIMATIONTRACK = 1
    APPEARANCE = 2
    BACKGROUND = 3
    CAMERA = 4
    COMPOSITINGMODE = 5
    FOG = 6
    GRAPHICS3D = 7
    GROUP = 8
    IMAGE2D = 9
    KEYFRAMESEQUENCE = 10
    LIGHT = 11
    LOADER = 12
    MATERIAL = 13
    MESH = 14
    MORPHINGMESH = 15
    PLASMAIMAGE = 16
    POLYGONMODE = 17
    RAYINTERSECTION = 18
    SKINNEDMESH = 19
    SPRITE3D = 20
    STAGESET = 21
    TEXTURE2D = 22
    TRANSFORM = 23
    TRIANGLESTRIPARRAY = 24
    VERTEXARRAY = 25
    VERTEXBUFFER = 26
    WORLD = 27
    UNKNOWN = 28

    OBJECT3D_FID = 0
    GRAPHICS3D_FID = 1
    LOADER_FID = 2
    RAYINTERSECTION_FID = 3
    TRANSFORM_FID = 4

    peer_table = {}  # Holds references to objects
    clean_peer_table = False
    lookup = None
    XOT = []
    XOTlength = 0
    tmpXOT = None

    @staticmethod
    def get_version_major():
        pass  # Native call

    @staticmethod
    def get_version_minor():
        pass  # Native call

    @staticmethod
    def get_revision_major():
        pass  # Native call

    @staticmethod
    def get_revision_minor():
        pass  # Native call

    @staticmethod
    def get_branch_number():
        pass  # Native call

    @staticmethod
    def release_handle(handle):
        pass  # Native call

    @staticmethod
    def get_handle_type(handle):
        pass  # Native call

    @staticmethod
    def get_handle_size(handle):
        pass  # Native call

    @staticmethod
    def instantiate_java_peer(handle):
        if handle == 0:
            return None

        success = False
        try:
            peer = Engine.get_java_peer(handle)
            if peer is not None:
                return peer

            peer = Engine._instantiate_peer_by_type(handle)

            if isinstance(peer, Object3D):
                params = None
                index = 0

                while (len := peer.get_user_parameter_value(index, None)) != -1:
                    if params is None:
                        params = {}
                    param_id = peer.get_user_parameter_id(index)
                    buffer = bytearray(len)
                    peer.get_user_parameter_value(index, buffer)
                    params[param_id] = buffer
                    index += 1

                if params is not None:
                    peer.remove_user_parameters()
                    peer.set_user_object(params)

            Engine.add_java_peer(handle, peer)
            success = True
            return peer
        finally:
            if not success:
                Engine.release_handle(handle)

    @staticmethod
    def _instantiate_peer_by_type(handle):
        # Create peer based on the type of handle
        peer = None
        handle_type = Engine.get_handle_type(handle)

        if handle_type == 0:
            peer = AnimationController(handle)
        elif handle_type == 1:
            peer = AnimationTrack(handle)
        elif handle_type == 2:
            peer = Appearance(handle)
        elif handle_type == 3:
            peer = Background(handle)
        elif handle_type == 4:
            peer = Camera(handle)
        elif handle_type == 5:
            peer = CompositingMode(handle)
        elif handle_type == 6:
            peer = Fog(handle)
        elif handle_type == 7:
            peer = Graphics3D(handle)
        elif handle_type == 8:
            peer = Group(handle)
        elif handle_type in [9, 16, 21]:
            peer = Image2D(handle)
        elif handle_type == 10:
            peer = KeyframeSequence(handle)
        elif handle_type == 11:
            peer = Light(handle)
        elif handle_type == 12:
            peer = Loader(handle)
        elif handle_type == 13:
            peer = Material(handle)
        elif handle_type == 14:
            peer = Mesh(handle)
        elif handle_type == 15:
            peer = MorphingMesh(handle)
        elif handle_type == 17:
            peer = PolygonMode(handle)
        elif handle_type == 18:
            peer = RayIntersection(handle)
        elif handle_type == 19:
            peer = SkinnedMesh(handle)
        elif handle_type == 20:
            peer = Sprite3D(handle)
        elif handle_type == 22:
            peer = Texture2D(handle)
        elif handle_type == 23:
            peer = Transform(handle)
        elif handle_type == 24:
            peer = TriangleStripArray(handle)
        elif handle_type == 25:
            peer = VertexArray(handle)
        elif handle_type == 26:
            peer = VertexBuffer(handle)
        elif handle_type == 27:
            peer = World(handle)
        else:
            raise ValueError("Invalid handle type")

        return peer

    @staticmethod
    def clean_up_peer_table():
        for key in list(Engine.peer_table.keys()):
            ref = Engine.peer_table[key]
            if ref() is None:
                del Engine.peer_table[key]

    @staticmethod
    def add_java_peer(handle, peer):
        with Engine.peer_table:
            if Engine.clean_peer_table:
                Engine.clean_up_peer_table()
                Engine.clean_peer_table = False
            Engine.peer_table[handle] = weakref.ref(peer)

    @staticmethod
    def get_java_peer(handle):
        with Engine.peer_table:
            if Engine.clean_peer_table:
                Engine.clean_up_peer_table()
                Engine.clean_peer_table = False

            entry = Engine.peer_table.get(handle)
            if entry is not None:
                return entry()

        return None

    @staticmethod
    def get_java_peer_array_handles(peers):
        if peers is None:
            return None

        handles = []
        for peer in peers:
            if peer is None:
                handles.append(0)
            elif isinstance(peer, Object3D):
                handles.append(peer.swerve_handle)
            else:
                raise ValueError(f"{peer} is not an instance of Object3D")

        return handles

    @staticmethod
    def add_xot(obj):
        if obj and (obj.ii or obj.uo is not None):
            with Engine.XOT:
                if obj not in Engine.XOT:
                    if Engine.XOTlength == len(Engine.XOT):
                        Engine.tmpXOT = [None] * (len(Engine.XOT) * 2 or 2)
                        Engine.XOT.extend(Engine.tmpXOT)
                        Engine.tmpXOT = None
                    Engine.XOT.append(obj)
                    Engine.XOTlength += 1

    @staticmethod
    def add_xot_multiple(obj_list):
        if obj_list:
            for obj in obj_list:
                Engine.add_xot(obj)
