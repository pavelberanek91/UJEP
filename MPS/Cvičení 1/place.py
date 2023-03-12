from typing import List
from token import Token

class Place:
    '''
    Places are states, conditions (failed, functioning, etc) or resources that needs to be met
        before action can be carried out. Places contains tokens.
    '''

    def __init__(self, name: str, tokens: Token):
        self._name = name
        self._tokens = tokens

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value) -> None:
        self._name = value

    @property
    def tokens(self) -> List[Token]:
        return self._tokens
    @tokens.setter
    def tokens(self, value: List[Token]) -> None:
        self._tokens = value

    def tokens_count(self) -> int:
        return len(self._tokens)

    def __repr__(self) -> str:
        return f"Name: {self._name} Tokens: {self.tokens_count()}, {[token.name for token in self._tokens]}"