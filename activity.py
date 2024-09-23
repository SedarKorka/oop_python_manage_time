class Activity:
    def __init__(self, bus_stop, direction, time_to_go):
        self.bus_stop = bus_stop
        self.direction = direction
        self.time_to_go = time_to_go

    def PrintWakeUpTime(self):
        print(self.time_to_go)
