# ----------------------------------
# Ralsei/cogs/games_cog
# Created by Infinidoge
# ----------------------------------
# Cog for Ralsei to contain all game commands
# ----------------------------------
"""The Ralsei Games cog, contains all commands related to games with the bot (such as rock, paper, scissors.)"""

import random
import asyncio

from discord.ext import commands


class Games:
    """The Ralsei Games cog, contains all commands related to games with the bot (such as rock, paper, scissors.)"""

    def __init__(self, ralsei):
        self.ralsei = ralsei

    @commands.command()
    async def rps(self, ctx, *, player_move=None):
        """Play rock, paper, scissors with Ralsei!"""
        com_move = random.randint(1, 3)
        if player_move is None:
            await ctx.send("Hai, try running the command with a move of either Rock, Paper, or Scissors. "
                           "(and they can be lowercase)")
        elif player_move.lower() not in ["rock", "paper", "scissors"]:
            await ctx.send("That isn't rock, paper, or scissors. Try again?")
        else:
            player_move = 1 if (player_move.lower() == "rock") else 2 if (player_move.lower() == "paper") else 3

            await ctx.send("Let's Play!")
            await asyncio.sleep(1)
            await ctx.send("Rock, Paper, Scissors!")
            await asyncio.sleep(1)
            await ctx.send("I choose %s!" % ("rock" if (com_move == 1) else "paper" if (com_move == 2) else "scissors"))
            await asyncio.sleep(0.5)
            await ctx.send("Sorry, I win!" if (com_move > player_move or com_move == 3 and player_move == 1) else
                           "Congrats, you win!" if (player_move > com_move or player_move == 3 and com_move == 1) else
                           "Ah well, it's a tie!")
