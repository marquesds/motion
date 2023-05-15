from dataclasses import dataclass


@dataclass
class Bus:
    id: int
    line: str
    name: str


@dataclass
class Passenger:
    id: int
    name: str
    email: str
    profile_image: str


@dataclass
class Post:
    id: int
    line: Bus
    passenger: str
    content: str
    likes: int
    created_at: str
