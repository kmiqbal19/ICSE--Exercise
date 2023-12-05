class Food:
    def __init__(self, quantifier):
        self.quantifier = quantifier

    def calories(self):
        pass 

    def get_weight(self):
        pass  

    def __eq__(self, other):
        return self.calories() == other.calories()

    def __lt__(self, other):
        return self.calories() < other.calories()


class Apples(Food):
    def calories(self):
        return 102 * self.quantifier

    def get_weight(self):
        return 200 * self.quantifier


class Oranges(Food):
    def calories(self):
        return 94 * self.quantifier

    def get_weight(self):
        return 200 * self.quantifier


class CookieDough(Food):
    def __init__(self, weight):
        super().__init__(weight)

    def calories(self):
        return int(2.44 * self.quantifier)

    def get_weight(self):
        return self.quantifier


class Broccoli(Food):
    def calories(self):
        return 55 * self.quantifier

    def get_weight(self):
        return 150 * self.quantifier


class Chocolate(Food):
    def __init__(self, amount):
        super().__init__(amount)

    def calories(self):
        return int(5.2 * self.quantifier)

    def get_weight(self):
        return 25 * self.quantifier


# Examples
apple1 = Apples(3)
orange1 = Oranges(2)
cookie_dough1 = CookieDough(300)
broccoli1 = Broccoli(4)
chocolate1 = Chocolate(5)

print(f"Apple 1 weight: {apple1.get_weight()}g, calories: {apple1.calories()} kcal")
print(f"Orange 1 weight: {orange1.get_weight()}g, calories: {orange1.calories()} kcal")
print(f"Cookie Dough 1 weight: {cookie_dough1.get_weight()}g, calories: {cookie_dough1.calories()} kcal")
print(f"Broccoli 1 weight: {broccoli1.get_weight()}g, calories: {broccoli1.calories()} kcal")
print(f"Chocolate 1 weight: {chocolate1.get_weight()}g, calories: {chocolate1.calories()} kcal")

# Comparisons
print(f"Is apple1 equal to orange1? {apple1 == orange1}")
print(f"Is cookie_dough1 less than chocolate1? {cookie_dough1 < chocolate1}")
