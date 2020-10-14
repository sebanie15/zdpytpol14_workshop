from datetime import datetime
from typing import List
from src.inventory.product import BaseProduct


class Food(BaseProduct):
	def __init__(self,name, price, quantity, kcal: int, best_before: datetime, nutritions: List):
		super().__init__(name, price, quantity)
		self.kcal = kcal
		self.best_before = best_before
		self.nutritions = nutritions


x = Food('ogórek', 2.3, 10, 102, datetime(2020, 10, 15), [])

print(x)
