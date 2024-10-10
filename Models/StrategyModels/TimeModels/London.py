from datetime import datetime

import pytz

from Interfaces.RiskManagement.ITimeWindow import ITimeWindow

berlin_timezone = pytz.timezone('Europe/Berlin')


class LondonOpen(ITimeWindow):
    def IsInExitWindow(self):
        # Get the current time in Berlin
        current_time_berlin = datetime.now(berlin_timezone)

        # Check if the current hour is 12 (noon)
        if current_time_berlin.hour == 17:
            return True
        return False

    def IsInEntryWindow(self):
        # Get the current time in Berlin
        current_time_berlin = datetime.now(berlin_timezone)

        # Check if the current hour is between 8 AM and 11 AM (inclusive)
        if 8 <= current_time_berlin.hour <= 11:
            return True
        return False
