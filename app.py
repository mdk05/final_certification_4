import pandas as pd

# Загружаем данные из CSV-файла
data = pd.read_csv('data.csv')

# Вычисляем среднюю зарплату всех сотрудников
average_salary = data['salary'].mean()
print(f"Средняя зарплата всех сотрудников: {average_salary}")

# Отбираем сотрудников старше 30 лет
employees_above_30 = data[data['age'] > 30]
print("\nСотрудники старше 30 лет:")
print(employees_above_30)
