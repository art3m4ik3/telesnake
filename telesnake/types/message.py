from dataclasses import dataclass
from .user import User
from .chat import Chat


@dataclass
class Message:
    id: int
    author: User
    chat: Chat
    content: str
    date: int

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["message_id"],
            author=User.from_dict(data["from"]),
            chat=Chat.from_dict(data["chat"]),
            content=data.get("text", ""),
            date=data["date"],
        )
