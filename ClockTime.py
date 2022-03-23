class ClockTime:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def setHours(self, hours):      # set hours
        self.hours = hours

    def setMinutes(self, minutes):  # set minutes
        self.minutes = minutes

    def setSeconds(self, seconds):  # set seconds
        self.seconds = seconds

    def showTime(self):             # display time
        time = self.hours.__str__() + " Hours, " + self.minutes.__str__() + " Minutes, " + self.seconds.__str__() + " Seconds"
        return time


ct = ClockTime()

# set hours
clockHours = int(input("Enter a value for hours: "))
ct.setHours(clockHours)

# set minutes
clockMinutes = int(input("Enter a value for minutes: "))
ct.setMinutes(clockMinutes)

# set hours
clockSeconds = int(input("Enter a value for seconds: "))
ct.setSeconds(clockSeconds)

# display time
clockTime = ct.showTime()
print("Time is", clockTime)
