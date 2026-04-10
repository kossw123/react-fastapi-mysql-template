from abc import abstractmethod


class IEventHandler:
    @abstractmethod
    def handle(self, event):
        pass
