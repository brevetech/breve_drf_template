from typing import List


class CreateLocationIn:
    """Handler location in entity"""

    name: str
    location_type: str
    description: str

    def __init__(self, name: str, location_type: str, description: str):
        self.name = name
        self.location_type = location_type
        self.description = description


class CreateLocationOut:
    """Handler location out entity"""

    name: str
    location_type: str
    description: str
    sucursals: List

    def __init__(self, name: str, location_type: str, description: str, sucursals: List):
        self.name = name
        self.location_type = location_type
        self.description = description
        self.sucursals = sucursals
