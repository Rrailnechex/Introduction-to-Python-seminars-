from telegram.ext import *
from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

bot_token = ('6174085340:AAE50P9p82p2MxoiOneZxmnfi4l0j6nTuyE')
updater = Updater(bot_token, True)


print('Starting a bot....')


print("server started")
updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))


print('server start')
updater.start_polling()
updater.idle()
