from activity import Activity

class School(Activity):
    def __init__(self, bus_stop, direction, time_to_go, wakeuptime):
        super().__init__(bus_stop, direction, time_to_go, wakeuptime)
        self.wakeuptime = wakeuptime

    def PrintWakeUpTime(self):
        print(self.wakeuptime)