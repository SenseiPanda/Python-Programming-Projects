from counter import Counter


c = Counter(60,30)


print (c.get_value())
print(c.tick())


#when calling function have empty parenthesis
i = 0
while c.get_value()>0:
    c.tick()
    print(c.get_value())
print(c.get_value())

