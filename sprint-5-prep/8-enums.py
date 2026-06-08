from dataclasses import dataclass
from enum import Enum
from typing import List
import sys

class OperatingSystem(Enum):
    MACOS = "macOS"
    ARCH = "Arch Linux"
    UBUNTU = "Ubuntu"

@dataclass(frozen=True)
class Person:
    name: str
    age: int
    preferred_operating_system: OperatingSystem

@dataclass(frozen=True)
class Laptop:
    id: int
    manufacturer: str
    model: str
    screen_size_in_inches: float
    operating_system: OperatingSystem

os_input_name = input("Your name is: ")

os_input_age = input("Your age is: ")
try:
    age = int(os_input_age)
except ValueError:
    print(f"Error: '{os_input_age}' is not a valid age", file=sys.stderr)
    sys.exit(1)

os_input_preferred_os = input("Preferred operating system is: ")
try:
    preferred_operating_system = OperatingSystem(os_input_preferred_os)
except ValueError:
    print(f"Error: '{os_input_preferred_os}' is not a valid operating system", file=sys.stderr)
    sys.exit(1)

person = Person(name = os_input_name, age=age, preferred_operating_system=preferred_operating_system)

laptops = [
    Laptop(id=1, manufacturer="Dell", model="XPS", screen_size_in_inches=13, operating_system=OperatingSystem.ARCH),
    Laptop(id=2, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=3, manufacturer="Dell", model="XPS", screen_size_in_inches=15, operating_system=OperatingSystem.UBUNTU),
    Laptop(id=4, manufacturer="Apple", model="macBook", screen_size_in_inches=13, operating_system=OperatingSystem.MACOS),
    Laptop(id=5, manufacturer="Apple", model="macBook", screen_size_in_inches=14, operating_system=OperatingSystem.MACOS),
    Laptop(id=6, manufacturer="Apple", model="macBook", screen_size_in_inches=15, operating_system=OperatingSystem.MACOS),
]

def find_specific_os(laptops: List[Laptop], preferred_os: OperatingSystem) -> List[Laptop]:
    possible_laptops = []

    for laptop in laptops:
        if (laptop.operating_system == preferred_os):
            possible_laptops.append(laptop)
    
    possible_laptops_amount = len(possible_laptops)

    print(f"The amount of possible laptops with preferred operating system is", possible_laptops_amount)

    return possible_laptops

result = find_specific_os(laptops, preferred_operating_system)

counts_laptop_per_os: dict[OperatingSystem, int] = {}

for laptop in laptops:
    os = laptop.operating_system
    if os in counts_laptop_per_os:
        counts_laptop_per_os[os] += 1
    else:
        counts_laptop_per_os[os] = 1

top_os = max(counts_laptop_per_os, key=lambda os: counts_laptop_per_os[os])

if top_os != preferred_operating_system:
    print(f"If you're willing to use {top_os.value}, you're more likely to get a laptop ({counts_laptop_per_os[top_os]} available)")