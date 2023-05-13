from motion.subscriptions.entities import Bus, Passenger, Post


class BusRepository:
    def create(self, bus: Bus) -> Bus:
        # db.collection.update(
        #     {username:"Bob"},
        #     {$set:{'longitude': '58.3', 'latitude': '0.3'}},
        #     { upsert: true}
        # )
        ...


class PassengerRepository:
    ...


class SubscriptionRepository:
    ...
