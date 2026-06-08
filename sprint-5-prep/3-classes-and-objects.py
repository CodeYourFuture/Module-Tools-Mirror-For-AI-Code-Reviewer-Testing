class Person:
    def __init__(self, name: str, age: int, preferred_operating_system: str):
        self.name = name
        self.age = age
        self.preferred_operating_system = preferred_operating_system

imran = Person("Imran", 22, "Ubuntu")
print(imran.name)
#print(imran.address)
#error: Person class has no attribute "address"

eliza = Person("Eliza", 34, "Arch Linux")
print(eliza.name)
#print(eliza.address)
#the same error: Person class has no attribute "address"

def is_adult(person: Person) -> bool:
    return person.age >= 18

print(is_adult(imran))

def get_phone(person: Person) -> str:
    return person.phone_number
# After running mypy this method also causes an error, because Person class has no attribute "phone_number"