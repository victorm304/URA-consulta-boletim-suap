class FalhaAoObterToken(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class CodigoDeAcessoVazio(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)