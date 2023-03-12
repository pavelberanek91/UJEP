from typing import List
from arc import Arc
from token import Token

class Transition:
    '''
    Transitions are local events (failure, restoration, etc).
    '''

    def __init__(self, name: str):
        self._name = name
        self._arcs = []
    
    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value) -> None:
        self._name = value

    def add_arc(self, arc: Arc) -> None:
        self._arcs.append(arc)

    def is_enabled(self) -> bool:
        token_sum = sum([arc.place.tokens_count() for arc in self._arcs if arc.edge_direction == 'input'])
        input_multiplicity_sum = sum([arc.weight for arc in self._arcs if arc.edge_direction == 'input'])
        return token_sum >= input_multiplicity_sum

    def fire(self) -> None:
        if self.is_enabled():
            self._fill_output_places()
            self._clear_input_places()

    def _fill_output_places(self) -> None:
        for arc in self.get_output_arcs():
            new_tokens = [Token(name="t"+str(Token.max_token_id)) for i in range(arc.weight)]
            arc.place.tokens.extend(new_tokens)

    def _clear_input_places(self) -> None:
        for arc in self.get_input_arcs():
            arc.place.tokens = []

    def get_input_arcs(self) -> List[Arc]:
        return [arc for arc in self._arcs if arc.edge_direction == "input"]

    def get_output_arcs(self) -> List[Arc]:
        return [arc for arc in self._arcs if arc.edge_direction == "output"]

    def __repr__(self) -> str:
        input_arcs_weights = "\n".join([f"P:{arc.place.name} " + f"W:{arc.weight}" for arc in self.get_input_arcs()])
        output_arcs_weights = "\n".join([f"P: {arc.place.name} " + f"W:{arc.weight}" for arc in self.get_output_arcs()])
        return f'Name:{self.name}\nInputs:\n{input_arcs_weights}\nOutputs:\n{output_arcs_weights}'        