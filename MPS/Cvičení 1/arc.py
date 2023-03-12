from place import Place

class Arc:
    '''
    Directed edges between Places and Transitions that connects state to event.
    '''

    def __init__(self, name: str, place: Place, edge_direction: str, weight: int = 1):
        self._name = name
        self._place = place
        self._weight = weight
        self._edge_direction = edge_direction

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        self._name = value
    
    @property
    def place(self) -> Place:
        return self._place
    @place.setter
    def place(self, value: Place) -> None:
        self._place = value

    @property
    def weight(self) -> int:
        return self._weight
    @weight.setter
    def weight(self, value: int) -> None:
        self._weight = value
    
    @property
    def edge_direction(self) -> str:
        return self._edge_direction
    @edge_direction.setter
    def edge_direction(self, value: str) -> None:
        self._edge_direction = value
