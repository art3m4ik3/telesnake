import asyncio
import aiohttp
from .types import Message, User, CallbackQuery
from .context import Context
from .cog import Cog, command, listener


class Bot:
    def __init__(self, token: str, *, prefix: str = "/"):
        self.token = token
        self.prefix = prefix
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.session = None
        self.commands = {}
        self.events = {}
        self.cogs = {}  # Инициализация атрибута cogs

    def event(self, coro):
        self.events[coro.__name__] = coro
        return coro

    def command(self, name=None):
        def decorator(func):
            command_name = name or func.__name__
            self.commands[command_name] = func
            return func

        return decorator

    def add_cog(self, cog):
        self.cogs[cog.__class__.__name__] = cog
        cog.bot = self
        for name, method in cog.__class__.__dict__.items():
            if hasattr(method, "__command__"):
                self.commands[method.__command__] = method.__get__(cog)
            elif hasattr(method, "__event__"):
                self.events[method.__event__] = method.__get__(cog)

    async def start(self):
        self.session = aiohttp.ClientSession()
        me = await self.get_me()
        print(f"Bot started: @{me.username}")
        if "on_ready" in self.events:
            await self.events["on_ready"]()
        await self.poll_updates()

    async def stop(self):
        if self.session:
            await self.session.close()

    async def send_message(self, chat_id: int, text: str, reply_markup=None):
        data = {"chat_id": chat_id, "text": text}
        if reply_markup:
            data["reply_markup"] = reply_markup.to_json()
        async with self.session.post(
            self.base_url + "sendMessage", json=data
        ) as response:
            return await response.json()

    async def get_me(self):
        async with self.session.get(self.base_url + "getMe") as response:
            data = await response.json()
            return User.from_dict(data["result"])

    async def poll_updates(self):
        offset = 0
        while True:
            async with self.session.get(
                self.base_url + f"getUpdates?offset={offset}&timeout=30"
            ) as response:
                updates = await response.json()
                for update in updates.get("result", []):
                    offset = update["update_id"] + 1
                    await self.process_update(update)

    async def process_update(self, update: dict):
        if "message" in update:
            message = Message.from_dict(update["message"])
            ctx = Context(self, message)

            if message.content and message.content.startswith(self.prefix):
                command_name = message.content[len(self.prefix) :].split()[0]
                if command_name in self.commands:
                    await self.commands[command_name](ctx)

            if "on_message" in self.events:
                await self.events["on_message"](ctx)

        elif "callback_query" in update:
            callback_query = CallbackQuery.from_dict(update["callback_query"])
            ctx = Context(self, callback_query.message)

            if "on_callback_query" in self.events:
                await self.events["on_callback_query"](ctx, callback_query)

    def run(self):
        asyncio.run(self.start())
