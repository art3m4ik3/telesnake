class Cog:
    def __init__(self, bot):
        self.bot = bot


def command(name=None):
    def decorator(func):
        func.__command__ = name or func.__name__
        return func

    return decorator


def listener(name=None):
    def decorator(func):
        func.__event__ = name or func.__name__
        return func

    return decorator
