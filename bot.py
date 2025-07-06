import os import json import random from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Document from telegram.ext import ( ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, ContextTypes, filters )

تنظیمات اصلی

BOT_TOKEN = "7978339304:AAESYFoIzMymbwoc4Vfsg3TyAmcR0MQOp_c" ADMIN_ID = 7112285392 CHANNEL_USERNAME = "@V2File_Mamad" BASE_DIR = "configs" PRICE_FILE = "prices.json"

CATEGORIES = ["free", "paid", "vip"] DEFAULT_PRICES = {"paid": 50000, "vip": 100000}

ساخت پوشه و فایل قیمت

for cat in CATEGORIES: os.makedirs(os.path.join(BASE_DIR, cat), exist_ok=True) if not os.path.exists(PRICE_FILE): with open(PRICE_FILE, "w") as f: json.dump(DEFAULT_PRICES, f) with open(PRICE_FILE) as f: prices = json.load(f)

متغیرهای موقتی

admin_pending_files = {} admin_waiting_for_price = False pending_payments = {}

منوی اصلی

def get_main_menu(is_admin=False): keyboard = [ [InlineKeyboardButton("\ud83d\udcc5 \u0641\u0627\u06cc\u0644 \u0631\u0627\u06cc\u06af\u0627\u0646", callback_data="get_free")], [InlineKeyboardButton("\ud83d\udcb0 \u0641\u0627\u06cc\u0644 \u067e\u0648\u0644\u06cc", callback_data="get_paid")], [InlineKeyboardButton("\ud83c\udf1f \u0641\u0627\u06cc\u0644 VIP", callback_data="get_vip")], [InlineKeyboardButton("\u2139\ufe0f \u062f\u0631\u0628\u0627\u0631\u0647 \u0645\u0627", callback_data="about")] ] if is_admin: keyboard.append([InlineKeyboardButton("\ud83d\udcb5 \u062a\u0646\u0638\u06cc\u0645 \u0642\u06cc\u0645\u062a", callback_data="set_price")]) return InlineKeyboardMarkup(keyboard)

/start

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): user_id = update.effective_user.id is_admin = (user_id == ADMIN_ID) await update.message.reply_text( "\ud83c\udf89 \u062e\u0648\u0634 \u0627\u0648\u0645\u062f\u06cc! \u06cc\u06a9\u06cc \u0627\u0632 \u06af\u0632\u06cc\u0646\u0647\u200c\u0647\u0627 \u0631\u0648 \u0627\u0646\u062a\u062e\u0627\u0628 \u06a9\u0646 \ud83d\udc47", reply_markup=get_main_menu(is_admin) )

اجرای ربات

def main(): app = ApplicationBuilder().token(BOT_TOKEN).build() app.add_handler(CommandHandler("start", start)) print("\ud83e\udd16 \u0631\u0628\u0627\u062a \u0622\u0645\u0627\u062f\u0647 \u0627\u062c\u0631\u0627\u0633\u062a...") app.run_polling()

if name == "main": main()

