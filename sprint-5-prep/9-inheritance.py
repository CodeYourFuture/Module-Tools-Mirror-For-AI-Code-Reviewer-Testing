class Parent:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def get_name(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Child(Parent):
    def __init__(self, first_name: str, last_name: str):
        super().__init__(first_name, last_name)
        self.previous_last_names = []

    def change_last_name(self, last_name) -> None:
        self.previous_last_names.append(self.last_name)
        self.last_name = last_name

    def get_full_name(self) -> str:
        suffix = ""
        if len(self.previous_last_names) > 0:
            suffix = f" (née {self.previous_last_names[0]})"
        return f"{self.first_name} {self.last_name}{suffix}"


# --- Predictions ---

person1 = Child("Elizaveta", "Alekseeva")

print(person1.get_name())
# Prediction: "Elizaveta Alekseeva"
# Reason: Child inherits get_name() from Parent, no name change yet

print(person1.get_full_name())
# Prediction: "Elizaveta Alekseeva"
# Reason: no previous last names, so suffix is empty string

person1.change_last_name("Tyurina")
# Saves "Alekseeva" into previous_last_names list, changes last_name to "Tyurina"

print(person1.get_name())
# Prediction: "Elizaveta Tyurina"
# Reason: get_name() uses self.last_name which is now "Tyurina"

print(person1.get_full_name())
# Prediction: "Elizaveta Tyurina (nee Alekseeva)"
# Reason: previous_last_names is not empty, so suffix shows the original last name

person2 = Parent("Elizaveta", "Alekseeva")

print(person2.get_name())
# Prediction: "Elizaveta Alekseeva"
# Reason: Parent has get_name(), works normally

# print(person2.get_full_name())
# Prediction: ERROR - AttributeError
# Reason: Parent class does not have get_full_name() method, only Child does

# person2.change_last_name("Tyurina")
# Prediction: ERROR - AttributeError
# Reason: Parent class does not have change_last_name() method, only Child does

# print(person2.get_name())
# Would print "Elizaveta Alekseeva" but we can't reach this line because of the error above

# print(person2.get_full_name())
# Would also error - Parent still doesn't have get_full_name()