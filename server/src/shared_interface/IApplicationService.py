from abc import ABC, abstractmethod


class IApplicationService(ABC):
    def __init__ (self):
        pass

    @abstractmethod
    def context_command(self):
        pass