class Time:
    """ Blueprint for a Time object"""
    def __init__(self):
        self.hour = 0
        self.minute = 0
        self.second = 0

    def set_time(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print (self.hour, ":", self.minute, ":", self.second)
#        print ('%d:%d:%d' % (self.hour, self.minute, self.second))
