from motion.subscriptions.entities import Bus, Passenger


class Config:
    def load_database(self):
        ...

    def get_connection(self):
        ...


class MongoSubscriptionRepository:
    def __init__(self, config: Config):
        self.config = config
        self.connection = self.config.get_connection()

    def follow(self, passenger: Passenger, bus: Bus) -> None:
        ...

    def unfollow(self, passenger: Passenger, bus: Bus) -> None:
        ...


class MongoPostRepository:
    ...
