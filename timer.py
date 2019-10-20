from counter import Counter

class Timer:
    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(24,hours)
        self.minutes = Counter(60,minutes)
        self.seconds = Counter(60,seconds)

    def __str__(self):
        return str(self)

    def tick(self):
        if self.seconds.tick():
            self.minutes.tick()
            if self.minutes.tick():
                self.hours.tick()


    #first, call 'tick' on seconds
    #if 'tick' on seconds returns true (it gets wrapped), then proceed with decrementing minutes
    # if 'tick' on minutes returns true (it gets wrapped), then proceed with decrementing hours
    def is_zero(self):
        if Timer.tick():
            return True
        else:
            return False
