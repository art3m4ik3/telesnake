class Context:
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    async def send(self, content: str, reply_markup=None):
        return await self.bot.send_message(self.message.chat.id, content, reply_markup)
