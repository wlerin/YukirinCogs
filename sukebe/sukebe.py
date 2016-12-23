import discord
from discord.ext import commands
import random

class Sukebe:
    """Paruru sensei can detect your Sukebe-ness."""

    def __init__(self, bot):
        self.bot = bot
        self.rng = random.Random()
        self.rng.seed() # seeds with system time or os.urandom()

    @commands.command(pass_context=True)
    async def sukebe(self, ctx, user: discord.Member):
        """Detects user's Sukebe-ness.

        157% accurate!"""

        # it's getting hot in here
        x = ":fire:" * self.rng.randint(5, 30)
        await self.bot.say("{}'s Sukebe-ness is : ".format(user.mention) + x)


def setup(bot):
    bot.add_cog(Sukebe(bot))
