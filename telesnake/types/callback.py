from dataclasses import dataclass
from .user import User
from .message import Message
from .chat import Chat


@dataclass
class CallbackQuery:
    id: str
    from_user: User
    message: Message
    chat_instance: str
    data: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            from_user=User.from_dict(data["from"]),
            message=Message.from_dict(data["message"]),
            chat_instance=data["chat_instance"],
            data=data["data"],
        )
