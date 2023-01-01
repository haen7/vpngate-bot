import logging
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
import os
from urllib.request import urlopen
import re,base64,csv,io

# Port is given by render.com
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

# botfather token and render.com app name
# define as Environment Variables in render.com

TOKEN = os.environ.get('TOKEN')
APP_NAME = os.environ.get('APP_NAME', 'vpngate-bot') 

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Bot enabled', quote='true')

def stop(update, context):
    """Send a message when the command /stop is issued."""
    update.message.reply_text('Bot disabled', quote='true')
    
def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('/start - start Bot\n/stop - stop Bot\n/getovpn - fetch OVPN files\n/getsstp - fetch MS-SSTP urls\n/help - show help\n', quote='true') 

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def getovpn(update, context):
    update.message.reply_text("Please Wait While Fetch OVPN Files", quote='true')
    vpndata=urlopen("http://www.vpngate.net/api/iphone").read().decode('utf-8')
    vpndata=vpndata.replace("*","")
    vpnfile=io.StringIO(vpndata)
    
    # Telegram Bot
    bot = telegram.Bot(token=TOKEN)
    userId = update.message.chat_id
    
    with vpnfile as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        next(reader)
        next(reader)
        for row in reader:
            try:
                if int(row[2])>1100000 and int(row[2])<4000000 and int(row[7])>0 and int(row[3])<20 :
                    filename=row[5]+"-"+row[1]+".ovpn"
                    config=base64.b64decode(row[14])
                    bot.sendDocument(chat_id=userId, document=io.BytesIO(config), filename=str(filename))
            except Exception as e:
                break
            else:
                pass
            finally:
                pass
    update.message.reply_text("Done!")
    
def getsstp(update, context):
    update.message.reply_text("Please Wait While Fetch MS-SSTP urls", quote='true')
    vpndata=urlopen("http://www.vpngate.net/api/iphone").read().decode('utf-8')
    vpndata=vpndata.replace("*","")
    vpnfile=io.StringIO(vpndata)
    
    # Telegram Bot
    bot = telegram.Bot(token=TOKEN)
    userId = update.message.chat_id
    
    with vpnfile as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        next(reader)
        next(reader)
        for row in reader:
            try:
                if int(row[2])>1100000 and int(row[2])<4000000 and int(row[7])>0 and int(row[3])<20 :
                    config=row[0]+".opengw.net"
                    update.message.reply_text(config)
            except Exception as e:
                break
            else:
                pass
            finally:
                pass
    update.message.reply_text("user: vpn\npass: vpn")
    update.message.reply_text("Done!")

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher   
    
    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stop", stop))
    dp.add_handler(CommandHandler("getovpn", getovpn))
    dp.add_handler(CommandHandler("getsstp", getsstp))
    dp.add_handler(CommandHandler("help", help))
        
    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))
    
    # log all errors
    dp.add_error_handler(error)
    
    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook("https://{}.onrender.com/{}".format(APP_NAME, TOKEN))
    
    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()
    
if __name__ == '__main__':
    main()
