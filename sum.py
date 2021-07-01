import csv

csv_file = csv.reader(open("2021-03.csv"))
next(csv_file)

total_income = 0
total_expense = 0

for row in csv_file:
    amount = float(row[4])
    if amount < 0:
        total_expense += amount
    else:
        total_income += amount

cashflow = total_income - abs(total_expense)

print(f"Expenses: {round(total_expense,2)}")
print(f"Revenue: {round(total_income,2)}")
print(f"Cashflow: {round(cashflow,2)}")
