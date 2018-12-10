# ----------------------------------
# Ralsei/cogs/dnd_cog
# Created by Infinidoge
# ----------------------------------
# Cog for Ralsei to contain all dnd related commands
# ----------------------------------
"""The Ralsei D&D cog, contains all commands related to D&D utilities (such as generating stats)"""

import random

from discord.ext import commands


def replace_greater(iter, index, value):
    iter[index] = value if iter[index] < value else iter[index]
    return iter


class DnD:
    """The Ralsei D&D cog, contains all commands related to D&D utilities (such as generating stats)"""
    def __init__(self, ralsei):
        self.ralsei = ralsei

    class GenStats:
        @staticmethod
        def infinidoge_standard():
            stat_block = []
            while sum(stat_block) < 70:
                stat_block = [random.randint(1, 20) for i in range(6)]

            return ["18 (%s)" % str(i) if (i > 18)
                    else i for i in sorted(replace_greater(sorted([random.randint(6, 20) if (i < 6)
                                                                   else i for i in stat_block]),
                                                           0, random.randint(1, 20)))]

        @staticmethod
        def critrole_standard():
            def block_gen():
                return sorted([random.randint(1, 6) for i in range(4)])[1:]

            stat_block = []
            while sum([sum(i) for i in stat_block]) < 70:
                stat_block = sorted([block_gen() for i in range(6)])
                print(str(stat_block) + " : " + str(sum([sum(i) for i in stat_block])))
            return [sum(i) for i in stat_block]

    @commands.group(invoke_without_command=True)
    async def dnd(self, ctx):
        await ctx.send("Uh, not sure what to do with that...")

    @dnd.command()
    async def stats(self, ctx):
        await ctx.send("[<@%s>]\n{%s}" % (ctx.message.author.id,
                                          str(" - ".join([str(i)
                                                         for i in self.GenStats.infinidoge_standard()]))))

    @dnd.command()
    async def test(self, ctx):
        await ctx.send(str(self.GenStats.critrole_standard()))

