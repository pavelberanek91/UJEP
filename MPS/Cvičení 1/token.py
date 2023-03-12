class Token:
    '''
    Tokens are dynamic elements used to represent system state at certain time.
    '''

    max_token_id = 0

    def __init__(self, name: str):
        self._name = name
        Token.max_token_id += 1

    @property
    def name(self) -> str:
        return self._name
    @name.setter
    def name(self, value: str) -> None:
        self._name = value