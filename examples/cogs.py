from telesnake import Bot, Context, Cog, command, listener
from telesnake.utils import InlineKeyboardMarkup, InlineKeyboardButton
import os

bot = Bot(os.getenv("TOKEN"))


class ExampleCog(Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @listener(name="on_message")
    async def on_message(self, ctx: Context):
        if ctx.message.content.startswith(self.bot.prefix):
            return

        await ctx.send(ctx.message.content)

    @command(name="hello")
    async def hello_command(self, ctx: Context):
        await ctx.send("Hello from Cog!")

    @command(name="button")
    async def button(self, ctx: Context):
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Click me", callback_data="button_click"))
        await ctx.send("Press the button", reply_markup=markup)

    @listener(name="on_callback_query")
    async def on_callback_query(self, ctx: Context, callback_query):
        data = callback_query.data
        if data == "button_click":
            await ctx.send("Button clicked!")


@bot.event
async def on_ready():
    print("Bot is ready!")


if __name__ == "__main__":
    bot.add_cog(ExampleCog(bot))
    bot.run()
