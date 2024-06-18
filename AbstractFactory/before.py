





class Program:
    def __init__(self, name: str, price: float, rate: float) -> None:
        self.name: str = name
        self.price: float = price
        self.rate: float = rate
    
    def get_price(self):
        total: float = self.price + (self.price * self.rate)
        print(f'Price of program {self.name}: {total}')

class Region:
    def __init__(self, name: str, math: Program, liter: Program, eng: Program) -> None:
        self.name: str = name
        self.math: Program = math
        self.literature: Program = liter
        self.english: Program = eng

    def print_region(self):
        text: str = 'Region ' + self.name + '\n'
        text += 'Math: ' + self.math.get_price()
        text += 'Literature: ' + self.literature.get_price()
        text += 'English: ' + self.english.get_price()
        print(text)


def main():
    math_v1: Program = Program('Math v1', 1000, 1)
    math_v2: Program = Program('Math v2', 1000, -0.5)
    math_v3: Program = Program('Math v3', 1000, 0.5)

    literature_v1: Program = Program('literature v1', 1000, 1)
    literature_v2: Program = Program('literature v2', 1000, -0.5)
    literature_v3: Program = Program('literature v3', 1000, 0.5)

    english_v1: Program = Program('english v1', 1000, 1)
    english_v2: Program = Program('english v2', 1000, -0.5)
    english_v3: Program = Program('english v3', 1000, 0.5)

    reg_v1:Region = Region(name='v1')
    reg_v2:Region = Region(name='v2')
    reg_v3:Region = Region(name='v3')



if __name__ == "__main__":
    main()