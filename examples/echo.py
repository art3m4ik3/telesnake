from telesnake import Bot, Context
import os

bot = Bot(os.getenv("TOKEN"))


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command()
async def start(ctx: Context):
    await ctx.send("Hello! I'm a TelePy bot.")


@bot.event
async def on_message(ctx: Context):
    if ctx.message.content.startswith(bot.prefix):
        return

    await ctx.send(ctx.message.content)


if __name__ == "__main__":
    bot.run()
