import csv

csv_file = csv.reader(open("2021-03.csv"))
next(csv_file)

total_income = 0
total_expense = 0

for row in csv_file:
    amount = int(float(row[4]) * 100)
    if amount < 0:
        total_expense += amount
    else:
        total_income += amount
breakpoint()

cashflow = total_income - abs(total_expense)

print(f"Expenses: {total_expense / 100}")
print(f"Revenue: {total_income / 100}")
print(f"Cashflow: {cashflow / 100}")
