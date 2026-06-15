import telebot
import random
import os

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

houses = [
    "🦁 Gryffindor",
    "🦅 Ravenclaw",
    "🐍 Slytherin",
    "🦡 Hufflepuff"
]

@bot.message_handler(commands=["sort"])
def sort_user(message):
    house = random.choice(houses)
    bot.reply_to(message, f"🎩 The Sorting Hat has decided!\nYou belong to {house}!")

bot.infinity_polling()
