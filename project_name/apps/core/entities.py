class CreateLocationIn:
    def __init__(self, name, type, description):
        self.name = name
        self.type = type
        self.description = description


class CreateLocationOut:
    def __init__(self, name, type, description, sucursals):
        self.name = name
        self.type = type
        self.description = description
        self.sucursals = sucursals
