import json


class InlineKeyboardMarkup:
    def __init__(self):
        self.inline_keyboard = []

    def add(self, *buttons):
        self.inline_keyboard.append([button.to_dict() for button in buttons])

    def to_json(self):
        return json.dumps({"inline_keyboard": self.inline_keyboard})


class InlineKeyboardButton:
    def __init__(self, label, callback_data=None, url=None):
        self.label = label
        self.callback_data = callback_data
        self.url = url

    def to_dict(self):
        button = {"text": self.label}
        if self.callback_data:
            button["callback_data"] = self.callback_data
        if self.url:
            button["url"] = self.url
        return button
