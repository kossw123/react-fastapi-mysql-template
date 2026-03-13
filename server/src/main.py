from src.config import app
from src.bootstrap import bootstrap


container = bootstrap()

event_dispatcher = container["eventDispatcher"]
command_bus = container["commandBus"]
uow = container["unitOfWork"]