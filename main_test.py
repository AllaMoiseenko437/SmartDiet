import pytest
from main import SmartDiet

def test_calculate_no_food():
    diet = SmartDiet()
    assert diet.calculate() == 1

def test_calculate_with_registered_food():
    diet = SmartDiet()
    diet.register_food("Яблоко", 50)
    diet.add_food("Яблоко", 2)
    assert diet.calculate() == 100

def test_calculate_with_multiple_foods():
    diet = SmartDiet()
    diet.register_food("Банан", 90)
    diet.register_food("Апельсин", 80)

    diet.add_food("Банан", 3)  # 270 калорий
    diet.add_food("Апельсин", 1)  # 80 калорий
