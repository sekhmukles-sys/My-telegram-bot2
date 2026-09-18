Telegram Bot (Termux Edition)
# Clean Version + Smart AI + Typing Effect
# Works for python-telegram-bot v20+
# -----------------------------
import os
import requests
from datetime import datetime
from bs4 import BeautifulSoup
import random
import asyncio
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    ContextTypes,
    filters,
)
# -----------------------------
# BOT TOKEN
# -----------------------------
BOT_TOKEN = "8644668603:AAEqiSwXwRYiihUjJeRdZFmBaAdZpVHjfBY"
# -----------------------------
# TYPING EFFECT
# -----------------------------
async def type_message(update: Update, context: ContextTypes.DEFAULT_TYPE, text: str):
    """Send typing animation + message."""
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    await asyncio.sleep(0.5)
    await update.message.reply_text(text)
# -----------------------------
# START
# -----------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await type_message(update, context, "👋 Hello! Welcome.\nType /help to see all commands.")
# -----------------------------
# HELP MENU
# -----------------------------
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "📌 *Available Commands:*\n"
        "/start - Start bot\n"
        "/help - Help\n"
        "/time - Current time\n"
        "/info - Your info\n"
        "/calc 10+5 - Calculator\n"
        "/menu - Show buttons\n"
        "/title url - Get website title\n"
        "/joke - Random joke\n\n"
        "✨ *AI Chat:* Just type normally."
    )
    await update.message.reply_text(text, parse_mode="Markdown")
# -----------------------------
# TIME
# -----------------------------
async def time_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    await type_message(update, context, f"⏱️ Current Time:\n{now}")
# -----------------------------
# USER INFO
# -----------------------------
async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    text = (
        f"👤 Name: {user.first_name}\n"
        f"🆔 User ID: {user.id}\n"
        f"🌐 Username: @{user.username}"
    )
    await update.message.reply_text(text)
