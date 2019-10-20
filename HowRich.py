# this gives a one time sum of Cormen's wealth in 2019, and how many times over he can buy the world
year = 0
cormen_dollars = 1  # initial deposit
CORMEN_INTEREST_RATE = 5
WORLD_REALESTATE_VALUE = 228000000000000
while (year < 2020):
    # cormen's grows at 5%
    cormen_dollars = cormen_dollars * 1.05

    # add a year to the year counter
    year = year + 1

print("After 2019 years of compound interest, Cormen would have " + str(cormen_dollars)
      + " dollars")

realestate_multiple = cormen_dollars / WORLD_REALESTATE_VALUE

print("This means Cormen could buy the world's real estate " + str(realestate_multiple) + " times over!")