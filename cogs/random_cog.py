# ----------------------------------
# Ralsei/cogs/random_cog
# Created by Infinidoge
# ----------------------------------
# Cog for Ralsei to contain all random generation related commands
# ----------------------------------
"""The Ralsei Random cog, contains all commands related to randomly generating objects (such as rolling dice)"""

import random

from discord.ext import commands


class Random:
    """The Ralsei Random cog, contains all commands related to randomly generating objects (such as rolling dice)"""

    def __init__(self, ralsei):
        self.ralsei = ralsei

    @commands.command()
    async def roll(self, ctx, roll: str):
        """Roll a dice in NdM±X format(Ex. 1d20+5, 1d8-3, 1d4)"""

        if "d" not in roll.lower():
            await ctx.send("I'm not sure how to roll that, sorry!")
            return

        try:
            num, pre = roll.split("d")
            num = int(num)
            if "+" in pre:
                dice, mod = pre.split("+")
                dice, mod = int(dice), int(mod)
            elif "-" in pre:
                dice, mod = pre.split("-")
                dice, mod = int(dice), int(mod)
                mod = mod * (-1)
            else:
                dice, mod = pre, 0
                dice = int(dice)

            dice_block = [random.randint(1, dice) for i in range(num)]

            await ctx.send("""[{0}]\n:game_die: **Rolling:** {1}d{2}{3}{4}:\n{5}{6}\n**Sum:**{7}
                           """.format("<@%s>" % ctx.author.id,
                                      str(num), str(dice),
                                      "+" if (mod > 0) else "-" if (mod < 0) else "",
                                      "" if (mod is 0) else str(mod),
                                      "+".join([str(i) for i in dice_block]),
                                      "%s%s" % ("**+" if (mod > 0) else "**-" if (mod < 0) else "",
                                                "" if (mod is 0) else str(mod)+"**"),
                                      str(sum(dice_block)+mod)))

        except ValueError:
            await ctx.send("I don't seem to be able to roll that, sorry!")

    @commands.command()
    async def flip(self, ctx):
        """Flip a coin!"""

        await ctx.send("""[{0}]\n**Coin Flip:**\n{1}""".format("<@%s>" % ctx.author.id,
                                                               "Heads!" if (random.randint(1, 2) == 1) else "Tails!"))

    @commands.command()
    async def choose(self, ctx, *, arg):
        """Chooses one thing from a list of inputs, separated by ', '"""

        choices = arg.split(", ")

        await ctx.send("""[{0}]\n**Choices:** {1}\n**My Choice: **{2}
                       """.format("<@%s>" % ctx.author.id,
                                  ", ".join(choices), random.choice(choices)))
