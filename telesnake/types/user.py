from dataclasses import dataclass


@dataclass
class User:
    id: int
    is_bot: bool
    first_name: str
    last_name: str = None
    username: str = None
    can_join_groups: bool = None
    can_read_all_group_messages: bool = None
    supports_inline_queries: bool = None

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id=data["id"],
            is_bot=data["is_bot"],
            first_name=data["first_name"],
            last_name=data.get("last_name"),
            username=data.get("username"),
            can_join_groups=data.get("can_join_groups"),
            can_read_all_group_messages=data.get("can_read_all_group_messages"),
            supports_inline_queries=data.get("supports_inline_queries"),
        )
