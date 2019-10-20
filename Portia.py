# This program computes Cormen's wealth over 2000 years

year = 0
cormen_dollars = 1  # initial deposit
jules_dollars = 100000  # initial deposit
CORMEN_INTEREST_RATE = 5
JULES_INTEREST_RATE = 4
cormen_beats_jules = 0  # this will track if Cormen has more money than Jules
while (year < 2020):
    # cormen's grows at 5%
    cormen_dollars = cormen_dollars * 1.05
    # jule's grows at 4%
    jules_dollars = jules_dollars * 1.04

    if cormen_dollars >= jules_dollars:
        print("Cormen's wealth exceeded Jules' wealth in the year " + str(year))
        #
        break

    year = year + 1
cormen_dollars = float(cormen_dollars)
jules_dollars = float(jules_dollars)
print("Cormen's balance in year 1203 was: " + str(cormen_dollars) + " dollars")
print("Jules' balance in year 1203 was: " + str(jules_dollars) + " dollars")