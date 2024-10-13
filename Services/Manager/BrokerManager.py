class BrokerManager:
    def __init__(self):
        self.brokers = {}

    def registerBroker(self, broker):
        self.brokers[broker.name] = broker
        print(f"Asset '{broker.name}' created and added to the controller.")
