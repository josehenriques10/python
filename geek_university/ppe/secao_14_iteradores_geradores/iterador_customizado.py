"""
Escrevendo um iterador customizado

class Contador:
    def __init__(self, menor, maior) -> None:
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration


count = Contador(1, 6)

it = iter(count)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for n in Contador(1, 61):
    print(n)

for n in range(1, 61):
    print(n)
"""


