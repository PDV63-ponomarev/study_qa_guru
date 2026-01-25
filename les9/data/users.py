import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    address: str



user1 = User('Test Testovich', 'test@gmail.com', 'city Testa, Testova street')
user2 = User('harry', 'potter@hg.com', 'Privet drive')

