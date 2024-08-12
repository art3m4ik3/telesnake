from dataclasses import dataclass


@dataclass
class Chat:
    id: int
    type: str
    title: str = None
    username: str = None
    first_name: str = None
    last_name: str = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)
