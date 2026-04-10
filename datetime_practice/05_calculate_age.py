from datetime import date

birth_date = date(2000, 5, 15)
today = date.today()

age = today.year - birth_date.year

print("Age:", age)