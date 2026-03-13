from abc import ABC, abstractmethod


class ICommandHandler():
    @abstractmethod
    def handle(self, command):
        pass