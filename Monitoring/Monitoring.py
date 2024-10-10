from datetime import datetime


class Monitoring:
    def logInformation(self,info):
        print(datetime.now(),":",info)
