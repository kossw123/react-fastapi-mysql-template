from src.config import create_app
from src.bootstrap import bootstrap


app = create_app()
container = bootstrap()

event_dispatcher = container["eventDispatcher"]
command_bus = container["commandBus"]
uow = container["unitOfWork"]
