
from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats

# Демонстрація календаря
calendar = UkrainianCalendar()
print("Свята:", calendar.get_holiday_list())
print("01.01.2025 — робочий день?", calendar.is_working_day("2025-01-01"))
print("03.06.2025 — робочий день?", calendar.is_working_day("2025-06-03"))

# Меню калькулятора
calc = Calculator()
print("Калькулятор")
operation = input("Операція (+, -, *, /): ")
a = float(input("Перше число: "))
b = float(input("Друге число: "))

if operation == "+":
    print("Результат:", calc.add(a, b))
elif operation == "-":
    print("Результат:", calc.subtract(a, b))
elif operation == "*":
    print("Результат:", calc.multiply(a, b))
elif operation == "/":
    print("Результат:", calc.divide(a, b))
else:
    print("Невідома операція")

# Аналіз тексту
text = input("Введіть текст: ")
stats = TextStats(text)
print("Кількість слів:", stats.count_words())
letter, count = stats.most_common_letter()
print(f"Найчастіша літера: '{letter}' ({count} разів)" if letter else "Літер не знайдено")
