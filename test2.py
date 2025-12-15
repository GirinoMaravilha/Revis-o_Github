"""
Módulo para testar o comando REBASE do git
"""

# Classes
class teste2:
    """
    Classe para realizar um teste

    Attributes:
        p (str): Frase qualquer.
    """
    def __init__(self,p):
        self.p = p

    def mostra_p(self):
        return self.p


# Função Main
def main():
    t = teste2("Astride Gostosa")
    t.mostra_p()


if __name__ == "__main__":
    main()