
import logging
import os

from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# Load environment variables from the project root
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    message = (
        "👋 Welcome to StreamLink!\n\n"
        "Your file, your link.\n"
        "Simple file delivery with StreamLink.\n\n"
        "📤 Send me a file to get started.\n\n"
        "Use /help to see available commands."
    )

    if update.message:
        await update.message.reply_text(message)


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    message = (
        "📚 StreamLink Help\n\n"
        "/start - Start the bot\n"
        "/help - Show available commands\n"
        "/about - About StreamLink\n"
        "/ping - Check bot status\n\n"
        "File-link generation is coming soon!"
    )

    if update.message:
        await update.message.reply_text(message)


async def about(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    message = (
        "🔗 StreamLink Bot\n\n"
        "Your file, your link.\n"
        "Simple file delivery with StreamLink.\n\n"
        "Built with Python and the Telegram Bot API."
    )

    if update.message:
        await update.message.reply_text(message)


async def ping(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    if update.message:
        await update.message.reply_text("🏓 Pong! StreamLink is online.")


async def post_init(application: Application) -> None:
    commands = [
        BotCommand("start", "Start StreamLink"),
        BotCommand("help", "Get help"),
        BotCommand("about", "About StreamLink"),
        BotCommand("ping", "Check bot status"),
    ]

    await application.bot.set_my_commands(commands)
    logger.info("Bot commands registered successfully.")


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError(
            "TELEGRAM_BOT_TOKEN is missing. "
            "Check the .env file in the project root."
        )

    application = (
        Application.builder()
        .token(BOT_TOKEN)
        .post_init(post_init)
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about))
    application.add_handler(CommandHandler("ping", ping))

    logger.info("Starting StreamLink Bot...")
    application.run_polling()


if __name__ == "__main__":
    main()
