from typing import Protocol


class SubscriptionRepository(Protocol):
    def follow(self, passenger, bus):
        ...

    def unfollow(self, passenger, bus):
        ...


class MongoBusLineRepository:
    def list(self, line=None):
        ...


class PostRepository(Protocol):
    def list(self, passenger):
        ...
