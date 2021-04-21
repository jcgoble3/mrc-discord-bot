import time
import discord
import psutil
import os
import asyncio

from datetime import datetime
from discord.ext import commands
from utils import default


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.config = default.config()
        self.process = psutil.Process(os.getpid())

    ## Poll command @story{63}
    # The poll command provides users with a command in which they can
    # submit a question and two answer options which are then presented
    # to the channel in the form of a question, two answers and an emoji
    # button for each answer.
    #
    # A poll is really just a Message object that contains a formated 
    # string (the message) with a populated list of Reaction objects. 
    # For the purposes of this class, a poll is a Message object, which
    # contains a formatted string (the message) and two reactions.
    @commands.command()
    async def poll (self, ctx, question = "", answer_option_1 = "", answer_option_2 = ""):
        # The context object must not be None
        assert ctx, "ctx must not be None"

        # Test for empty input
        if (not (question and answer_option_1 and answer_option_2)):
            await ctx.send(f"Cannot create poll:")
            # Inform the user what is wrong with their use of the poll command
            if (not question):
                await ctx.send(f"No question was supplied.")            
            if (not answer_option_1): 
                await ctx.send(f"Answer option #1 was not supplied.")            
            if (not answer_option_2):
                await ctx.send(f"Answer option #2 was not supplied.")
            return

        # Create the poll 
        poll = await ctx.send(f"```" + question + "```\n**✅ = " + answer_option_1 + "**\n**❎ = " + answer_option_2 + "**")
        # Verify the message was created.
        # In the interest of time, only two fields are verified here to demonstrate
        # understanding of the concept. It can be fairly argued that an assert needs
        # added for every field of the object to verify it was created correctly but
        # that seems execessive and unnecessary for the purposes of this class.
        assert poll.id >= 0, "The message must have a valid ID"
        assert poll.channel == ctx.channel, "The message must be for the same channel that was passed as an argument to poll"

        # Add the first reaction
        await poll.add_reaction('✅') 
        poll = await ctx.fetch_message(poll.id)
        assert len(poll.reactions) == 1, "One reaction must be added to the message"

        await poll.add_reaction('❎')
        poll = await ctx.fetch_message(poll.id)
        assert len(poll.reactions) == 2, "A second reaction must be added to the message"

    @commands.command()
    async def trivia (self, ctx, arg1 = "", arg2 = ""):

        # *** BEGIN ***
        if (arg1.lower() == "begin" or arg1.lower() == "start"):
            if (self.bot.trivia.inProgress):
                await ctx.send("Trivia is already in progress")
            else:
                await ctx.send("Starting trivia...")
                if (self.bot.trivia.start() == 0):
                    self.bot.trivia.inProgress = True
   
        # *** END ***
        elif (arg1.lower() == "end" or arg1.lower() == "stop"):
            if (self.bot.trivia.inProgress):
                await ctx.send("Stopping trivia...")
                if (self.bot.trivia.end() == 0):
                    self.bot.trivia.inProgress = False
            else:
                await ctx.send("Trivia is not in progress")

        # *** STATUS ***
        elif (arg1.lower() == "status"):
            await ctx.send(self.bot.trivia.status())
        
        # *** ANSWER ***
        elif (arg1.lower() == "answer"):
            if (self.bot.trivia.check(arg2) == 0):
                await ctx.send(f"Answer: " + arg2 + " is correct!")
            else:
                await ctx.send(f"Sorry, answer: " + arg2 + " is incorrect.")
                
        else:
            await ctx.send("arg1: " + arg1)
 
    ## Proof of concept for use with @story{9}
    @commands.command()
    async def hello(self, ctx):
        """Greet the user and ask them how their day is."""
        # These lines send the greeting
        await ctx.send(f"Hello: " + ctx.author.name + " my name is Test Bot!")
        await ctx.send(f"How are you today?")

        # The purpose of the check function is to filter out messages so that only the
        # message the wait_for function is looking for is returned
        def check(msg):
            # check that the channel is the same between the message and the context
            channel_result = msg.channel == ctx.channel

            # check that the author is the same between the message and the context
            author_result = msg.author == ctx.author

            return channel_result and author_result

        try:
            # This line waits for a response from the user. The wait period times out
            # after 10 seconds. When a timeout occurs, an asyncio.TimeoutError execption
            # is thrown. This execption is caught on the next line and a response is sent
            # to the channel, informing the user by name, that they took to long to respond.
            msg = await self.bot.wait_for('message', timeout=10.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Sorry " + ctx.author.name + " you took too long to respond")
        else:
            # These lines customize the bot's response based on user input.
            if msg.content.lower() == "bad":
                await ctx.send("That's bad!")
            elif msg.content.lower() == "good":
                await ctx.send("That's good!")
            elif msg.content.lower() == "great":
                await ctx.send("That's great!")
            else:
                await ctx.send("I'm sorry, I don't understand your response")

    @commands.command()
    async def ping(self, ctx):
        """ Pong! """
        before = time.monotonic()
        before_ws = int(round(self.bot.latency * 1000, 1))
        message = await ctx.send("🏓 Pong")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"🏓 WS: {before_ws}ms  |  REST: {int(ping)}ms")

    @commands.command(aliases=['joinme', 'join', 'botinvite'])
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\n<{discord.utils.oauth_url(self.bot.user.id)}>")

    @commands.command()
    async def source(self, ctx):
        """ Check out my source code <3 """
        # Do not remove this command, this has to stay due to the GitHub LICENSE.
        # TL:DR, you have to disclose source according to MIT.
        # Reference: https://github.com/AlexFlipnote/discord_bot.py/blob/master/LICENSE
        await ctx.send(f"**{ctx.bot.user}** is powered by this source code:\nhttps://github.com/AlexFlipnote/discord_bot.py")

    @commands.command(aliases=['supportserver', 'feedbackserver'])
    async def botserver(self, ctx):
        """ Get an invite to our support server! """
        if isinstance(ctx.channel, discord.DMChannel) or ctx.guild.id != 86484642730885120:
            return await ctx.send(f"**Here you go {ctx.author.name} 🍻\n<{self.config['botserver']}>**")
        await ctx.send(f"**{ctx.author.name}** this is my home you know :3")

    @commands.command(aliases=['info', 'stats', 'status'])
    async def about(self, ctx):
        """ About the bot """
        ramUsage = self.process.memory_full_info().rss / 1024**2
        avgmembers = sum(g.member_count for g in self.bot.guilds) / len(self.bot.guilds)

        embedColour = discord.Embed.Empty
        if hasattr(ctx, 'guild') and ctx.guild is not None:
            embedColour = ctx.me.top_role.colour

        embed = discord.Embed(colour=embedColour)
        embed.set_thumbnail(url=ctx.bot.user.avatar_url)
        embed.add_field(name="Last boot", value=default.timeago(datetime.now() - self.bot.uptime), inline=True)
        embed.add_field(
            name=f"Developer{'' if len(self.config['owners']) == 1 else 's'}",
            value=', '.join([str(self.bot.get_user(x)) for x in self.config["owners"]]),
            inline=True
        )
        embed.add_field(name="Library", value="discord.py", inline=True)
        embed.add_field(name="Servers", value=f"{len(ctx.bot.guilds)} ( avg: {avgmembers:,.2f} users/server )", inline=True)
        embed.add_field(name="Commands loaded", value=len([x.name for x in self.bot.commands]), inline=True)
        embed.add_field(name="RAM", value=f"{ramUsage:.2f} MB", inline=True)

        await ctx.send(content=f"ℹ About **{ctx.bot.user}** | **{self.config['version']}**", embed=embed)


def setup(bot):
    bot.add_cog(Information(bot))
