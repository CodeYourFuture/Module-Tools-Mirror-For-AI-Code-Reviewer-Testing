from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Person:
    name: str
    date_of_birth: date
    preferred_operating_system: str

    def is_adult(self) -> bool:
        today = date.today()

        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18
    

zoi = Person("Zoi", date(2003, 3, 23), "Ubuntu")

print("zoi:", zoi)
print("zoi.is_adult():", zoi.is_adult())