from dataclasses import dataclass


@dataclass
class Bus:
    line: str
    name: str


@dataclass
class Passenger:
    name: str
    email: str
    subscriptions: list[Bus]


@dataclass
class Post:
    bus: Bus
    passenger: Passenger
    text: str
