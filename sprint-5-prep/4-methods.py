# Exercises-1
# Think of the advantages of using methods instead of free functions. 
# Write them down in your notebook.

# 1. Organisation: all Person-related logic lives inside the Person class.

# 2. Encapsulation: we only have to update the method once, 
# for example if we change "age" to "date_of_birth" inside the class.
# With free functions, we'd have to update every function that touches person.age across the whole codebase.

# 3. Simple search: if we type "imran." our editor shows everything Person can do.
# With free functions, we have to remember they exist.

# 4. Clear ownership: "person.is_adult()" is definitely about a person,
# but with "is_adult(x)" we don't know what it's about.

# 5. Easier to catch errors with mypy, because all methods related to the class are in one place.


# Exercises-2
# Change the Person class to take a date of birth (using the standard library’s datetime.date class)
#  and store it in a field instead of age.
#
# Update the is_adult method to act the same as before.

from datetime import date

class Person:
    def __init__(self, name: str, date_of_birth: date, preferred_operating_system: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.preferred_operating_system = preferred_operating_system

    def is_adult(self) -> bool:
        today = date.today()
        age = today.year - self.date_of_birth.year

        if(today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1

        return age >= 18

imran = Person("Imran", date(2003, 6, 20), "Ubuntu")
print(imran.is_adult())
