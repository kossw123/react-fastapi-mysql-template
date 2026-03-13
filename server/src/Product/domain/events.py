from src.shared_interface.IEvent import IEvent, IEventHandler


# 1. Created
# 2. Activated
# 3. Discontinued


class ProductCreated(IEvent):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price
class ProductCreatedHandler(IEventHandler):
    def handle(self, event):
        return {
            "message": f"ProductCreated: {event.id}, {event.name}"
        }



class ProductActivated(IEvent):
    def __init__(self, id):
        self.id = id
class ProductActivatedHandler(IEventHandler):
    def handle(self, event):
        return {
            "message": f"Product Activated : {event.id}"
        }
    



class ProductDiscontinued(IEvent):
    def __init__(self, id):
        self.id = id
class ProductDiscontinuedHandler(IEventHandler):
    def handle(self, event):
        return { 
            "message": f"Product Discontinued : {event.id}"
        }


class ProductOutOfStack(IEvent):
    def __init__(self, id, name):
        self.id = id
        self.name = name
class ProductOutOfStackHandler(IEventHandler):
    def handle(self, event):
        return {
            "message": f"Product Out Of Stack : {event.id}, {event.name}"
        }