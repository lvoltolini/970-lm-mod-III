
class operations:
    @staticmethod
    def soma(x, y):
        for element in (x, y):
            if type(element) not in (int, float):
                print(element)
                raise TypeError(f"O input 'a' e 'b' devem ser uma string, recebido {x}, {type(x)}, {y}, {type(y)}")
        return x + y