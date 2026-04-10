from abc import abstractmethod


class ICommandHandler:
    @abstractmethod
    def handle(self, command):
        pass
