from src.shared_interface.IEvent import IEvent
from src.shared_interface.IEventHandler import IEventHandler

class EventDispatcher():
    def __init__(self):
        self.handlers = {}
    def register(self, event_type: IEvent, handler: IEventHandler):
        handlers = self.handlers.setdefault(event_type, [])
        if handler not in handlers:
            handlers.append(handler)
    def dispatch(self, events):
        for event in events:
            for handler in self.handlers.get(type(event)):
                handler.handle(event)

