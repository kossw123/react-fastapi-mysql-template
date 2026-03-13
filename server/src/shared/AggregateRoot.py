from src.shared_interface.IEvent import IEvent

class AggregateRoot():
    def __init__(self):
        self.events = []

    def register(self, event: IEvent):
        self.events.add(event)
        
    def pull_events(self):
        events = self.events
        self.events = []
        return events
        
