class SmartDiet:
    def __init__(self):
        self.food_registry = {}
        self.food_intake = {}

    def register_food(self, name: str, calories: int):
        if calories < 0:
            raise ValueError("Калорийность не может быть отрицательной.")
        self.food_registry[name] = calories

    def add_food(self, name: str, quantity: int):
        if name not in self.food_registry:
            raise ValueError("Продукт не зарегистрирован.")
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным.")
        if name in self.food_intake:
            self.food_intake[name] += quantity
        else:
            self.food_intake[name] = quantity

    def calculate(self) -> int:
        total_calories = 0
        for name, quantity in self.food_intake.items():
            total_calories += self.food_registry[name] * quantity
        return total_calories


import unittest

class TestSmartDiet(unittest.TestCase):

    def setUp(self):
        self.diet = SmartDiet()
        self.diet.register_food("Яблоко", 52)
        self.diet.register_food("Банан", 89)

    def test_calculate_single_food(self):
        """Тест на расчет калорий для одного продукта"""
        self.diet.add_food("Яблоко", 2)
        total_calories = self.diet.calculate()
        self.assertEqual(total_calories, 104, "Ошибка в подсчете калорий для яблок.")

    def test_calculate_multiple_foods(self):
        """Тест на расчет калорий для нескольких продуктов"""
        self.diet.add_food("Яблоко", 3)  # 3 * 52 = 156
        self.diet.add_food("Банан", 2)   # 2 * 89 = 178
        total_calories = self.diet.calculate()
        self.assertEqual(total_calories, 334, "Ошибка в подсчете калорий для нескольких продуктов.")  # Исправлено

    def test_calculate_no_foods(self):
        """Тест на расчет калорий при отсутствии потребленной еды"""
        total_calories = self.diet.calculate()
        self.assertEqual(total_calories, 0, "Ошибка: сумма калорий должна быть 0 при отсутствии продуктов.")

if __name__ == "__main__":
    unittest.main()