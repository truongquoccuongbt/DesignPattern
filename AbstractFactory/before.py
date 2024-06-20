
class Mobile:
    def __init__(self, name: str, price: float, code: str) -> None:
        self.name: str = name
        self.price: float = price
        self.code: str = code
    
    def to_string(self) -> str:
        return f'Model {self.code} - price: {self.price}'



class BussinessMobile:
    def __init__(self, name: str, price: float, code: str) -> None:
        self.name: str = name
        self.price: float = price
        self.code: str = code
        self.dynamon: bool = True
    
    def to_string(self):
        return f'Model {self.code} - price: {self.price}'


class BussinessTablet:
    def __init__(self, name: str, screen_size: int, price: float) -> None:
        self.name: str = name
        self.screen_size = screen_size
        self.price = price
        self.dynamon: bool = True

    def to_string(self):
        text: str = 'Name ' + self.name + '\n'
        text += 'screen_size: ' + str(self.screen_size) + '\n'
        text += 'Price: ' + str(self.price) + '\n'
        return text


class Tablet:
    def __init__(self, name: str, screen_size: int, price: float) -> None:
        self.name: str = name
        self.screen_size = screen_size
        self.price = price

    def to_string(self):
        text: str = 'Name ' + self.name + '\n'
        text += 'screen_size: ' + str(self.screen_size) + '\n'
        text += 'Price: ' + str(self.price) + '\n'
        return text


class BussinessWatch:
    def __init__(self, name: str = None, type: str = None, sex: str = None) -> None:
        self.name: str = name
        self.type: str = type
        self.sex: str = sex

    def to_string(self) -> str:
        return f'Name: {self.name} - type: {self.type} - sex: {self.sex}'


class Watch:
    def __init__(self, name: str = None, type: str = None, sex: str = None) -> None:
        self.name: str = name
        self.type: str = type
        self.sex: str = sex
        self.dynamon: bool = True

    def to_string(self) -> str:
        return f'Name: {self.name} - type: {self.type} - sex: {self.sex}'


class ClassicProduct:
    def __init__(self, name_type:str) -> None:
        self.mobile = None
        self.watch  = None
        self.tablet = None
        self.name_type = None

    def add_mobile(self, mobile: Mobile) -> None:
        self.mobile = mobile

    def add_watch(self, watch: Watch) -> None:
        self.watch = watch
    
    def add_tablet(self, tablet: Tablet) -> None:
        self.tablet = tablet

    def print(self) -> str:
        print(self.mobile.to_string())
        print(self.watch.to_string())
        print(self.tablet.to_string())
     

class BussinessProduct:
    def __init__(self, name_type:str) -> None:
        self.mobile: Mobile = None
        self.watch: Watch  = None
        self.tablet: Tablet = None
        self.name_type: str = None

    def add_mobile(self, mobile: BussinessMobile) -> None:
        self.mobile = mobile

    def add_watch(self, watch: BussinessWatch) -> None:
        self.watch = watch
    
    def add_tablet(self, tablet: BussinessTablet) -> None:
        self.tablet = tablet

    def print(self) -> str:
        print(self.mobile.to_string())
        print(self.watch.to_string())
        print(self.tablet.to_string())


def main():
    type_class: str = 'buss'

    mobile_classic: Mobile = Mobile('apple', 1000, '0001')
    watch_classic: Watch = Watch('galaxy watch', 1000, 'Female')
    tablet_classic: Tablet = Tablet('ipad mini', 15, 5000)

    if(type_class == 'class'):
        classic_product: ClassicProduct = ClassicProduct(name_type='classic')

        classic_product.add_mobile(mobile_classic)
        classic_product.add_watch(watch_classic)
        classic_product.add_tablet(tablet_classic)

        classic_product.print()
    elif (type_class == 'buss'):
        mobile_bus: BussinessMobile = BussinessMobile('buss apple', 1000, '0001')
        watch_bus: BussinessWatch = BussinessWatch('buss galaxy watch', 1000, 'Female')
        tablet_bus: BussinessTablet = BussinessTablet('buss ipad mini', 15, 5000)

        bussiness_product: BussinessProduct = BussinessProduct(name_type='bussiness')
        bussiness_product.add_mobile(mobile_bus)
        bussiness_product.add_tablet(tablet_bus)
        bussiness_product.add_watch(tablet_bus)
        bussiness_product.print()



if __name__ == "__main__":
    main()