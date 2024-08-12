# Telesnake

<p align="center">
     <a href="https://pypi.org/project/Telesnake/"><img src="https://img.shields.io/pypi/v/Telesnake.svg?style=flat-square" alt="PyPI version info" /></a>
    <a href="https://pypi.org/project/Telesnake/"><img src="https://img.shields.io/pypi/pyversions/Telesnake.svg?style=flat-square" alt="PyPI supported Python versions" /></a>
    <a href="https://github.com/art3m4ik3/telesnake/commits"><img src="https://img.shields.io/github/commit-activity/w/art3m4ik3/Telesnake.svg?style=flat-square" alt="Commit activity" /></a>
</p>

Telegram API Wrapper: modern, similar to Discord libraries

# Features
* Quick response
* Simplicity
* And more...

# Installing
Python 3.8 or higher is required.

To install the library, you need to enter these commands into the console
```bash
# Linux/MacOS
python3 -m pip install -U Telesnake

# Windows
py -3 -m pip install -U Telesnake
```

# Quick Example
Echo bot
```py
from telesnake import Bot, Context
import os

bot = Bot(os.getenv("TOKEN"))

@bot.event
async def on_message(ctx: Context):
    await ctx.send(ctx.message.content)

bot.run()
```
You can find more examples in the [examples directory](https://github.com/art3m4ik3/telesnake/tree/main/examples)

<br>
<p align="center">
    <a href="https://ll-u.ru">My Website</a>
    ⁕
    <a href="https://github.com/art3m4ik3/telesnake/issues">Github Issues</a>
    ⁕
    <a href="https://core.telegram.org/bots/api">Telegram API</a>
</p>
<br>
