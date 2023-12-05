import random


class Clock:
    def __init__(self, hours: int, minutes: int):
        total_minutes = (hours * 60 + minutes) % (24 * 60)
        self.hours = total_minutes // 60
        self.minutes = total_minutes % 60

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clock):
            return False
        return self.hours == other.hours and self.minutes == other.minutes

    def __add__(self, other: "Clock") -> "Clock":
        total_minutes = (self.hours * 60 + self.minutes + other.hours * 60 + other.minutes) % (24 * 60)
        return Clock(total_minutes // 60, total_minutes % 60)

    def add_minutes(self, minutes: int) -> "Clock":
        total_minutes = (self.hours * 60 + self.minutes + minutes) % (24 * 60)
        return Clock(total_minutes // 60, total_minutes % 60)

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}"


#  Clock objects
clock1 = Clock(random.randint(0, 23), random.randint(0, 59))
clock2 = Clock(random.randint(0, 23), random.randint(0, 59))

#  equality
print(f"Clock 1: {clock1}")
print(f"Clock 2: {clock2}")
print(f"Are they equal? {'Yes' if clock1 == clock2 else 'No'}")

# addition
sum_clock = clock1 + clock2
print(f"Sum of Clock 1 and Clock 2: {sum_clock}")

# adding minutes
new_clock = clock1.add_minutes(30)
print(f"Clock 1 + 30 minutes: {new_clock}")
