from abc import ABC, abstractmethod


class IEventHandler():
    @abstractmethod
    def handle(self, event):
        pass