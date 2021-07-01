import csv

csv_file = csv.reader(open("2021-03.csv"))
next(csv_file)
neg = 0
pos = 0
dist = 0
for row in csv_file:
    _dist = row[4]
    try:
        _dist = float(_dist)
        if _dist > 0:
            pos += _dist
        else:
            # if _dist <= 0: #4517
            neg += _dist
            print(_dist)
            print(neg)  # this is just for testing
    except ValueError:
        _dist = 0
    dist += _dist
dist = dist / 3
print("expenses")
print("{:.2f}".format(round(neg, 2)))
print("revenue")
print("{:.2f}".format(round(pos, 2)))
print("total")
print("{:.2f}".format(round(dist, 2)))
