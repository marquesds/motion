from typing import Protocol

from motion.subscriptions.entities import Bus, Passenger


class SubscriptionRepository(Protocol):
    def follow(self, passenger: Passenger, bus: Bus) -> None:
        ...

    def unfollow(self, passenger: Passenger, bus: Bus) -> None:
        ...


class PostRepository(Protocol):
    ...
