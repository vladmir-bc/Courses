import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(list, Loggable):
    def append(self, p_object):
        super(LoggableList, self).append(p_object)
        self.log(p_object)

y = LoggableList([1, 2, 3, 4])
y.append(10)
print(y)