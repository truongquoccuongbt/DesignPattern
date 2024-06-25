from abc import ABC, abstractmethod

################## Mobile ##############
class IMobile(ABC):
    def __init__(self, name: str = None, price: float = None, code: str = None) -> None:
        self.name: str = name
        self.price: float = price
        self.code: str = code

    @abstractmethod
    def to_string(self) -> str:
        pass

class ClassicMobile(IMobile):
    def __init__(self, name: str, price: float, code: str) -> None:
        super().__init__(name, price, code)
    
    def to_string(self) -> str:
        return f'Model {self.code} - price: {self.price}'
    
class BussinessMobile(IMobile):
    def __init__(self, name: str, price: float, code: str) -> None:
        super().__init__(name, price, code)
        self.dynamon: bool = True

    def to_string(self):
        return f'Model {self.code} - price: {self.price}'
    
################## Tablet ##############
class ITablet(ABC):
    def __init__(self, name: str = None, screen_size: int = None, price: float = None) -> None:
        self.name: str = name
        self.screen_size = screen_size
        self.price = price

    @abstractmethod
    def to_string(self) -> str:
        pass

class ClassicTablet(ITablet):
    def __init__(self, name: str, screen_size: int, price: float) -> None:
        super().__init__(name, screen_size, price)

    def to_string(self):
        text: str = 'Name ' + self.name + '\n'
        text += 'screen_size: ' + str(self.screen_size) + '\n'
        text += 'Price: ' + str(self.price) + '\n'
        return text
    
class BussinessTablet(ITablet):
    def __init__(self, name: str, screen_size: int, price: float) -> None:
        super().__init__(name, screen_size, price)

    def to_string(self):
        text: str = 'Name ' + self.name + '\n'
        text += 'screen_size: ' + str(self.screen_size) + '\n'
        text += 'Price: ' + str(self.price) + '\n'
        return text


################## Watch ##############
class IWatch(ABC):
    def __init__(self, name: str = None, type: str = None, sex: str = None) -> None:
        self.name: str = name
        self.type: str = type
        self.sex: str = sex

    @abstractmethod
    def to_string(self) -> str:
        pass

class ClassicWatch(IWatch):
    def __init__(self, name: str = None, type: str = None, sex: str = None) -> None:
        super().__init__(name, type, sex)

    def to_string(self) -> str:
        return f'Name: {self.name} - type: {self.type} - sex: {self.sex}'

class BussinessWatch(IWatch):
    def __init__(self, name: str = None, type: str = None, sex: str = None) -> None:
        super().__init__(name, type, sex)

    def to_string(self) -> str:
        return f'Name: {self.name} - type: {self.type} - sex: {self.sex}'
    

class IProduct(ABC):
    def __init__(self, name_type:str = None) -> None:
        self.mobile = None
        self.watch  = None
        self.tablet = None
        self.name_type = name_type

    def add_mobile(self, mobile: IMobile) -> None:
        self.mobile = mobile

    def add_watch(self, watch: IWatch) -> None:
        self.watch = watch
    
    def add_tablet(self, tablet: ITablet) -> None:
        self.tablet = tablet

    def print(self) -> str:
        print(self.mobile.to_string())
        print(self.watch.to_string())
        print(self.tablet.to_string())


########## Factory ###########
class AbstractProductFactory(ABC):
    @abstractmethod
    def create_watch(self) -> IWatch:
        pass

    @abstractmethod
    def create_tablet(self) -> ITablet:
        pass

    @abstractmethod
    def create_mobile(self) -> IMobile:
        pass

    @abstractmethod
    def create_product(self) -> IProduct:
        pass


class ClassicProductFactory(AbstractProductFactory):
    
    def create_watch(self) -> IWatch:
        return ClassicWatch()
    
    def create_tablet(self) -> ITablet:
        return ClassicTablet()
    
    def create_mobile(self) -> IMobile:
        return ClassicMobile()
    

class BussinessProductFactory(AbstractProductFactory):
    def create_watch(self) -> IWatch:
        return BussinessWatch()
    
    def create_tablet(self) -> ITablet:
        return BussinessTablet()
    
    def create_mobile(self) -> IMobile:
        return BussinessMobile()


def create_event(factor: AbstractProductFactory) -> IProduct:
    mobile = factor.create_mobile()
    watch = factor.create_watch()
    tablet =  factor.create_tablet()
    
    season_product = factor.create_product()
    season_product.add_mobile(mobile)
    season_product.add_watch(watch)
    season_product.add_tablet(tablet)
    return season_product

def main():
    type_class: str = 'buss'
    factory: AbstractProductFactory = None

    if(type_class == 'class'):
        factory = ClassicProductFactory()
    else:
        factory = BussinessProductFactory()

    season_product:IProduct = create_event(factory)

if __name__ == "__main__":
    main()
