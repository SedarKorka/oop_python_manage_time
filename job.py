from activity import Activity

class Job(Activity):
    def __init__(self,bus_stop, direction, time_to_go, wakeuptime):
        super().__init__(bus_stop, direction, time_to_go)
        self.wakeuptime = wakeuptime
