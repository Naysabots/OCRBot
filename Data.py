from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
🌟 Hey {}

🚴‍♂️ I am Image To Text Bot

🎸 I can extract text from images using OCR technology.

🏍️ Maintained By : @NaysaBots
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")],
        [InlineKeyboardButton(text="🏠 Return Home 🏠", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("✨ Bot Status and More Bots ✨", url="https://t.me/StarkBots/7")
        ],
        [
            InlineKeyboardButton("How to Use ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ More Amazing bots ♥", url="https://t.me/StarkBots")],
        [InlineKeyboardButton("🎨 Support Group 🎨", url="https://t.me/StarkBotsChat")],
    ]

    # Help Message
    HELP = """
❄️ Just Send Image To Detect Text and Get Started
    """

    # About Message
    ABOUT = """
**About This Bot** 

Bot created by @StarkBots

Source Code : [Click Here](https://github.com/StarkBotsIndustries/OCRBot)

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : @StarkProgrammer
    """
