from timer import Timer
from counter import Counter

t = Timer(1,30,00)

c = Counter(60,0)


while t.seconds:
    t.tick()
    print(int(t.seconds))


# i = 0
# while c.get_value()>0:
#     c.tick()
#     print(c.get_value())
# print(c.get_value())
