import discord

from utils.trivia import QuestionAnswer, QuestionList, Trivia
from utils import permissions
from discord.ext.commands import AutoShardedBot, DefaultHelpCommand

class Bot(AutoShardedBot):
    trivia: Trivia

    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix
        self.trivia = Trivia()

    async def on_message(self, msg):
        if not self.is_ready() or not permissions.can_handle(msg, "send_messages"):
            return

        await self.process_commands(msg)

    ## @story{51} In order to test command coroutines, a second bot is needed.
    # The default discord.py Bot class does not respond to other bots, so we
    # must override this method to allow complete testing.
    async def process_commands(self, message):
        # Do nothing if sent by a bot that is not the testing bot
        if message.author.bot and message.author.id != 834537991397572618:
            return

        ctx = await self.get_context(message)
        await self.invoke(ctx)

class HelpFormat(DefaultHelpCommand):
    def get_destination(self, no_pm: bool = False):
        if no_pm:
            return self.context.channel
        else:
            return self.context.author

    async def send_error_message(self, error):
        destination = self.get_destination(no_pm=True)
        await destination.send(error)

    async def send_command_help(self, command):
        self.add_command_formatting(command)
        self.paginator.close_page()
        await self.send_pages(no_pm=True)

    async def send_pages(self, no_pm: bool = False):
        try:
            if permissions.can_handle(self.context, "add_reactions"):
                await self.context.message.add_reaction(chr(0x2709))
        except discord.Forbidden:
            pass

        try:
            destination = self.get_destination(no_pm=no_pm)
            for page in self.paginator.pages:
                await destination.send(page)
        except discord.Forbidden:
            destination = self.get_destination(no_pm=True)
            await destination.send("Couldn't send help to you due to blocked DMs...")
