class SubscribeToBusLineUseCase:
    def __init__(self, bus_line_repository: BusLineRepository):
        self.bus_line_repository = bus_line_repository

    def subscribe(self, bus_line: BusLine):
        self.bus_line_repository.save(bus_line)
