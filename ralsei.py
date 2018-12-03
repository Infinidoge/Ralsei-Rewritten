# ----------------------------------
# Ralsei Base
# Created by Infinidoge
# ----------------------------------
# Ralsei discord bot.
# ----------------------------------
"""The Ralsei Discord Bot File, containing the Ralsei bot class"""

import time

import discord
from discord.ext import commands

from pypresence import Presence, exceptions


from utils.config import Config
from utils.correction import command_correct
from utils.spell_correct import correct

from cogs.random_cog import Random


configuration = Config()


class Ralsei(commands.Bot):
    def __init__(self, config):
        self.config = config
        super(Ralsei, self).__init__(command_prefix=config.command_prefix,
                                     description="""Ralsei, the Fluffiest Bot on Discord!""",
                                     case_insensitive=config.case_insensitive,
                                     pm_help=config.pm_help,
                                     command_not_found=config.command_not_found,
                                     command_has_no_subcommands=config.command_has_no_subcommands,
                                     owner_id=config.owner_id if (config.owner_id != "") else None,
                                     activity=discord.Activity(name="In an Unknown World",
                                                               url="https://www.twitch.tv/discord_ralsei",
                                                               type=discord.ActivityType.streaming))
        try:
            self.RPC = Presence(config.app_id)
            self.RPC.connect()
            self.RPC.update(start=int(time.time()),
                            details="in an Unknown World",
                            state="Most likely with Python",
                            large_image="ralsei_uh",
                            large_text="nothing to see here")
        except exceptions.InvalidPipe or FileNotFoundError:
            pass

    def ralsei_run(self):
        self.run(self.config.token)


ralsei = Ralsei(configuration)


@ralsei.event
async def on_ready():
    print('Logged in as')
    print(ralsei.user.name)
    print(ralsei.user.id)
    print('------')


@ralsei.event
async def on_command_error(ctx, error):
    if type(error) == discord.ext.commands.errors.CommandNotFound:
        cmd = ctx.message.content.replace(ralsei.config.command_prefix, "").split(" ")[0]
        suggestion = command_correct(cmd)
        await ctx.send("<@%s>, I don't understand `%s`, did you mean `%s`?" % (ctx.message.author.id, cmd,
                                                                               suggestion)
                       if (suggestion != cmd) else "I'm not sure what command that is, sorry!")

    elif type(error) == discord.ext.commands.errors.MissingRequiredArgument:
        await ctx.send("<@%s>, You seem to be missing some arguments for that command." % ctx.message.author.id)

    else:
        await ctx.send("<@%s>, I'm sorry, but i'm not sure how to respond to that..." % ctx.message.author.id)


@ralsei.command()
@commands.is_owner()
async def echo(ctx, *args):
    """Echos everything after the command."""
    msg = " ".join(args)
    await ctx.send(msg)
    await ctx.message.delete()


@echo.error
async def echo_error(ctx, error):
    if isinstance(error, commands.errors.NotOwner):
        await ctx.send(error)


@ralsei.command()
@commands.is_owner()
async def shutdown(ctx):
    """Shuts down Ralsei"""
    await ctx.send("See ya later!")
    await ralsei.close()

ralsei.add_cog(Random(ralsei))
ralsei.ralsei_run()
