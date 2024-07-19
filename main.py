class SmartDiet:
    def __init__(self):
        self.food_items = {}
        self.calories_consumed = {}

    def register_food(self, name: str, calories_per_unit: int):
        if calories_per_unit <= 0:
            raise ValueError("Калорийность должна быть положительной")
        self.food_items[name] = calories_per_unit
        self.calories_consumed[name] = 0

    def add_food(self, name: str, units: int):
        if name not in self.food_items:
            raise ValueError(f"Продукт '{name}' не зарегистрирован")
        if units <= 0:
            raise ValueError("Количество должно быть положительным")
        self.calories_consumed[name] += self.food_items[name] * units

    def calculate(self) -> int:
        return sum(self.calories_consumed.values())