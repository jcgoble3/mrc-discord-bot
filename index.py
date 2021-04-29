from utils.bot import bot, config

print("Logging in...")
try:
    bot.run(config["token"])
except Exception as e:
    print(f'Error when logging in: {e}')
