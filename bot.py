import logging
import wikipedia
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from event_analyzer import analyze_event

wikipedia.set_lang("en")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! Send me a historical event (in English), and I’ll try to find its causes!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    try:
        summary = wikipedia.summary(query, sentences=5)
        await update.message.reply_text(f"Wikipedia summary:\n\n{summary}")

        
        causes = await analyze_event(summary)
        await update.message.reply_text(f"Causes analysis:\n\n{causes}")

    except wikipedia.exceptions.DisambiguationError as e:
        await update.message.reply_text(f"Too many results. Try to be more specific.\nOptions:\n{e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await update.message.reply_text("Couldn't find anything on that topic.")
    except Exception as e:
        await update.message.reply_text(f"Something went wrong: {str(e)}")

if __name__ == '__main__':
    import os
    from dotenv import load_dotenv

    load_dotenv()
    TOKEN = os.getenv("BOT_TOKEN")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    app.run_polling()
