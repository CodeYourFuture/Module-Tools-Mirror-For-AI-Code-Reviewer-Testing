from datetime import date


class Person:
    def __init__(self, name: str, dob: date, preferred_operating_system: str):
        self.name = name
        self.dob = dob
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self):
        dob = self.dob
        today = date.today()
        today_tuple = (today.year, today.month, today.day)
        eighteenth_bday_tuple = (dob.year + 18, dob.month, dob.day)

        return today_tuple >= eighteenth_bday_tuple


imran = Person("Imran", date(2004, 8, 31), "Ubuntu")
print(imran.is_adult())

# Change the Person class to take a date of birth
# (using the standard library’s datetime.date class) and store it in a field instead of age.

# Update the is_adult method to act the same as before.
